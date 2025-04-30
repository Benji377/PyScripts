import requests
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import random
import os
from multiprocessing import Pool, cpu_count
from time import sleep
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

# Letterboxd Watch Time Analyzer
#
# This script allows you to scrape a Letterboxd user's film history and calculate
# total watch time, generate CSV reports, and create PDF reports with graphs.
# The script works by:
#   1. Fetching a user's film slugs (unique identifiers for each film).
#   2. Retrieving detailed information for each film via JSON API endpoints.
#   3. Calculating the total time watched and generating summary reports.
#   4. Optionally exporting the data to a CSV file or generating a PDF report
#      with graphs showing the user's watch time and films watched per year.
#
# Usage:
#   python letterboxd_analyzer.py --user <username> [--csv] [--pdf]
#     --user <username>  : The Letterboxd username of the user you want to analyze.
#     --csv             : Export the results to a CSV file.
#     --pdf             : Generate a PDF report with graphs.

HEADERS = {"User-Agent": "Mozilla/5.0"}

# Scrape movie slugs from a Letterboxd user's film list pages
def get_film_slugs(user):
    slugs = []
    page = 1
    while True:
        url = f"https://letterboxd.com/{user}/films/page/{page}/"
        soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, 'html.parser')
        posters = soup.select('ul.poster-list li div[data-details-endpoint]')
        if not posters:
            break
        for div in posters:
            endpoint = div.get('data-details-endpoint')
            if endpoint:
                slug = endpoint.split('/film/')[1]
                slugs.append(slug)
        page += 1
    return slugs


# Fetch runtime and release year from JSON endpoint
def fetch_film_data(slug, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            json_url = f"https://letterboxd.com/film/{slug}"
            data = requests.get(json_url, headers=HEADERS, timeout=10).json()
            return {
                'title': data.get('name', 'Unknown'),
                'minutes': int(data.get('runTime') or 0),
                'year': int(data.get('releaseYear') or 0)
            }
        except Exception as e:
            attempt += 1
            print(f"Error fetching data for {json_url}: {e}, retrying ({attempt}/{retries})...")
            sleep(random.randint(1, 3))  # Random backoff
    return None  # After retries, return None if failed


# Generate CSV export
def export_to_csv(film_data, filename="letterboxd_watch_log.csv"):
    film_data = [f for f in film_data if f and f['minutes'] > 0]
    df = pd.DataFrame(film_data)
    df.to_csv(filename, index=False)
    print(f"📁 CSV exported to {filename}")

# Plot and save charts
def generate_graphs(film_data):
    film_data = [f for f in film_data if f and f['minutes'] > 0]
    df = pd.DataFrame(film_data)
    df = df[df['year'] > 0]
    df = df.dropna(subset=['minutes', 'year'])  # Remove rows with missing data

    # Runtime per year
    time_per_year = df.groupby('year')['minutes'].sum()
    time_per_year.plot(kind='bar', title='Watch Time per Year', figsize=(8, 3), color='skyblue')
    plt.ylabel("Minutes")
    plt.tight_layout()
    plt.savefig("watch_time_per_year.png")
    plt.close()

    # Films per year
    films_per_year = df.groupby('year')['title'].count()
    films_per_year.plot(kind='bar', title='Films Watched per Year', figsize=(8, 3), color='salmon')
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("films_per_year.png")
    plt.close()

# Generate a simple PDF report with embedded charts
def generate_pdf_report(total_minutes):
    total_hours = total_minutes / 60
    doc = SimpleDocTemplate("letterboxd_report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    header_style = ParagraphStyle(
        name='HeaderStyle',
        parent=styles['Heading2'],
        alignment=TA_CENTER,
        spaceAfter=12
    )

    elements = [
        Paragraph("<b>Letterboxd Watch Report</b>", header_style),
        Paragraph("🎬 Your personal film-watching stats summary", styles['Normal']),
        Spacer(1, 12),
        Paragraph("<b>▶️ Total Time Watched:</b>", styles['Heading3']),
        Paragraph(f"{total_minutes} minutes ({total_hours:.2f} hours)", styles['Normal']),
        Spacer(1, 12),
        Paragraph("<b>📊 Watch Time Per Year</b>", styles['Heading3']),
        Image("watch_time_per_year.png", width=6*72, height=2.5*72),
        Spacer(1, 6),
        Paragraph("<b>🎞️ Films Watched Per Year</b>", styles['Heading3']),
        Image("films_per_year.png", width=6*72, height=2.5*72),
        Spacer(1, 6),
    ]

    doc.build(elements)
    print("📄 PDF report saved as letterboxd_report.pdf ✅")

    # Clean up temp graphs
    for img in ["watch_time_per_year.png", "films_per_year.png"]:
        try:
            os.remove(img)
        except Exception as e:
            print(f"Warning: Couldn't delete {img}: {e}")

# Command-line entry point
def main():
    parser = argparse.ArgumentParser(
        description="Letterboxd Watch Time Analyzer. This script scrapes Letterboxd data, calculates total watch time, generates CSV, and creates PDF reports with graphs."
    )
    parser.add_argument("username", help="Your Letterboxd username")
    parser.add_argument("--csv", action="store_true", help="Export results to CSV")
    parser.add_argument("--pdf", action="store_true", help="Generate a PDF report")
    args = parser.parse_args()

    print(f"🔍 Scanning films for user: {args.username}")
    slugs = get_film_slugs(args.username)
    print(f"🎞️  Found {len(slugs)} films")

    # Use multiprocessing to fetch data faster
    with Pool(cpu_count()) as pool:
        film_data = list(filter(None, pool.map(fetch_film_data, slugs)))

    total_minutes = sum(f['minutes'] for f in film_data)
    print(f"⏱️  Total watch time: {total_minutes} minutes ({total_minutes / 60:.2f} hours)")

    if args.csv:
        export_to_csv(film_data)

    if args.pdf:
        generate_graphs(film_data)
        generate_pdf_report(total_minutes)

if __name__ == "__main__":
    main()

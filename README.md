# Web Content Scraper

This repository contains tools for scraping web content and extracting text from web pages. It includes a Bash script for downloading HTML snapshots of web pages (`download_html.sh`) and a Python script for extracting text from these HTML snapshots (`getText.py`). The HTML snapshots are saved in the `html_snapshots` folder, and the extracted text is saved in the `text_output` folder.

## Requirements

- Bash shell (for `download_html.sh`)
- Python 3.x (for `getText.py`)
- BeautifulSoup4 (for parsing HTML in `getText.py`)

## Installation

### Clone the Repository

`cd your-repository-name`

### Python Dependencies

`pip install beautifulsoup4`

## Usage

### Downloading HTML Snapshots

1. Ensure you have a list of URLs you want to download in a file named `url.txt`, with one URL per line.
2. Run the Bash script to download HTML snapshots:
   ```bash
   ./download_html.sh
   ```
   HTML snapshots will be saved in the `html_snapshots` directory.

### Extracting Text from HTML Snapshots

1. After downloading HTML snapshots, run the Python script to extract text:
   ```bash
   python getText.py
   ```
   Extracted text files will be saved in the `text_output` directory.

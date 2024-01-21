# Python Job Scraper

## Description
This script is designed to scrape Python-related job postings from the website `rocketjobs.pl`. It filters job postings based on a user-specified skill that they are not familiar with, allowing them to focus on more relevant job opportunities. The script extracts job titles, company names, required skills, and links to the job postings. Additionally, it identifies if a job offer is new.

## How It Works
The script uses `requests` and `BeautifulSoup` to scrape job postings from `rocketjobs.pl`. The user is prompted to input a skill they are unfamiliar with, which the script uses to filter out irrelevant job posts. The filtered job data is then saved to a CSV file named 'jobs_data.csv'.

## Requirements
- Python 3
- Libraries: `requests`, `bs4` (BeautifulSoup), `pandas`, `time`

## Installation
To install the required libraries, run:

*pip install requests beautifulsoup4 pandas*


## Usage
1. Run the script using Python.
2. When prompted, enter a skill you are unfamiliar with. This skill will be excluded from the job search.
3. The script will scrape job postings and filter them based on the entered skill.
4. The data will be saved to 'jobs_data.csv' and the script will wait for 10 minutes before scraping new data.

## Features
- Scrapes job titles, company names, required skills, and job URLs.
- Filters jobs based on user-inputted unfamiliar skill.
- Saves the scraped data in a CSV file.
- Runs continuously, scraping new data every 10 minutes.

## Author
Martyna Rachańczyk


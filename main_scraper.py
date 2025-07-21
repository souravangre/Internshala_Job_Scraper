import os
import smtplib
import requests
import csv
from bs4 import BeautifulSoup
from email.message import EmailMessage
from dotenv import load_dotenv
import time


load_dotenv()
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Build the URL
def build_internshala_url(keyword, location=None):
    
    keyword = keyword.strip().lower().replace(" ", "-")

    url = f"https://internshala.com/jobs/keywords-{keyword}"

    if location:
        location = location.strip().lower().replace(" ", "-")
        url += f"-in-{location}"

    return url


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U)...",
    "Accept-Language": "en-GB,en;q=0.9"
}



# Scrape the website and save the data in CSV
def scrape_jobs_to_csv(base_url, filename="jobs.csv", pages=5):
    """
    Scrapes job data from a dynamic Internshala URL and writes to a CSV.
    Arguments:
        base_url: Job search URL built from keyword/location
        filename: Output CSV file name
        pages: How many pages to scrape (Internshala paginates results)
    """

    # Define the CSV column headers 
    headline_csv = ["Job_Title", "Company", "Location", "Salary", "Apply_Link"]

    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headline_csv)

        for page_num in range(1, pages + 1):
            url = base_url
            if page_num > 1:
                url += f"/page-{page_num}"

            print(f"Scraping: {url}")
            try:
                response = requests.get(url, headers=HEADERS, timeout=10)
                soup = BeautifulSoup(response.content, "html.parser")

                # All job containers
                job_cards = soup.find_all("div", class_="individual_internship")

                if not job_cards:
                    print("No jobs found on this page.")
                    break

                for job in job_cards:
                    try:
                        title = job.find("div", class_="company").h3.a.text.strip()
                        company = job.find("div", class_="company_and_premium").p.text.strip()
                        location = job.find("div", class_="detail-row-1").p.span.a.text.strip()
                        salary = job.find("div", class_="row-1-item").span.text.strip()
                        link = "https://internshala.com" + job.find("a", class_="job-title-href")["href"].strip()
                        writer.writerow([title, company, location, salary, link])
                    except Exception as e:
                        print("Skipping a job due to missing data:", e)

                time.sleep(1)  # To avoid hitting rate limits

            except Exception as e:
                print("Error scraping page:", url, "Error:", e)

    print(f"✅ Finished scraping: {filename}")



# Send the Email with CSV
def send_email_with_csv(to_email, username, filename):
    """
    Sends an email with a CSV attachment to the given user.
    Arguments:
        to_email: recipient's email
        username: recipient's name for greeting
        filename: CSV file to attach
    """

    msg = EmailMessage()
    msg['Subject'] = 'Your Latest Internshala Job Recommendations'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    msg.set_content(f"""
    Hi {username},

    Based on your preferences, we’ve found some recent job listings for you on Internshala.

    Please find your job list attached in the CSV file.

    Best wishes,
    Your Job Alert Bot 🤖
    """)

    # Attach the CSV
    with open(filename, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=f.name)

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"✅ Email sent to {to_email}")






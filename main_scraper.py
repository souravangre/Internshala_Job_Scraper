import os
import smtplib
import requests
import csv
from bs4 import BeautifulSoup
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def scrape_jobs_to_csv(filename="Internshala_Jobs.csv"):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
        "Accept-Language": "Accept-Language: da, en-gb, en",
        "Accept-Encoding": "Accept-Encoding: gzip, deflate, br",
        "Accept": "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Referer": "https://www.bbc.com/news/entertainment-arts-64759120"
    }

    headline_csv = ["Job_Title", "Company", "Location", "Salary", "Apply_Link"]
    
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headline_csv)

        for page_num in range(1, 5):
            url = "https://internshala.com/jobs/full-stack-development-jobs/"
            if page_num > 1:
                url += f"page-{page_num}/"

            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, "html.parser")

            for main_post in soup.find_all("div", class_="individual_internship"):
                try:
                    title = main_post.find("div", class_="company").h3.a.text.strip()
                    company = main_post.find("div", class_="company_and_premium").p.text.strip()
                    location = main_post.find("div", class_="detail-row-1").p.span.a.text.strip()
                    salary = main_post.find("div", class_="row-1-item").span.text.strip()
                    apply_link = "https://internshala.com" + main_post.find("a", class_="job-title-href")["href"].strip()

                    print(f"{title} | {company} | {location} | {salary}")
                    writer.writerow([title, company, location, salary, apply_link])

                except Exception as e:
                    print("Skipping a job due to missing field:", e)

def send_email_with_csv(filename="Internshala_Jobs.csv"):
    msg = EmailMessage()
    msg['Subject'] = 'Daily Internshala Jobs Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'souravangre@gmail.com'
    msg.set_content(
        "Hi Sourav,\n\nAttached is the latest scraped Full Stack Development job listing from Internshala.\n\nBest,\nYour Python Bot"
    )

    with open(filename, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=f.name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(" Email sent successfully!")

# 4. Run everything
if __name__ == "__main__":
    print(" Scraping jobs...")
    scrape_jobs_to_csv()

    print(" Sending email...")
    send_email_with_csv()

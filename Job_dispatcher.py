from models import db, User, JobPreference
from main_scraper import build_internshala_url, scrape_jobs_to_csv, send_email_with_csv

def run_job_dispatcher():
    users = User.query.all()

    for user in users:
        if not user.preferences:
            print(f"⚠️ No preferences found for {user.email}")
            continue

        keyword = user.preferences.keyword
        location = user.preferences.location

        url = build_internshala_url(keyword, location)
      
        filename = f"{user.username}_jobs.csv"
        
        print(f"🔍 Scraping for {user.email} - {keyword} in {location}")
        scrape_jobs_to_csv(url, filename)

        send_email_with_csv(user.email, user.username, filename)

if __name__ == '__main__':
    run_job_dispatcher()

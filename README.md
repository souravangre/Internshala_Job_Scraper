
 📩 Internshala Job Scraper & Email Notifier

A Python automation project that scrapes the latest **Full Stack Developer jobs** from [Internshala.com](https://internshala.com), stores them in a `.csv` file, and emails the file to you every 24 hours.

Perfect for automating your job hunt or showcasing your automation skills in DevOps, Python, or Web Scraping.

---

 🚀 Features

- 🔎 Scrapes job listings from **multiple pages**
- 📊 Saves job title, company, location, salary, and job link in CSV
- 📬 Automatically emails the CSV every 24 hours
- ✅ Uses `BeautifulSoup`, `requests`, `smtplib`, `dotenv`
- 🔐 Environment variables for secure email handling
- 🖥️ Scheduled via **Windows Task Scheduler**

---

## 🖼️ Sample Output

```csv
Job_Title,Company,Location,Salary,Apply_Link
"Full Stack Developer","ABC Pvt Ltd","Bangalore","₹ 4,00,000","https://internshala.com/job/detail/full-stack-developer-job-in-bangalore-at-abc-pvt-ltd1234567890"

---

## 🛠️ Tech Stack

* Python 3.10+
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](https://docs.python-requests.org/)
* [smtplib](https://docs.python.org/3/library/smtplib.html)
* [dotenv](https://pypi.org/project/python-dotenv/)
* Windows Task Scheduler (for automation)

---

## 📁 Project Structure

```
InternshalaScraper/
│
├── .env                    # Stores email credentials
├── Internshala_Jobs.csv    # Generated CSV file
├── main_scraper.py         # Main scraping and email script
├── scraper.bat             # Batch file to run via Task Scheduler
├── venv/                   # Python virtual environment
├── README.md               # Project documentation
└── .gitignore              # To ignore venv, CSV, and secret files
```

---

## 🔒 .env File Example

Create a `.env` file in the root directory:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_generated_app_password
```

> ⚠️ Use **App Password** if you’re using Gmail with 2FA.
> Generate one from: [Google App Passwords](https://myaccount.google.com/apppasswords)

---

## 🧪 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/internshala-job-scraper.git
cd internshala-job-scraper

# Step 2: Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Add your .env file

# Step 5: Run the scraper manually
python main_scraper.py
```

---

## 📆 Automating with Task Scheduler (Windows)

1. Open **Task Scheduler**
2. Create a new **Basic Task**
3. Select trigger: *Daily at 9 AM* (or any time)
4. Action: `Start a program`
5. Program/script: Point to your `.bat` file (e.g., `send_mail.bat`)

---

## ✅ To Do / Future Scope

* [ ] Add Flask UI for job filtering
* [ ] Add user input for job role/location
* [ ] Notify only for matching jobs
* [ ] Deploy to server or cloud

---

## 🧠 Learning Outcomes

* Real-world **web scraping**
* Automating with **Python**
* Using **SMTP** to send mails
* Working with **.env** for security
* Scheduling with **Task Scheduler**

---

## 📌 License

MIT License © 2025

---

## 🤝 Contribute / Fork / Use

If you're learning Python automation or preparing for DevOps interviews — feel free to fork, use, and modify the project!

> Star ⭐ the repo if you found it useful!




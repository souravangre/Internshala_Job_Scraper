---

## 🚀 Internshala Job Alert App

Automatically fetch the latest internships from [Internshala](https://internshala.com) based on user preferences and send them personalized job lists via email every 48 hours.

> 🔍 Built with Flask • SQLAlchemy • BeautifulSoup • Gmail SMTP • Bootstrap
> 📩 Personalized internship alerts for students and job seekers!

---

### 🧠 Features

* ✅ **User Authentication** (Register/Login system)
* 📝 **User Preference Form** — Add your desired job keyword & location
* 🔄 **Dynamic Scraping** of Internshala job listings based on user input
* 📊 **Saves Jobs to CSV** — Titles, Companies, Locations, Salaries, Links
* 📬 **Automated Email Alerts** with attachment (CSV of relevant jobs)
* 💽 **SQLite Database** using SQLAlchemy ORM
* 🧠 Modular & Production-ready codebase (split into `app.py`, `main_scraper.py`, `job_dispatcher.py`)
* 💡 Ready for CRON-based periodic job updates (every 48 hrs)

---

### 📂 Project Structure

```bash
InternshalaJobAlert/
├── app.py                 # Flask app: UI, Routes, DB logic
├── models.py              # SQLAlchemy Models (User, JobPreference)
├── main_scraper.py        # URL builder, scraper, email sender functions
├── job_dispatcher.py      # Scheduled job runner (loops over users)
├── templates/             # Bootstrap HTML files
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   └── preferences.html
├── static/                # (Optional) CSS or images
├── .env                   # Email credentials
├── requirements.txt
└── README.md
```

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/internshala-job-alert.git
cd internshala-job-alert
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create `.env` File

Create a `.env` file in the root directory:

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

> ✅ *Use Gmail App Password if 2FA is enabled.*

#### 4. Initialize Database

```python
# Inside a Python shell or at the start of app.py
from app import db
db.create_all()
```

#### 5. Run the Flask App

```bash
python app.py
```

Go to: `http://127.0.0.1:5000` and test the full workflow!

#### 6. Run the Job Dispatcher (Manually or via Cron)

```bash
python job_dispatcher.py
```

---

### 🧠 How It Works

1. **User registers** and submits email, job keyword, and location.
2. Data is stored in SQLite via SQLAlchemy.
3. Scraper uses `requests` + `BeautifulSoup` to scrape relevant job listings.
4. CSV file is generated and emailed using `smtplib`.
---

### 💡 Future Enhancements

* ⏰ CRON job setup (for 48hr automated runs)
* 📈 Admin dashboard to view user submissions
* 🔐 OAuth-based login (Google / GitHub)
* 🌐 Deploy on Render / Railway / EC2

---

### 📸 UI Screenshots

Add screenshots here of:

* 🧍 Register/Login pages
* 🧾 Preferences form
* ✅ Flash message
* 📧 Sample Email / CSV

---

### 📬 Sample Email

```
Subject: Daily Internshala Jobs Report

Hi Sourav,

Attached is the latest scraped Full Stack Development job listing from Internshala.

Best,
Your Python Bot
```

---

### 📜 License

MIT License. Free to use and modify.

---

### 👨‍💻 Author

Sourav Angre — [@Souravangre](mailto:hehustleshard@gmail.com)
Passionate about automation, DevOps, and building real-world SaaS ideas.

---



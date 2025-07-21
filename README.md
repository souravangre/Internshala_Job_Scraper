
---

## 🚀 InternAlert - Internshala Job Alert App

A Flask-based web application that allows users to register, set job preferences (e.g., Full Stack Developer), and receive daily job alerts scraped from [Internshala](https://internshala.com). The app uses BeautifulSoup for scraping, SQLite for storage, and includes email alerts with job listings in CSV format.

This project demonstrates automation, web scraping, backend development, and deployment readiness using Docker and Gunicorn.

🌐Live 
```bash
https://intern-alert-app-v1.onrender.com
```
Run with Docker
```bash
docker pull souravangre/intern_alert_app:v1
docker run -d -p 8000:8000 souravangre/intern_alert_app:v1
```
---

### 📌 Features

* ✅ User registration and login system (Flask Auth)
* ✅ Set custom job preferences (e.g., Full Stack, Data Science)
* ✅ Scrape latest jobs from Internshala based on preferences
* ✅ Automatically send daily email alerts with job listings in CSV
* ✅ Web UI for preferences and profile settings
* ✅ Styled with Bootstrap and consistent frontend experience
* ✅ Dockerized setup with Gunicorn for production readiness

---

### 🏗️ Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | Python, Flask           |
| Web Scraping     | BeautifulSoup, Requests |
| Frontend         | HTML, Bootstrap         |
| Database         | SQLite + SQLAlchemy     |            
| Email            | SMTP + `smtplib`        |
| Production       | Gunicorn (via Docker)   |
| Deployment Ready | Docker + Gunicorn       |

---

### 📂 Project Structure

```
internshala-job-alert-app/
│
├── app.py                   # Main Flask app
├── main_scraper.py          # Scraping + emailing logic
├── Job_dispatcher.py        # Job dispatch and scheduling logic
├── templates/               # HTML files (login, register, home, preferences)
├── static/                  # CSS and image assets
├── models.py                # SQLAlchemy models
├── requirements.txt         # Dependencies
├── Dockerfile               # Container setup
├── .gitignore
└── README.md
```

---

### ⚙️ Setup Instructions

#### 1. Clone the repo

```bash
git clone https://github.com/souravangre/Internshala_Job_Scraper.git
cd Internshala_Job_Scraper
```

#### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Add environment variables

Create a `.env` file with:

```env
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
SECRET_KEY=some-secret-key
```

#### 4. Run the app (dev)

```bash
python app.py
```

#### 5. Run with Gunicorn (Linux/macOS)

```bash
gunicorn app:app --workers 4 --worker-class gthread --timeout 30
```

#### 6. Docker Setup

```bash
docker build -t yourimgname .
docker run -d -p 5000:5000 yourimgname
```

---

### 🛠️ Environment Requirements

* Python 3.10+
* Docker (for production)
* SMTP-enabled email account (for alerts)

---

### 📈 Learning Outcomes

* Flask backend development with Blueprints and modular code
* Automating job scraping and email alerts
* Building and scheduling data pipelines
* Containerizing a Flask app using Docker and deploying with Gunicorn
* Writing maintainable, scalable Python code with proper environment handling

---

### 🤝 Contributing

Want to improve the UI, add job filtering, or integrate with a database like PostgreSQL or a scheduler like Celery? PRs are welcome!

---

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

### 🙋‍♂️ Author

**Sourav Angre**
  IT Student | Python & Cloud Enthusiast
[LinkedIn](https://www.linkedin.com/in/sourav-angre) • [GitHub](https://github.com/souravangre)

---



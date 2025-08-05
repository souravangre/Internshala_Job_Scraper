##🚀 InternAlert - Internshala Job Alert App

A Flask-based web application that allows users to register, set job preferences (e.g., Full Stack Developer), and receive daily job alerts scraped from Internshala. The app uses BeautifulSoup for scraping, SQLite for storage, and includes email alerts with job listings in CSV format.

This project demonstrates automation, web scraping, backend development, and deployment readiness using Docker and Gunicorn.

🌐 Live

- Render (v1):``` https://intern-alert-app-v1.onrender.com ```
- AWS EB (Dockerized): [Elastic Beanstalk deployment, on-demand or local only] 
---

📦 Deployment Options

### ▶️ Run with Docker (Local)

```bash
docker pull souravangre/intern_alert_app:v1
docker run -d -p 8000:8000 souravangre/intern_alert_app:v1
```

<details>
<summary>📸 Screenshots</summary>
- ![Architechture](<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/78e9671a-6892-44fb-9be1-d01d3fa0db86" />
)
- ![APP on AWS](<img width="1366" height="698" alt="Screenshot 2025-08-05 142048" src="https://github.com/user-attachments/assets/43cc8077-e803-4ffc-a7a4-4d6e3e23c83d" />
)
- ![EB and Health checks](<img width="1364" height="722" alt="Screenshot 2025-08-05 141947" src="https://github.com/user-attachments/assets/e221cf4c-ae53-49dc-bc55-2097bbe960e5" />
)

</details>

---

### 🚀 Deploy on AWS Elastic Beanstalk (Dockerized Setup)

> **Uses single-container Docker deployment via EB Console**

#### Requirements:

* AWS Account
* Docker image pushed to DockerHub
* `Dockerrun.aws.json` file to define the image & port

#### Steps:

1. Go to AWS Console → Elastic Beanstalk → Create Application
2. Platform: **Docker**
3. Environment: **Web Server**
4. Upload a zip file containing the `Dockerrun.aws.json` file
   (This file specifies the Docker image and port)

**Sample `Dockerrun.aws.json`:**

```json
{
  "AWSEBDockerrunVersion": "1",
  "Image": {
    "Name": "souravangre/intern_alert_app:v1",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": "8000"
    }
  ]
}
```

5. Click “Launch” to deploy. EB will:

   * Pull the image from DockerHub
   * Run it inside an EC2-managed container
   * Provide a public URL to access the app

✅ You **don’t need to push the full app code** — only the `Dockerrun.aws.json` file in a zip is uploaded for Docker image-based deployments.

---

📌 Features
✅ User registration and login system (Flask Auth)
✅ Set custom job preferences (e.g., Full Stack, Data Science)
✅ Scrape latest jobs from Internshala based on preferences
✅ Automatically send daily email alerts with job listings in CSV
✅ Web UI for preferences and profile settings
✅ Styled with Bootstrap and consistent frontend experience
✅ Dockerized setup with Gunicorn for production readiness

---

🏗️ Tech Stack

| Layer        | Technology                         |
| ------------ | ---------------------------------- |
| Backend      | Python, Flask                      |
| Web Scraping | BeautifulSoup, Requests            |
| Frontend     | HTML, Bootstrap                    |
| Database     | SQLite + SQLAlchemy                |
| Email        | SMTP + smtplib                     |
| Production   | Gunicorn (via Docker)              |
| Deployment   | Docker + Gunicorn on AWS EB/Render |

---

📂 Project Structure

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
├── Dockerrun.aws.json       # (Used for AWS EB Docker deployment)
├── .gitignore
└── README.md
```

---

⚙️ Setup Instructions

1. Clone the repo

```bash
git clone https://github.com/souravangre/Internshala_Job_Scraper.git
cd Internshala_Job_Scraper
```

2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Add environment variables
   Create a `.env` file with:

```env
MAIL_USERNAME=your-email@gmail.com  
MAIL_PASSWORD=your-app-password  
SECRET_KEY=some-secret-key  
```

4. Run the app (dev)

```bash
python app.py
```

5. Run with Gunicorn (Linux/macOS)

```bash
gunicorn app:app --workers 4 --worker-class gthread --timeout 30
```

6. Docker Setup

```bash
docker build -t yourimgname .
docker run -d -p 5000:5000 yourimgname
```

---

🛠️ Environment Requirements

* Python 3.10+
* Docker (for production)
* SMTP-enabled email account (for alerts)

---

📈 Learning Outcomes

* Flask backend development with Blueprints and modular code
* Automating job scraping and email alerts
* Building and scheduling data pipelines
* Containerizing a Flask app using Docker and deploying with Gunicorn
* Deploying on cloud using AWS Elastic Beanstalk
* Writing maintainable, scalable Python code with proper environment handling

---

🤝 Contributing

Want to improve the UI, add job filtering, or integrate with a database like PostgreSQL or a scheduler like Celery? PRs are welcome!

---

📄 License

This project is licensed under the MIT License.

---

🙋‍♂️ Author

**Sourav Angre**
IT Student | Python & Cloud Enthusiast
[LinkedIn](www.linkedin.com/in/sourav-angre) • [GitHub](https://github.com/souravangre)

```





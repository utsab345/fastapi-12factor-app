# 🔗 FastAPI URL Shortener

A simple and efficient URL shortener built with ⚡ **FastAPI**, 🐍 **Python**, and 🛢️ **SQLAlchemy**.

This app lets you convert long URLs into short ones and redirect users from those short links back to the original site  similar to services like Bitly or TinyURL.

---

## 🚀 Features

- ✅ Create short URLs
- 🔁 Redirect short URLs to original
- 🧪 Includes test using `pytest`
- 🗃️ Uses SQLite for local storage
- 📦 Run locally or via Docker
- 🔍 API docs with Swagger at `/docs`

---



---

## 🛠️ Running Locally

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/utsab-345/url-shortener.git
cd app
```
### ✅ Step 2: Create a virtual environment and install requirements
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### ✅ Step 3: Start the FastAPI server
```bash
uvicorn app.main:app --reload
🔗 Open your browser and go to: http://127.0.0.1:8000/docs

Use:

POST /api/short to generate short URLs

GET /{short_link} to redirect
```
## 🐳 Running with Docker
### ✅ Step 1: Build the Docker image
```bash
docker build -t app .
```
### ✅ Step 2: Run the Docker container
```bash
docker run -d -p 8000:8000 app
🔗 Visit http://localhost:8000/docs
```
## ⚙️ Configuration
```
The project uses environment variables via .env file.

DATABASE_URL=sqlite:///D:/fastapi_project/app.db
You can change to PostgreSQL, MySQL, etc., by modifying this variable.
```
## ✅ Run Tests
The test case is located in tests/test_main.py.
```bash
pytest
Test ensures the /api/short endpoint works and returns a short URL.
```
## 📄 License
```
MIT License © 2025
```
## ✨ Acknowledgments
```bash
Thanks to:

💡 FastAPI for the amazing framework

⚙️ SQLAlchemy for the ORM support

🧪 Pytest for easy testing

🙌 You — for checking out this project!
```

Made with ❤️ by [Utsab Dahal]
```
Let me know if you'd like the `Dockerfile` or `requirements.txt` generated too!
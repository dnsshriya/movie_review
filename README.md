# 🎬 Movie Review Flask App

A simple, responsive web app built with Flask and SQLite that allows users to add, view, edit, delete, and search movie reviews.

---

## 🌐 Live Demo
Hosted on [Render](https://render.com)
> 🔗 [Visit the App]  https://movie-review-opvr.onrender.com/reviews

---

## 📁 Project Structure
```
movie_review/
├── app.py                  # Main Flask app
├── init_db.py              # Script to initialize SQLite DB
├── requirements.txt        # Project dependencies
├── Procfile                # For Render deployment
├── templates/              # HTML templates
│   ├── add_review.html
│   ├── edit_review.html
│   └── reviews.html
├── static/                 # Static CSS files
│   └── style.css
└── movies.db               # SQLite database file
```

---

## 🔧 Features
- ✅ Add movie reviews
- ✏️ Edit reviews
- 🗑️ Delete reviews
- 🔍 Search by movie title or reviewer
- ⭐ Star rating display
- 📱 Responsive design with custom CSS

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/dnsshriya/movie_review.git
cd movie_review
```

### 2. Create a virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the database
```bash
python init_db.py
```

### 5. Run the app
```bash
python app.py
```
Visit: `http://127.0.0.1:5000`

---

## 🧾 License
This project is for educational/demo purposes only.

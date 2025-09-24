# 🎬 Movie Finder App

A simple Django web app that lets you **search movies** using the TMDb API, view details like cast, rating, genres, and runtime — all in a clean responsive UI.

---

## 🚀 Features
- 🔍 **Search movies** with live suggestions (auto-complete).
- 🎥 **Popular movies** on homepage.
- 📄 **Movie detail page** with overview, runtime, rating, and top cast.
- 📱 **Responsive design** (works on mobile & desktop).
- ⭐ **Pagination** for browsing large movie lists.
- 🎨 Clean UI with animations and hover effects.

---

## 🛠️ Tech Stack
- **Backend:** Django 5+
- **Frontend:** HTML, CSS, JavaScript
- **API:** [The Movie Database (TMDb)](https://developers.themoviedb.org/3)
- **Styling:** Custom CSS (dark mode UI)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
git clone https://github.com/yourusername/MovieFinder.git
cd MovieFinder

2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your TMDb API key
In myapp/views.py, replace YOUR_API_KEY with your actual TMDb API key.

API_KEY = "YOUR_API_KEY"
5️⃣ Run the server
python manage.py runserver
Then open http://127.0.0.1:8000 in your browser 🎉







Ask ChatGPT

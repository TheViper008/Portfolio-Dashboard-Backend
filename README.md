# 🧠 Portfolio Dashboard – Backend (Django REST API)

This is the Django backend for the **Portfolio Analytics Dashboard**. It exposes a REST API that calculates portfolio metrics like total value, gain/loss, sector allocation, and performance trends from a stock holdings dataset.

---

## 🧩 Project Overview

This backend reads an Excel sheet of holdings, processes portfolio analytics using `pandas`, and serves data to the frontend via clean, RESTful API endpoints.

It includes:

- **📊 Holdings breakdown** with gain/loss per stock
- **🧠 Portfolio summary:** total value, gain %, top/worst performers
- **🧩 Allocation data:** sector & market cap split
- **📈 Portfolio performance** vs Nifty50 and Gold
- **✅ CORS-enabled** for frontend integration

---

## ⚙️ Tech Stack Used

- **Django 5**
- **Django REST Framework**
- **pandas** – for data processing
- **openpyxl** – for reading Excel files
- **django-cors-headers** – for CORS support
- **gunicorn** – for production server
- **Render** – for deployment

---

## 🖥️ How to Run Locally

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/portfolio-backend.git
    cd portfolio-backend
    ```
2.  **Create virtual environment and activate:**
    ```bash
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Place your Excel file in the root directory:**
    ```
    Sample Portfolio Dataset for Assignment.xlsx
    ```
5.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
    Access API locally at:
    ```bash
    http://localhost:8000/api/portfolio/summary
    ```

---

## 🌐 Hosted API (Render)

**Base URL:**
[https://portfolio-backend-6il2.onrender.com/api/portfolio](https://portfolio-backend-6il2.onrender.com/api/portfolio)

**📡 Available Endpoints:**

| Method | Endpoint       | Description                             |
| :----- | :------------- | :-------------------------------------- |
| `GET`  | `/holdings`    | Returns list of holdings                |
| `GET`  | `/summary`     | Portfolio totals, gain/loss, best/worst |
| `GET`  | `/allocation`  | Sector + market cap breakdown           |
| `GET`  | `/performance` | Performance trend vs Nifty50 + Gold     |

---

## 🧠 AI Tool Usage

- Used ChatGPT to scaffold serializers, views, and dataframe logic
- Used Copilot for autocompleting repetitive calculations
- All code was reviewed and manually optimized

---

## 🚀 Deployed URL

- **🔗 Backend (Render):** [https://portfolio-backend-6il2.onrender.com](https://portfolio-backend-6il2.onrender.com)

---

## ✅ Status

- Fully deployed on Render
- Clean REST API with all required endpoints
- CORS-enabled for frontend access

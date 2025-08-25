# Personal Finance App

This is a simple personal finance tracking app with a Python FastAPI backend and a minimal vanilla JavaScript frontend (in place of React for simplicity). The backend uses SQLite for storage and provides endpoints for accounts, transactions, summary, and suggestions. The frontend allows basic interactions to create accounts, view summary, and view suggestions.

## Backend

The backend is located in the `backend/` directory.

### Endpoints

- `GET /summary`: Returns total balance and list of accounts.
- `GET /suggestions`: Returns cash flow rotation suggestions.
- `GET /accounts`: List all accounts.
- `POST /accounts`: Create a new account.
- `GET /transactions`: List all transactions.
- `POST /transactions`: Create a new transaction (deposit or withdrawal).

To run the backend locally:

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

## Frontend

The frontend is a simple static site in `frontend/` that communicates with the backend using fetch. To serve it locally, you can use any static file server or run:

```bash
cd frontend
python -m http.server 3000
```

Then open `http://localhost:3000/index.html` in your browser.

For deployment, the `index.html` and `src/main.js` can be served from any static hosting service, and the backend can be deployed on a platform like Render, Deta, or Heroku.

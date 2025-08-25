from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Finance API")

# Allow CORS for frontend on any origin for simplicity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/summary")
def read_summary(db: Session = Depends(get_db)):
    return crud.get_summary(db)

@app.get("/suggestions")
def read_suggestions(db: Session = Depends(get_db)):
    return {"suggestions": crud.get_suggestions(db)}

@app.get("/accounts")
def read_accounts(db: Session = Depends(get_db)):
    return crud.get_accounts(db)

@app.post("/accounts", response_model=schemas.Account)

def create_new_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account)

@app.get("/transactions")

def read_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.post("/transactions", response_model=schemas.Transaction)

def create_new_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

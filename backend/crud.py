from sqlalchemy.orm import Session
from . import models, schemas

# Account CRUD

def get_accounts(db: Session):
    return db.query(models.Account).all()


def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(name=account.name, balance=account.balance)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

# Transaction CRUD

def get_transactions(db: Session):
    return db.query(models.Transaction).all()


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_trans = models.Transaction(
        amount=transaction.amount,
        type=transaction.type,
        date=transaction.date,
        account_id=transaction.account_id,
    )
    # update account balance
    account = db.query(models.Account).filter(models.Account.id == transaction.account_id).first()
    if transaction.type.lower() == "deposit":
        account.balance += transaction.amount
    else:
        account.balance -= transaction.amount
    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans

# Summary endpoint

def get_summary(db: Session):
    accounts = db.query(models.Account).all()
    total_balance = sum(a.balance for a in accounts)
    return {"total_balance": total_balance, "accounts": accounts}

# Suggestions: simple rule-based suggestions for cash flow rotation

def get_suggestions(db: Session):
    # fetch accounts
    accounts = db.query(models.Account).all()
    suggestions = []
    # if any account has negative balance, suggest transfer
    negative_accounts = [a for a in accounts if a.balance < 0]
    positive_accounts = [a for a in accounts if a.balance > 0]
    for neg in negative_accounts:
        for pos in positive_accounts:
            if pos.balance > abs(neg.balance):
                suggestions.append(
                    f"Transfer {abs(neg.balance)} from {pos.name} to {neg.name} to cover negative balance."
                )
                break
    if not suggestions:
        suggestions.append("All accounts are balanced. No transfers needed.")
    return suggestions

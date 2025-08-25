from datetime import date
from typing import Optional
from pydantic import BaseModel

class AccountBase(BaseModel):
    name: str
    balance: Optional[float] = 0

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float
    type: str
    date: date
    account_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    account: Account

    class Config:
        orm_mode = True

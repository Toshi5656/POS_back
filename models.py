from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "m_products_ts"
    prd_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(13), unique=True, index=True)
    name = Column(String(50))
    price = Column(Integer)

class Transaction(Base):
    __tablename__ = "transactions_ts"
    trd_id = Column(Integer, primary_key=True, index=True)
    emp_cd = Column(String(10))
    store_cd = Column(String(5))
    pos_no = Column(String(3))
    total_amt = Column(Integer)

class TransactionDetail(Base):
    __tablename__ = "transaction_details_ts"
    trd_id = Column(Integer, ForeignKey("transactions_ts.trd_id"), primary_key=True)
    dtl_id = Column(Integer, primary_key=True)
    prd_id = Column(Integer, ForeignKey("m_products_ts.prd_id"))
    prd_code = Column(String(13))
    prd_name = Column(String(50))
    prd_price = Column(Integer)
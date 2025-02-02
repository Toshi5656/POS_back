from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Product, Transaction, TransactionDetail
from schemas import ProductResponse, PurchaseRequest, PurchaseResponse
import crud

# FastAPIアプリの作成
app = FastAPI()

# データベース接続用の依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 商品検索API
@app.get("/product/{code}", response_model=ProductResponse)
def get_product(code: str, db: Session = Depends(get_db)):
    return crud.get_product(db, code)

# 購入処理API
@app.post("/purchase", response_model=PurchaseResponse)
def purchase(request: PurchaseRequest, db: Session = Depends(get_db)):
    return crud.purchase(db, request)

# データベース初期化
Base.metadata.create_all(bind=engine)

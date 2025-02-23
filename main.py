from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Product, Transactions, TransactionDetails
from schemas import ProductResponse, PurchaseRequest, PurchaseResponse
import crud
from fastapi.middleware.cors import CORSMiddleware

# FastAPIアプリの作成
app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://192.168.11.45:3000",  # フロントエンドのIPアドレス
        "http://localhost:3000"       # ローカルでのデバッグ用
    ],
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
)

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
    try:
        print(f"受信データ: {request.dict()}")  # デバッグ用ログ
        return crud.purchase(db, request)
    except Exception as e:
        print(f"購入処理エラー: {str(e)}")  # エラーログを出力
        # `total_amt` を 0 にしてレスポンスの形式を維持する
        return PurchaseResponse(success=False, total_amt=0)

# データベース初期化
Base.metadata.create_all(bind=engine)

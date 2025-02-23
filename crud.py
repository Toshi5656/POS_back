from sqlalchemy.orm import Session
from models import Product, Transactions, TransactionDetails
from schemas import PurchaseRequest, PurchaseResponse
from fastapi import HTTPException

def get_product(db: Session, code: str):
    product = db.query(Product).filter(Product.code == code).first()
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return product

def purchase(db: Session, request: PurchaseRequest):
    try:
        transaction = Transactions(
            emp_cd=request.emp_cd, 
            store_cd=request.store_cd, 
            pos_no=request.pos_no, 
            total_amt=0
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)

        total_amt = 0
        for item in request.items:
            product = db.query(Product).filter(Product.prd_id == item.prd_id).first()
            if not product:
                raise HTTPException(status_code=404, detail=f"商品 {item.prd_id} が見つかりません")

            detail = TransactionDetails(
                trd_id=transaction.trd_id, 
                prd_id=item.prd_id, 
                prd_code=product.code, 
                prd_name=product.name, 
                prd_price=product.price,
                quantity=item.quantity  # ← 数量を追加
            )
            db.add(detail)
            total_amt += product.price * item.quantity
        
        transaction.total_amt = total_amt
        db.commit()
        
        return {"success": True, "total_amt": total_amt}
    
    except Exception as e:
        print(f"DB処理エラー: {str(e)}")  # ログに出力
        db.rollback()  # 失敗した場合はロールバック
        raise HTTPException(status_code=500, detail="購入処理に失敗しました")

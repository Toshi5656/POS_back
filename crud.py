from sqlalchemy.orm import Session
from models import Product, Transaction, TransactionDetail
from schemas import PurchaseRequest, PurchaseResponse
from fastapi import HTTPException

def get_product(db: Session, code: str):
    product = db.query(Product).filter(Product.code == code).first()
    if not product:
        raise HTTPException(status_code=404, detail="商品が見つかりません")
    return product

def purchase(db: Session, request: PurchaseRequest):
    transaction = Transaction(emp_cd=request.emp_cd, store_cd=request.store_cd, pos_no=request.pos_no, total_amt=0)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    
    total_amt = 0
    for item in request.items:
        product = db.query(Product).filter(Product.prd_id == item.prd_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"商品 {item.prd_id} が見つかりません")
        detail = TransactionDetail(trd_id=transaction.trd_id, prd_id=item.prd_id, prd_code=product.code, prd_name=product.name, prd_price=product.price)
        db.add(detail)
        total_amt += product.price * item.quantity
    
    transaction.total_amt = total_amt
    db.commit()
    
    return {"success": True, "total_amt": total_amt}

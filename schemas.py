from pydantic import BaseModel
from typing import List

class ProductResponse(BaseModel):
    prd_id: int
    code: str
    name: str
    price: int
    class Config:
        from_attributes = True  # 修正: orm_mode → from_attributes

class PurchaseItem(BaseModel):
    prd_id: int
    quantity: int

class PurchaseRequest(BaseModel):
    emp_cd: str
    store_cd: str
    pos_no: str
    items: List[PurchaseItem]

class PurchaseResponse(BaseModel):
    success: bool
    total_amt: int

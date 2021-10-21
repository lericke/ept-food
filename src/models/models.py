from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None 
    name: str
    phone: str
    my_products: List[Product]
    my_sells: List[Demand]
    my_demands: List[Demand]

class Product(BaseModel):
    id: Optional[str] = None
    user: User
    name: str
    detail: str
    price: float
    available: bool = False

class Demand(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delievery: bool = True
    delievery_address: str
    comments: str = "Sem observações"

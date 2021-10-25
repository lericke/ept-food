
from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None 
    name: str
    telefone: str

class Produto(BaseModel):
    id: Optional[str] = None
    name: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    quantidade: int
    entrega: bool = True
    endereco_entrega: str
    observacoes: str = "Sem observações"
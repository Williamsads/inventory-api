from sqlalchemy.orm import Session
from repository import movimentacao_repo, produto_repo
from models import Estoque
from fastapi import HTTPException

def registrar_movimentacao(db: Session, estoque_id: int, tipo: str, quantidade: int):
    estoque = db.query(Estoque).filter(Estoque.id == estoque_id).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    
    if tipo == "saida" and estoque.quantidade < quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")
    
    # Atualiza quantidade do estoque
    if tipo == "entrada":
        estoque.quantidade += quantidade
    else:  # saida
        estoque.quantidade -= quantidade
    
    db.commit()
    db.refresh(estoque)
    
    return movimentacao_repo.registrar_movimentacao(db, estoque_id, tipo, quantidade)

def listar_movimentacoes(db: Session, estoque_id: int):
    return movimentacao_repo.listar_movimentacoes(db, estoque_id)

from sqlalchemy.orm import Session
from models import Movimentacao, Produto

def registrar_movimentacao(db: Session, estoque_id: int, tipo: str, quantidade: int):
    # Verifica se vai gerar estoque negativo
    if tipo == "saida":
        saldo_atual = sum([m.quantidade if m.tipo == "entrada" else -m.quantidade for m in db.query(Movimentacao).filter(Movimentacao.estoque_id == estoque_id).all()])
        if saldo_atual - quantidade < 0:
            raise ValueError("Estoque insuficiente")

    mov = Movimentacao(
        estoque_id=estoque_id,
        tipo=tipo,
        quantidade=quantidade
    )
    db.add(mov)
    db.commit()
    db.refresh(mov)
    return mov

def listar_movimentacoes(db: Session, estoque_id: int):
    return db.query(Movimentacao).filter(Movimentacao.estoque_id == estoque_id).all()

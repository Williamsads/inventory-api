from sqlalchemy.orm import Session
from models import Produto, Categoria, Movimentacao

def get_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def get_produtos(db: Session):
    return db.query(Produto).all()

def create_produto(db: Session, nome: str, sku: str, categoria_id: int):
    produto = Produto(nome=nome, sku=sku, categoria_id=categoria_id)
    db.add(produto)
    db.commit()
    db.refresh(produto)

    # Cria registro inicial de estoque com quantidade zero
    estoque = Movimentacao(
        estoque_id=produto.id,
        tipo="entrada",
        quantidade=0
    )
    db.add(estoque)
    db.commit()
    db.refresh(estoque)

    return produto

def update_produto(db: Session, produto: Produto, nome: str, sku: str, categoria_id: int):
    produto.nome = nome
    produto.sku = sku
    produto.categoria_id = categoria_id
    db.commit()
    db.refresh(produto)
    return produto

def delete_produto(db: Session, produto: Produto):
    # Remove todos os registros de movimentação antes de deletar o produto
    db.query(Movimentacao).filter(Movimentacao.estoque_id == produto.id).delete()
    db.delete(produto)
    db.commit()
    return {"ok": True}

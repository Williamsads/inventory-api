from sqlalchemy.orm import Session
from repository import produto_repo, categoria_repo
from models import Produto, Estoque
from fastapi import HTTPException

def criar_produto(db: Session, nome: str, sku: str, categoria_id: int):
    # Verifica SKU único
    if db.query(Produto).filter(Produto.sku == sku).first():
        raise HTTPException(status_code=400, detail="SKU já existe")
    # Verifica categoria
    if not categoria_repo.get_categoria(db, categoria_id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    produto = produto_repo.create_produto(db, nome, sku, categoria_id)
    # Cria estoque automaticamente
    estoque = Estoque(produto_id=produto.id, quantidade=0)
    db.add(estoque)
    db.commit()
    db.refresh(estoque)
    return produto

def listar_produtos(db: Session):
    return produto_repo.get_produtos(db)

def buscar_produto(db: Session, produto_id: int):
    produto = produto_repo.get_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

def atualizar_produto(db: Session, produto_id: int, nome: str, sku: str, categoria_id: int):
    produto = buscar_produto(db, produto_id)
    return produto_repo.update_produto(db, produto, nome, sku, categoria_id)

def excluir_produto(db: Session, produto_id: int):
    produto = buscar_produto(db, produto_id)
    produto_repo.delete_produto(db, produto)
    return {"detail": "Produto excluído"}

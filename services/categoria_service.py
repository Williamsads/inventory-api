from sqlalchemy.orm import Session
from repository import categoria_repo
from models import Categoria, Produto
from fastapi import HTTPException

def criar_categoria(db: Session, nome: str):
    existing = db.query(Categoria).filter(Categoria.nome == nome).first()
    if existing:
        raise HTTPException(status_code=400, detail="Categoria já existe")
    return categoria_repo.create_categoria(db, nome)

def listar_categorias(db: Session):
    return categoria_repo.get_categorias(db)

def buscar_categoria(db: Session, categoria_id: int):
    categoria = categoria_repo.get_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

def atualizar_categoria(db: Session, categoria_id: int, nome: str):
    categoria = buscar_categoria(db, categoria_id)
    return categoria_repo.update_categoria(db, categoria, nome)

def excluir_categoria(db: Session, categoria_id: int):
    categoria = buscar_categoria(db, categoria_id)
    if db.query(Produto).filter(Produto.categoria_id == categoria_id).first():
        raise HTTPException(status_code=400, detail="Categoria possui produtos vinculados")
    return categoria_repo.delete_categoria(db, categoria)

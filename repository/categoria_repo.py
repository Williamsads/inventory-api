from sqlalchemy.orm import Session
from models import Categoria, Produto

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_categorias(db: Session):
    return db.query(Categoria).all()

def create_categoria(db: Session, nome: str):
    categoria = Categoria(nome=nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def update_categoria(db: Session, categoria: Categoria, nome: str):
    categoria.nome = nome
    db.commit()
    db.refresh(categoria)
    return categoria

def delete_categoria(db: Session, categoria: Categoria):
    db.delete(categoria)
    db.commit()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import categoria_service
import schemas

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=schemas.Categoria)
def criar_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.criar_categoria(db, categoria.nome)

@router.get("/", response_model=list[schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.listar_categorias(db)

@router.get("/{categoria_id}", response_model=schemas.Categoria)
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return categoria_service.buscar_categoria(db, categoria_id)

@router.put("/{categoria_id}", response_model=schemas.Categoria)
def atualizar_categoria(categoria_id: int, categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.atualizar_categoria(db, categoria_id, categoria.nome)

@router.delete("/{categoria_id}")
def excluir_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return categoria_service.excluir_categoria(db, categoria_id)

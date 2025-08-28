from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import produto_service
import schemas

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=schemas.Produto)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.criar_produto(db, produto.nome, produto.sku, produto.categoria_id)

@router.get("/", response_model=list[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)

@router.get("/{produto_id}", response_model=schemas.Produto)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    return produto_service.buscar_produto(db, produto_id)

@router.put("/{produto_id}", response_model=schemas.Produto)
def atualizar_produto(produto_id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return produto_service.atualizar_produto(db, produto_id, produto.nome, produto.sku, produto.categoria_id)

@router.delete("/{produto_id}")
def excluir_produto(produto_id: int, db: Session = Depends(get_db)):
    return produto_service.excluir_produto(db, produto_id)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services import movimentacao_service
import schemas

router = APIRouter(prefix="/movimentacoes", tags=["Movimentações"])

@router.post("/", response_model=schemas.Movimentacao)
def movimentar_estoque(mov: schemas.MovimentacaoBase, db: Session = Depends(get_db)):
    return movimentacao_service.registrar_movimentacao(db, mov.estoque_id, mov.tipo, mov.quantidade)

@router.get("/{estoque_id}", response_model=list[schemas.Movimentacao])
def historico_movimentacoes(estoque_id: int, db: Session = Depends(get_db)):
    return movimentacao_service.listar_movimentacoes(db, estoque_id)


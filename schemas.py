from pydantic import BaseModel

# Categoria
class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    class Config:
        from_attributes = True

# Produto
class ProdutoBase(BaseModel):
    nome: str
    sku: str
    categoria_id: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
    class Config:
        from_attributes = True

# Estoque
class Estoque(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    class Config:
        from_attributes = True

# Movimentacao
class MovimentacaoBase(BaseModel):
    estoque_id: int
    tipo: str
    quantidade: int

class Movimentacao(MovimentacaoBase):
    id: int
    class Config:
        from_attributes = True

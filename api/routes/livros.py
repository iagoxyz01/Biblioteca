from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.livro import LeitorCreate , LeitorOut
from services.biblioteca_service import(
    criar_livro,
    lista_livros,
    buscar_livro,
    alterar_preco_livro,
)

router= APIRouter (prefix="/livros", tags=["Livros"])

class AlterarPrecoInput(BaseModel):
    preco: float

@router.post("", response_model=livroOut)
def post_livro(data:LivroCreate):
    return criar_livro(data)

@
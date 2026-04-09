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
-
@router.get("", response-_model= list[LivroOut])
def get_livros():-
    return listar_livros-()
-
@router.get("/{codigo}",- response_model= LivroOut)
def get_livro(codigo:int-):
    livro= buscar_livro(-codigo)
    if not livro:-
        raise HTTPExcept-ion](status_code=404, detail="Livro não encontrado.")
    return livro-

@router.put ("/{codigo}/ preco", response_model=LivroOut)
def put_preco_livro(codigo:int, data: AlterarPrecoInput):
    livro= alterar_preco_livro(codigo,data.preco)
    if not livro:
        raise HTTPException (status_code=404, detail="Livro não encontrado.")
    return livro

@router.get("/{codigo} preco-final")
def get_preco_final(codigo:int):
    livro= buscar_livro(codigo)
    if not livro:
        raise HTTPException (status_code = 404, detail="Livro não encontrado.")
    return {"codigo": livro.codigo, "titulo": livro.titulo, "preco_final": livro.preco_final()}
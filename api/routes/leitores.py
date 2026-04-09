from fastapi import APIRouter
from schemas.Leitor import LeitorCreate, LeitorOut
from services.biblioteca_service import criar_leitor, Listar_leitores

router= APIRouter(prefix= "/leitores" , tags= ["Leitores"])

@router.post("", response_model= LeitorOut)
def post_leitor(data: LeitorCreate):
    return criar_leitor(data)

@router.get("", response_model=list[LeitorOut])
def get_leitores():
    return Listar_leitores()
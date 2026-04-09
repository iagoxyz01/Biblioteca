from fastapi import FastAPI
from api.routes.leitores import router as leitores_router
from api.router.livros import router as livros_router

app = FastAPI (title= "biblioteca API")
@app.get("/")
def home():
    return {"msg": "Biblioteca API funcionando"}

app.include_router(leitores_router)
app.include_router(livros_router)
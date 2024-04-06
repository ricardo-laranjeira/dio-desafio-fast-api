from fastapi import APIRouter
from _models.controllers import router as atleta
from _models.controllers import router as categoria
from _models.controllers import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamentos', tags=['centros_treinamento'])

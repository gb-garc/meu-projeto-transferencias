from fastapi import FastAPI
from routes.transfer_routes import router as transfer_router

app = FastAPI(
    title="API de Transferências",
    description="Gerencia transferências de funcionários",
    version="1.0.0"
)

# Inclui as rotas do módulo transfer_routes
app.include_router(transfer_router)

@app.get("/")
def root():
    return {"mensagem": "API de transferências em funcionamento!"}

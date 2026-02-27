from fastapi import FastAPI

app = FastAPI(title="Hub Inteligente de Recursos Educacionais API")

@app.get("/health")
def health_check():
    # Rota de health check exigida nos requisitos bônus do desafio!
    return {"status": "ok", "message": "API rodando perfeitamente"}

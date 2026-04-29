from fastapi import FastAPI, Request
from app.routes.rag_test import router as rag_test_router

app = FastAPI(
    title="Totem Inteligente Flex Media - RAG",
    description="API demonstrativa para RAG com busca vetorial.",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "ok", "app": "agentai-totem-rag-public"}

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    public_paths = ["/login", "/health", "/docs", "/openapi.json", "/static", "/rag-test", "/api/rag-test"]
    if any(request.url.path.startswith(path) for path in public_paths):
        return await call_next(request)
    return await call_next(request)

app.include_router(rag_test_router)

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy import create_engine, text

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
load_dotenv(ROOT_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não definida.")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY não definida.")

client = OpenAI(api_key=OPENAI_API_KEY)
engine = create_engine(DATABASE_URL)

def gerar_embedding(conteudo: str):
    response = client.embeddings.create(model="text-embedding-3-small", input=conteudo)
    return response.data[0].embedding

def montar_documentos_company_contexts(data: dict):
    documentos = []
    for company_id, empresa in data.items():
        documentos.append({
            "company_id": company_id,
            "titulo": f"{company_id} - descrição",
            "conteudo": f"{empresa.get('name', '')}. {empresa.get('description', '')}",
            "fonte": "company_contexts.json",
        })

        location = empresa.get("location", {})
        documentos.append({
            "company_id": company_id,
            "titulo": f"{company_id} - localização",
            "conteudo": f"Endereço: {location.get('address', '')}. Referência: {location.get('reference', '')}.",
            "fonte": "company_contexts.json",
        })

        hours = empresa.get("hours", {})
        documentos.append({
            "company_id": company_id,
            "titulo": f"{company_id} - horários",
            "conteudo": (
                f"Segunda a sábado: {hours.get('monday_to_saturday', '')}. "
                f"Domingo: {hours.get('sunday', '')}. "
                f"Feriados: {hours.get('holidays', '')}."
            ),
            "fonte": "company_contexts.json",
        })

        contacts = empresa.get("contacts", {})
        documentos.append({
            "company_id": company_id,
            "titulo": f"{company_id} - contatos",
            "conteudo": f"Telefone: {contacts.get('phone', '')}. Email: {contacts.get('email', '')}. Site: {contacts.get('site', '')}.",
            "fonte": "company_contexts.json",
        })

        for service in empresa.get("services", []):
            documentos.append({
                "company_id": company_id,
                "titulo": f"{company_id} - serviço - {service.get('name', '')}",
                "conteudo": (
                    f"Serviço: {service.get('name', '')}. "
                    f"Categoria: {service.get('category', '')}. "
                    f"Zona: {service.get('zone', '')}. "
                    f"Referência: {service.get('reference', '')}. "
                    f"Tags: {', '.join(service.get('tags', []))}."
                ),
                "fonte": "company_contexts.json",
            })

        for item in empresa.get("faq", []):
            documentos.append({
                "company_id": company_id,
                "titulo": f"{company_id} - FAQ - {item.get('question', '')}",
                "conteudo": f"Pergunta: {item.get('question', '')}. Resposta: {item.get('answer', '')}",
                "fonte": "company_contexts.json",
            })

        for policy in empresa.get("policies", []):
            documentos.append({
                "company_id": company_id,
                "titulo": f"{company_id} - política",
                "conteudo": policy,
                "fonte": "company_contexts.json",
            })
    return documentos

def montar_documentos_zoo_faq(data):
    documentos = []
    if isinstance(data, dict):
        items = data.get("faq", [])
        company_id = data.get("company_id", "FLX-001")
    else:
        items = data
        company_id = "FLX-001"

    for item in items:
        pergunta = item.get("question") or item.get("pergunta")
        resposta = item.get("answer") or item.get("resposta")
        if pergunta and resposta:
            documentos.append({
                "company_id": company_id,
                "titulo": f"{company_id} - FAQ - {pergunta}",
                "conteudo": f"Pergunta: {pergunta}. Resposta: {resposta}",
                "fonte": "zoo_faq.json",
            })
    return documentos

def carregar_documentos():
    documentos = []
    company_contexts_path = ROOT_DIR / "data" / "company_contexts.json"
    zoo_faq_path = ROOT_DIR / "data" / "zoo_faq.json"

    if company_contexts_path.exists():
        documentos.extend(montar_documentos_company_contexts(json.loads(company_contexts_path.read_text(encoding="utf-8"))))
    if zoo_faq_path.exists():
        documentos.extend(montar_documentos_zoo_faq(json.loads(zoo_faq_path.read_text(encoding="utf-8"))))
    return documentos

def main():
    documentos = carregar_documentos()
    if not documentos:
        print("Nenhum documento encontrado para vetorizar.")
        return

    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS base_conhecimento (
                id SERIAL PRIMARY KEY,
                company_id TEXT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                fonte TEXT,
                embedding vector(1536)
            )
        """))
        conn.execute(text("DELETE FROM base_conhecimento"))

        total = 0
        for doc in documentos:
            embedding = gerar_embedding(doc["conteudo"])
            conn.execute(
                text("""
                    INSERT INTO base_conhecimento
                    (company_id, titulo, conteudo, fonte, embedding)
                    VALUES (:company_id, :titulo, :conteudo, :fonte, :embedding)
                """),
                {
                    "company_id": doc["company_id"],
                    "titulo": doc["titulo"],
                    "conteudo": doc["conteudo"],
                    "fonte": doc["fonte"],
                    "embedding": str(embedding),
                },
            )
            total += 1

    print(f"Base vetorizada com sucesso. {total} documentos inseridos.")

if __name__ == "__main__":
    main()

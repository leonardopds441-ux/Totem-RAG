CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS base_conhecimento (
    id SERIAL PRIMARY KEY,
    company_id TEXT,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    fonte TEXT,
    embedding vector(1536)
);

# Totem-RAG
O repositório original é privado por conter credenciais e infraestrutura da AWS. Por isso foi criada uma versão pública sanitizada, mantendo a arquitetura, código e funcionamento da solução.

## Arquitetura

```text
Totem / Interface Web → API FastAPI na EC2 → RDS PostgreSQL + pgvector → OpenAI → Resposta
```

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- OpenAI API
- HTML/CSS/JavaScript
- AWS EC2
- AWS RDS

## Estrutura

```text
app/
  main.py
  routes/rag_test.py
DB/
  session.py
  create_vector_table.sql
data/
  company_contexts.json
  zoo_faq.json
scripts/
  seed_base_conhecimento.py
templates/
  rag_test.html
.env.example
requirements.txt
README.md
```

## Instalação

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Criar tabela vetorial

Execute o arquivo:

```text
DB/create_vector_table.sql
```

## Popular base vetorial

```bash
python scripts/seed_base_conhecimento.py
```

## Rodar API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Testar

```text
http://localhost:8000/rag-test/FLX-001
```

Perguntas sugeridas:

- Como posso entrar em contato com o zoológico?
- Onde posso comer algo no local?
- Onde ficam os pinguins?
- Qual o horário de funcionamento?
- Onde ficam os banheiros?
- Se eu estiver com fome, para onde devo ir?
- O que tem perto da saída do zoológico?
- Existe algum lugar para comprar lembranças?
- Onde posso encontrar refeições rápidas?
- O zoológico oferece estrutura básica para visitantes?

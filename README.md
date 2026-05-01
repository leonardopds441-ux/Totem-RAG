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

Pergunta 1

Qual é o endereço completo do zoológico?

Resposta:
O endereço completo do zoológico é Av. Miguel Estéfano, 4241 - Água Funda - São Paulo/SP.

Pergunta 2

Qual é o horário de funcionamento aos domingos?

Resposta:
Aos domingos, o zoológico funciona das 12:00 às 18:00.

Pergunta 3

Que lojas e estabelecimentos comerciais existem dentro do zoológico?

Resposta:
Dentro do zoológico existem Lembrancinhas & Cia, Loja do Pinguim e Praça de Alimentação.

Pergunta 4

Qual é o telefone do zoológico?

Resposta:
O telefone de contato do zoológico é (11) 5073-0811.

Pergunta 5

Qual é o email de contato do zoológico?

Resposta:
O email de atendimento do zoológico é atendimento@zoologico.com.br
.

Pergunta 6

Qual é o site oficial do zoológico?

Resposta:
O site oficial do zoológico é https://zoologico.com.br
.

Pergunta 7

Qual é o horário de funcionamento de segunda a sábado?

Resposta:
De segunda a sábado, o zoológico funciona das 10:00 às 17:00.

Pergunta 8

Onde fica a Praça de Alimentação?

Resposta:
A Praça de Alimentação fica na área central do percurso, próxima aos banheiros principais.

Pergunta 9

Onde fica a Loja do Pinguim?

Resposta:
A Loja do Pinguim fica na área temática dos pinguins, próxima à atração dos pinguins.

Pergunta 10

Quais serviços estão disponíveis no zoológico?

Resposta:
Os serviços disponíveis incluem banheiros principais, fraldário e ponto de informações.

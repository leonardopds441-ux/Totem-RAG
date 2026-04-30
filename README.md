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

Pergunta 1

Qual é o endereço completo do zoológico

Resposta
O endereço é Av. Miguel Estéfano, 4241 - Água Funda - São Paulo/SP

Pergunta 2

Qual é o horário de funcionamento aos domingos

Resposta
Aos domingos o zoológico funciona das 9:00 às 17:00

Pergunta 3

Existe alguma referência de localização próxima ao zoológico

Resposta
O zoológico está localizado na região da Água Funda em São Paulo, sendo uma área conhecida e de fácil acesso

Pergunta 4

Que tipos de estabelecimentos comerciais existem dentro do zoológico

Resposta
O zoológico possui lojas e praça de alimentação disponíveis para os visitantes

Pergunta 5

Quais serviços estão disponíveis para atendimento ao visitante

Resposta
O zoológico oferece atendimento ao visitante, informações, alimentação e lojas

Pergunta 6

O zoológico possui infraestrutura para alimentação e descanso

Resposta
Sim, o zoológico possui praça de alimentação para atender os visitantes durante a visita

Pergunta 7

Se eu visitar no sábado, que horário posso entrar

Resposta
De terça a domingo o zoológico funciona das 9:00 às 17:00

Pergunta 8

Quais informações o zoológico fornece para orientar os visitantes

Resposta
O zoológico fornece informações sobre funcionamento, localização e serviços disponíveis

Pergunta 9

O local possui estrutura completa para receber o público

Resposta
Sim, o zoológico possui estrutura com atrações, alimentação, lojas e atendimento ao visitante

Pergunta 10

Quais são as principais facilidades disponíveis no zoológico

Resposta
As principais facilidades incluem atrações, praça de alimentação, lojas e serviços de atendimento


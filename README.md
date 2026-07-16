# Full_Customer_Support_Chat_Bot_GenAI_AgentAI

# Full Customer Support Chat Bot - GenAI AgentAI

> Enterprise Multi-Agent AI Customer Support Platform powered by RAG, LangGraph, FastAPI, ChromaDB, Pinecone, and OpenAI.

![Version](https://img.shields.io/badge/version-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.12-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![LangGraph](https://img.shields.io/badge/LangGraph-AgenticAI-orange)
![RAG](https://img.shields.io/badge/RAG-Enabled-purple)

---

## Table of Contents

1. Project Overview
2. Business Problem
3. Business Goals
4. Key Features
5. Technology Stack
6. System Architecture
7. Complete Workflow
8. RAG Pipeline
9. Multi-Agent Architecture
10. LangGraph Workflow
11. Memory Workflow
12. Embedding Configuration
13. Chunk Configuration
14. Vector Database Configuration
15. LLM Configuration
16. Project Structure
17. Installation
18. Environment Variables
19. Running the Application
20. Running Tests
21. Local URLs
22. Performance Metrics
23. Future Roadmap
24. AWS Migration Plan
25. Version Information

---

## Project Overview

Full Customer Support Chat Bot - GenAI AgentAI is an Enterprise Multi-Agent AI Customer Support Platform designed to automate customer support operations using:

- Retrieval-Augmented Generation (RAG)
- Multi-Agent Architecture
- LangGraph Orchestration
- Conversation Memory
- FastAPI Backend
- ChromaDB / Pinecone
- OpenAI GPT Models

The system is capable of:

- Understanding customer intent.
- Maintaining conversation context.
- Retrieving enterprise knowledge.
- Generating contextual responses.
- Escalating sensitive issues.
- Supporting multi-turn conversations.

---

## Business Problem

Traditional customer support systems suffer from:

- Poor contextual understanding
- Rule-based limitations
- High support costs
- Inability to scale
- Lack of conversational memory
- Poor customer experience

Existing chatbots often:

- Break on rephrased questions.
- Cannot handle multi-turn conversations.
- Fail to understand emotions.
- Cannot retrieve enterprise knowledge.

---

## Business Goals

This project aims to:

- Reduce support costs.
- Improve customer satisfaction.
- Enable AI-powered support.
- Support multi-turn conversations.
- Provide enterprise scalability.
- Reduce average response time.
- Enable human escalation workflows.

---

## Key Features

### RAG

- Document ingestion
- Semantic search
- Context grounding
- Hallucination reduction

### Multi-Agent

- Intent Agent
- Sentiment Agent
- Conversation Agent
- Retrieval Agent
- Response Agent
- Escalation Agent

### Enterprise

- FastAPI
- Logging
- Exception Handling
- Middleware
- Dependency Injection
- Application Factory

### Future

- Redis Memory
- MCP
- AWS Bedrock
- CloudWatch
- Docker
- Kubernetes

---

## Technology Stack

| Category | Technology |
|---------|------------|
| Backend | FastAPI |
| LLM | OpenAI GPT-4o |
| Local LLM | Ollama |
| RAG | LangChain Concepts |
| Agents | LangGraph |
| Embeddings | Sentence Transformers |
| Vector DB | ChromaDB |
| Production Vector DB | Pinecone |
| Memory | Conversation Memory |
| Logging | Loguru |
| Database | SQLite |
| Future DB | PostgreSQL |
| Cloud | AWS |
| Deployment | Docker |
| Monitoring | CloudWatch (Future) |

---

## System Architecture

```text
Customer
    ↓
FastAPI
    ↓
LangGraph
    ↓
Intent Agent
    ↓
Sentiment Agent
    ↓
Conversation Agent
    ↓
Retrieval Agent
    ↓
Vector DB
    ↓
Prompt Builder
    ↓
GPT-4o
    ↓
Response Agent
    ↓
Escalation Agent
    ↓
Customer
```

---

## Complete Workflow

```text
Customer Query
      ↓
FastAPI Endpoint
      ↓
LangGraph
      ↓
Intent Classification
      ↓
Sentiment Detection
      ↓
Conversation Memory
      ↓
RAG Retrieval
      ↓
Prompt Construction
      ↓
GPT Generation
      ↓
Response Validation
      ↓
Escalation Check
      ↓
Customer Response
```

---

## RAG Pipeline

```text
PDF/DOCX/TXT/CSV/JSON
           ↓
Document Loader
           ↓
Cleaner
           ↓
Metadata Extraction
           ↓
Chunking
           ↓
Embeddings
           ↓
ChromaDB
           ↓
Retriever
           ↓
Prompt Builder
           ↓
LLM
```

---

## Multi-Agent Architecture

| Agent | Responsibility |
|------|---------------|
| Intent Agent | Classifies customer intent |
| Sentiment Agent | Detects emotions |
| Conversation Agent | Maintains context |
| Retrieval Agent | Performs RAG retrieval |
| Response Agent | Generates final response |
| Escalation Agent | Routes to human support |

---

## LangGraph Workflow

```text
START
   ↓
Intent
   ↓
Sentiment
   ↓
Conversation
   ↓
Retrieval
   ↓
Response
   ↓
Escalation
   ↓
END
```

---

## Memory Workflow

```text
Customer
    ↓
Conversation Agent
    ↓
Memory Manager
    ↓
Conversation Memory
    ↓
Session Memory
    ↓
Redis Memory (Future)
```

---

## Embedding Configuration

| Parameter | Value |
|----------|------|
| Provider | Sentence Transformers |
| Model | all-MiniLM-L6-v2 |
| Dimensions | 384 |
| Batch Size | 64 |
| Normalize Embeddings | True |
| Device | CPU |
| Future Models | OpenAI, Bedrock Titan |

---

## Chunk Configuration

| Parameter | Value |
|----------|------|
| Chunk Size | 500 |
| Chunk Overlap | 100 |
| Strategy | Recursive Character Splitter |
| Top-K | 5 |

---

## Vector Database Configuration

| Parameter | Value |
|----------|------|
| Local Vector DB | ChromaDB |
| Production Vector DB | Pinecone |
| Similarity Search | Cosine |
| Metadata Support | Yes |
| Top-K Retrieval | 5 |

---

## LLM Configuration

| Parameter | Value |
|----------|------|
| Provider | OpenAI |
| Model | GPT-4o-mini |
| Temperature | 0.2 |
| Max Tokens | 512 |
| Streaming | Planned |
| Fallback | Ollama |

---

## Memory Configuration

| Parameter | Value |
|----------|------|
| Conversation Memory | Enabled |
| Session Memory | Enabled |
| Redis Memory | Planned |
| Long-Term Memory | Planned |

---

## Performance Metrics

| Metric | Value |
|------|------|
| Embedding Dimensions | 384 |
| Batch Size | 64 |
| Chunk Size | 500 |
| Chunk Overlap | 100 |
| Top-K Retrieval | 5 |
| Max Tokens | 512 |
| Temperature | 0.2 |
| Average Latency | 2–5 Seconds |

---

## Project Structure

```text
Full_Customer_Support_Chat_Bot_GenAI_AgentAI/

app/
│
├── agents/
├── api/
├── config/
├── core/
├── data_pipeline/
├── embeddings/
├── llm/
├── memory/
├── rag/
├── services/
├── shared/
├── vector_db/
└── main.py
│
tests/
frontend/
docs/
deployment/
data/
logs/
Dockerfile
docker-compose.yml
requirements.txt
.env.example
README.md
```

---

## Installation

```bash
git clone https://github.com/JayABharaTh01/Full_Customer_Support_Chat_Bot_GenAI_AgentAI.git

cd Full_Customer_Support_Chat_Bot_GenAI_AgentAI

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

Create:

```bash
cp .env.example .env
```

Example:

```env
OPENAI_API_KEY=

PINECONE_API_KEY=

HF_TOKEN=

LLM_PROVIDER=openai

OPENAI_MODEL=gpt-4o-mini

VECTOR_DB=chroma

EMBEDDING_PROVIDER=sentence_transformers

EMBEDDING_MODEL=all-MiniLM-L6-v2

CHROMA_COLLECTION=customer_support

LOG_LEVEL=INFO
```

---

## Running the Application

### FastAPI

```bash
uvicorn app.main:app --reload
```

### Swagger

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

### Health Check

```text
http://localhost:8000/api/v1/health
```

---

## Running Tests

### Embeddings

```bash
python -m tests.test_embedding
```

### Vector Database

```bash
python -m tests.test_vector
```

### RAG

```bash
python -m tests.test_rag
```

### Agents

```bash
python -m tests.test_agents
```

### LangGraph

```bash
python -m tests.test_graph
```

### Memory

```bash
python -m tests.test_memory
```

---

## Local URLs

| Service | URL |
|-------|-----|
| API | http://localhost:8000 |
| Swagger | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Health | http://localhost:8000/api/v1/health |

---

## Future Roadmap

```text
v1.0
-----
Local Multi-Agent Platform

v1.1
-----
Redis Memory

v1.2
-----
MCP Integration

v1.3
-----
Streamlit UI

v1.4
-----
Docker Deployment

v2.0
-----
AWS Migration

v2.1
-----
Amazon Bedrock

v2.2
-----
CloudWatch

v2.3
-----
ECS/EKS
```

---

## AWS Migration Plan

```text
Local
   ↓
EC2

SQLite
   ↓
RDS

ChromaDB
   ↓
Pinecone

OpenAI
   ↓
Bedrock

Memory
   ↓
Redis

Logs
   ↓
CloudWatch
```

AWS Services:

- IAM
- EC2
- S3
- RDS
- Bedrock
- VPC
- CloudWatch
- ECS
- EKS

---

## Version Information

| Property | Value |
|--------|------|
| Version | v1.0.0 |
| Release Name | Local Enterprise Edition |
| Status | Stable |
| Deployment | Local |
| Platform | GitHub Codespaces |
| Future | AWS + Bedrock |

---

## Author

### G. Jaya Bharath

- Data Scientist | GenAI Engineer
- Experience: 3.5+ Years
- Specialization:
  - Generative AI
  - Agentic AI
  - RAG Systems
  - Multi-Agent Architectures
  - MLOps
  - AWS

---

## License

MIT License

---

## Final Note

This project demonstrates:

- Enterprise Backend Development
- Multi-Agent AI Systems
- Retrieval-Augmented Generation
- LangGraph Orchestration
- Conversation Memory
- Vector Databases
- FastAPI
- Production-Ready Architecture

This repository serves as a complete reference implementation for building Enterprise AI Customer Support Platforms.
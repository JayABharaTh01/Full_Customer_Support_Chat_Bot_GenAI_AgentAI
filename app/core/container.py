"""
Dependency Container

Central place to register application services.
"""


class Container:

    llm = None

    embedding_model = None

    vector_store = None

    database = None

    memory = None

    prompt_manager = None

    orchestrator = None


container = Container()



# container.llm = OpenAIClient()

# container.vector_store = ChromaManager()

# container.embedding_model = SentenceTransformer(...)
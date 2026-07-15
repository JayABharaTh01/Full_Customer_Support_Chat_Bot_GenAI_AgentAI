# from app.utils.logger import get_logger

# logger = get_logger("api")


# def startup():

#     logger.info("Starting Customer Support AI...")

from app.utils.logger import get_logger
from app.core.bootstrap import bootstrap
from app.core.environment import check_environment

logger = get_logger("api")


def startup():

    # Create required directories
    bootstrap()

    # Check environment information
    check_environment()

    # initialize_llm()

    # initialize_embeddings()

    # initialize_vector_db()

    # initialize_database()

    # initialize_prompt_manager()

    # initialize_agent_orchestrator()
    

    logger.info(
        "Starting Customer Support AI..."
    )
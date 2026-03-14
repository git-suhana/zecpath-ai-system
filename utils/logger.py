from loguru import logger

logger.add("logs/ai_system.log", rotation="1 MB")

def get_logger():
    return logger
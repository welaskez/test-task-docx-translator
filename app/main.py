import logging

import uvicorn
from core.config import settings
from utils.init_app import create_app

app = create_app()

if __name__ == "__main__":
    logging.basicConfig(format=settings.log.log_format)
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )

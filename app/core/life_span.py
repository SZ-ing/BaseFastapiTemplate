from .config_manager import loadConfig
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifeSpan(app: FastAPI):
    """
    Template
    app.state.XXX = XXX
    try:
        yield
    finally:
        if hasattr(app.state, "XXX"):
            app.state.XXX.stop()
    """
    app.state.configs = loadConfig()
    try:
        yield
    finally:
        del app.state.configs
        # 此处放要进行资源清理的内容



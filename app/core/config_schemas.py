from pydantic import BaseModel

class ServerConfig(BaseModel):
    host: str
    port: int

class PathConfig(BaseModel):
    tmp: str
    out: str
    logs: str
    weights: str

class AppConfig(BaseModel):
    server: ServerConfig
    path: PathConfig
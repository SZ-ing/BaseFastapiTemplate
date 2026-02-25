from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/get_configs")
def getConfigs(request:Request):
    return {"state":True,"msg":request.app.state.configs}

@router.get("/aget_configs")
async def asyncGetConfigs(request:Request):
    return {"state":True,"msg":request.app.state.configs}

@router.get("/health_check")
def healthCheck():
    return {"state":True,"msg":"服务启动正常"}

@router.get("/ahealth_check")
async def asyncHealthCheck():
    return {"state":True,"msg":"服务启动正常"}
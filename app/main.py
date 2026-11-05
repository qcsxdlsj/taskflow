from fastapi import FastAPI
from app.core.config import settings 

app = FastAPI(
    title=settings.app_name,
    version='0.1.0',
    description='taskFlow任务管理后端API'
)

@app.get('/')
def read_root():
    """健康检查接口，用来确认服务活着。"""
    return {'message': 'taskFlow is running'}

@app.get('/health')
def health_check():
    """给部署平台/监控用的健康检查。"""
    return {'status': 'ok', "env": settings.app_env}
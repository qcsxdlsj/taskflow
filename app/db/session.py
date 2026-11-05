from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

#引擎
engine = create_engine(
    settings.database_url,
    echo=True,# 会把 ORM 生成的每一条 SQL 打印到控制台,上线前要关掉
    connect_args={"check_same_thread": False},# 为了让 SQLite 能跑起来.换成 PostgreSQL 时，这一行必须删掉
)

#会话工厂
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,#不自动把内存里的修改刷到数据库，等你显式 commit。行为更可预测，出问题好排查
    autocommit=False,#这是有状态的东西，默认关闭才对
    expire_on_commit=False,#会偷偷再发一次 SELECT。关掉它，commit 后对象还能正常读，少一次无谓查询
)

# fastAPI生成器依赖
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


















# # 1. 引擎：数据库地址 + 连接池，它本身不连数据库，是「生产连接的工厂」
# engine = create_engine(
#     settings.database_url,
#     echo=True, # 上线前要关掉
#     connect_args={"check_same_thread": False},
# )

# # 2. 会话工厂：每次调用 SessionLocal() 得到一个「和数据库对话的窗口」
# SessionLocal = sessionmaker(
#     bind=engine,
#     autoflush=False,
#     autocommit=False,
#     expire_on_commit=False,
# )


# def get_db() -> Generator[Session, None, None]:
#     """FastAPI 的依赖：每个请求开一个会话，请求结束自动关闭。"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
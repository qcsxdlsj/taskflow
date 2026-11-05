from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    """用户表。"""

    __tablename__ = "users"

    # 主键：自增整数
    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # 登录账号：唯一 + 索引，登录时按它查
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )

    # 密码哈希，绝不存明文
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # 昵称：展示用，可以重复，允许空串
    nickname: Mapped[str] = mapped_column(String(50), nullable=False, default="")

    # 是否启用：禁用用户用这个标记，不物理删除
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # 注册时间：由数据库在插入时生成
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
from app.db.session import SessionLocal
from app.models.user import User

db = SessionLocal()

# ---- 1. 插入 ----
user = User(email="zhangsan@test.com", password_hash="fake-hash", nickname="张三")
db.add(user)          # 只是放进会话，还没写库
db.commit()           # 这一步才真正 INSERT
db.refresh(user)      # 从数据库读回服务器生成的值（id、created_at）

dup = User(email="zhangsan@test.com", password_hash="x", nickname="李四")
db.add(dup)
db.commit()

print("新增成功，id =", user.id)
print("created_at =", user.created_at)

# ---- 2. 查询 ----
same = db.get(User, user.id)     # 按主键查，最简单的查法
print("查回来：", same.email, same.nickname)

# ---- 3. 删除（清理测试数据）----
db.delete(same)
db.commit()

print("测试数据已删除")
db.close()
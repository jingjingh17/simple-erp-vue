import sqlite3


# 登录
def get_user_login_from_db(username):
    conn = sqlite3.connect('simple_erp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, password FROM user WHERE name = ?", (username,))
    user = cursor.fetchone()
    print('数据库查到的内容',user)
    conn.close()
    return user

# 获取权限管理列表数据
def get_users_from_db():
    conn = sqlite3.connect('simple_erp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, createDate, department, role, phone, email, lastDate, lock FROM user")
    rows = cursor.fetchall()
    conn.close()
    return rows

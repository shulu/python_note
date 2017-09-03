# -*- coding: utf-8 -*-

import os,sqlite3


def creat_sql():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('CREATE TABLE IF NOT EXISTS user(id varchar(20) PRIMARY KEY , name varchar(20))')
    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('INSERT INTO user(id,name) VALUES (\'1\', \'Micheal\')')
    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)
    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()


def select_sql():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('SELECT * FROM user WHERE id=?',('1',))
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    cursor.close()
    cursor.close()


def home_work():
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    # 初始数据:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    result = cursor.execute('SELECT name FROM user WHERE score BETWEEN ? AND ? ORDER BY score ASC ', (low, high))
    #values = cursor.fetchall()
    values = []
    for row in result:
        values.append(row[0])
    #print(values)
    return values

# get_score_in(80, 95)
# get_score_in(60, 80)
# get_score_in(60, 100)
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')

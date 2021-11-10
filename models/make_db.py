import sqlite3
import random

db_path = "./hw.sqlite3"


def insert_db(conn):
    sql = '''
            INSERT INTO greetings (greeting,image_path) VALUES (?,?)
        '''

    values = ('Good evening', 'http://urx3.nu/xUVy')
    with sqlite3.connect(db_path) as conn:

        print(values)
        # DB実行時は、リストに格納すること注意する。
        conn.executemany(sql, [values])

# 確認用


def select_db(conn):
    sql = '''
        SELECT * FROM greetings
    '''
    select = conn.execute(sql)
    data = select.fetchall()
    return data

# ランダムでDBからgreetingを一つ取得


def get_random_greeting():
    table = 'greetings'
    id_list = get_id_list(table)
    # id一覧からランダムで一つ選びだす
    random_id = random.choice(id_list)['id']
    sql = 'SELECT greeting,image_path FROM ' + \
        table + ' WHERE id=' + str(random_id)
    greeting = execute_sql(sql)
    # 取得データは一つだけなのでここで0を指定しておく
    result = greeting[0]
    return result

# 指定したtableのID一覧を取得


def get_id_list(table):
    sql = 'SELECT id FROM ' + table
    id_list = execute_sql(sql)
    return id_list

# DBに接続してsqlを実行


def execute_sql(sql):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.close()
    return result


with sqlite3.connect(db_path) as conn:

    # データ挿入
    # insert_db(conn)
    # データ取得
    data = select_db(conn)
    for row in data:
        print(row)

result1 = get_random_greeting()
print(result1)

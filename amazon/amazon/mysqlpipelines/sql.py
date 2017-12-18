import pymysql
from .. import settings
# import settings
conn = pymysql.connect(
    host=settings.MYSQL_HOST,
    port=settings.MYSQL_PORT,
    user=settings.MYSQL_USER,
    password=settings.MYSQL_PWD,
    db=settings.MYSQL_DB,
    charset='utf8'
)

cursor = conn.cursor()


class Sql(object):
    @staticmethod
    def insert_table_goods(goods_name, goods_price):
        sql = 'insert into goods(name,price) values(%s,%s);'
        cursor.execute(sql, args=(goods_name, goods_price))
        conn.commit()

    @staticmethod
    def is_repeat(goods_name, goods_price):
        sql = 'select count(1) from goods where name=%s and price=%s'
        cursor.execute(sql, args=(goods_name, goods_price))
        res=cursor.fetchone()[0]
        if res >= 1:
            return True

# if __name__ == '__main__':
#     # Sql.insert_table_goods('123', 'qwe')
#     print(Sql.is_repeat('123', 'qwe'))

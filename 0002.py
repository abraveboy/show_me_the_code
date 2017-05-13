#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

"""
Help on method execute in module pymysql.cursors:
execute(query, args=None) method of pymysql.cursors.Cursor instance
    Execute a query

    :param str query: Query to execute.

    :param args: parameters used with query. (optional)
    :type args: tuple, list or dict

    :return: Number of affected rows
    :rtype: int

    If args is a list or tuple, %s can be used as a placeholder in the query.
    If args is a dict, %(name)s can be used as a placeholder in the query.
    """
import pymysql

#建立数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     db='samp')

#创建数据库游标
cursor = db.cursor()

#若表act_code存在则删除
def if_exist():
    return "drop table if exists act_code "

#创建表
def create_table():
    return """create table act_code (
                        activation_code CHAR(10) PRIMARY KEY )"""
def main():
    with open('activation_code.txt') as wb:
        for code in wb:
            insert ="insert into act_code(activation_code) values(%s)"
            cursor.execute(insert,code.strip())
if __name__ == '__main__':
    #对数据库进行操作
    cursor.execute(if_exist())
    cursor.execute(create_table())
    main()
    #提交表单
    db.commit()
    #关闭数据库
    db.close()

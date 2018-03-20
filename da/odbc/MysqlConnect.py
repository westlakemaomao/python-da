import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ymy@201507',
                             db='recsys',
                             port=3306,
                             charset='utf8')  # 注意是utf8不是utf-8
# try:
#     with connection.cursor() as cursor:
#         sql_1 = 'select * from kline_1_min LIMIT 100'
#         cout_1 = cursor.execute(sql_1)
#         print("数量： " + str(cout_1))
#         for row in cursor.fetchall():
#             print(row)
# finally:
#     print("OK")
#     connection.close()

def getMysqlData(sql):
    result=[]
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            i=0
            for row in cursor.fetchall():
                result.append(row)
                # print(row)
            return result
    finally:
        connection.close()
if __name__=="__main__":
    sql="select * from kline_1_min LIMIT 100"
    resultList=getMysqlData(sql)
    for i in resultList:
        print(i)

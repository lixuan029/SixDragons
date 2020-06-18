# -*- coding: UTF-8 -*-
import pymysql
from DbConnect import passwd, host, port, user, db

'''获取年份天干及属性
    年干序号：StemNo
    年干名称：StemName
    阴阳属性：StemAttribute_y
    五行属性：StemAttribute_e
'''
def getChineseYearMain(sunYear):
    if sunYear % 10 < 3:
        chineseYearMainNo = sunYear % 10 + 3
    else:
        chineseYearMainNo = sunYear % 10
    # 打开数据库连接
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM heavenlystem" \
         " WHERE StemNo = %s" % chineseYearMainNo
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    cols = cursor.description
    colname = []
    for i in cols:
        colname.append(i[0])
    chineseYear = {}
    for row in results:
        chineseYear[colname[0]] = row[0]
        chineseYear[colname[1]] = row[1]
        chineseYear[colname[2]] = row[2]
        chineseYear[colname[3]] = row[3]
    # 关闭数据库连接
    conn.close()
    return chineseYear


'''获取年份地支及属性
    地支序号：BranchNo
    地支名称：BranchName
    阴阳属性：BranchAttribute_y
    五行属性：BranchAttribute_e
'''
def getChineseYearBranch(sunYear):
    chineseYearBranchNo = (sunYear % 12) - 3
    # 打开数据库连接
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM earthlybranch" \
         " WHERE BranchNo = %s" % chineseYearBranchNo
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    cols = cursor.description
    colname = []
    for i in cols:
        colname.append(i[0])
    chineseYearBranch = {}
    for row in results:
        chineseYearBranch[colname[0]] = row[0]
        chineseYearBranch[colname[1]] = row[1]
        chineseYearBranch[colname[2]] = row[2]
        chineseYearBranch[colname[3]] = row[3]
    # 关闭数据库连接
    conn.close()
    return chineseYearBranch


if __name__ == '__main__':
    print(getChineseYearMain(2019)['StemName'])
    print(getChineseYearBranch(2020))

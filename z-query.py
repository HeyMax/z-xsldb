#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlrd
import sys
import pymysql

def query_from_mysql(cur,target_str):
	#fetching result
	query_nrow = cur.execute("select Question,Answer from `QA` where Question like '%{}%'".format(target_str))
	query_result = cur.fetchall()
	#formatting it
	for row in query_result:
		question = row[0]
		answer = row[1]
		print("Q:{}\nA:{}\n".format(question,answer))
	print("\n共计{}个结果".format(str(query_nrow)))
	return query_result
	
if __name__ == '__main__':
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Dw199719',db='QQQA',charset='utf8')
	cur = conn.cursor
	#create cursor
	cur = conn.cursor()
	cur.execute("USE QQQA")
	
	#query QA from table`QA`
	try:
		if not query_from_mysql(cur,str(sys.argv[1])):
			print("暂无相关信息")
	except IndexError:
		print("usage:z-query.py <inputfilename.xlsx>")

	#close cursor
	cur.close()
	#conn_rollback
	try:
		conn.commit()
	except Exception:	
		conn.rollback()
	#close connection
	conn.close()
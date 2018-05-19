#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlrd
import sys
import pymysql

def query_from_mysql(cur,keywords):
	#multiKeywords
	query_exe = "select Question,Answer from `QA` where concat(Question,',',Answer) like '%{}%'".format(keywords[1])
	if len(keywords) > 2:
		for keyword in range(2,len(keywords)):
			query_exe = query_exe + " and concat(Question,',',Answer) like '%{}%'".format(keywords[keyword])
	#fetching result	
	query_nrow = cur.execute(query_exe)
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
	#use DB QQQA
	cur.execute("USE QQQA")
	
	#query QA from table`QA`
	try:
		#str(sys.argv[1]).split()
		if not query_from_mysql(cur,sys.argv):
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
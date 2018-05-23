#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import xlrd
import sys
import pymysql
import json

def query_from_mysql(dbname, query_exe, fields):
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Dw199719',charset='utf8')
	#create cursor
	cur = conn.cursor()
	#use DB QQQA
	cur.execute("USE " + dbname)
	
	#fetching result	
	query_nrow = cur.execute(query_exe)
	query_result = cur.fetchall()
	inventories = []
	error_status = 1
	#formatting it
	for row in query_result:
		inventroy = {}
		for index in range(len(fileds)):
			inventroy[fields[index]] = "{}\n".format(row[index])
		#inventroy_js = json.dumps(inventroy,ensure_ascii=False)
		print(inventroy)
		inventories.append(inventroy)
	print("\n共计{}个结果".format(str(query_nrow)))
	if query_nrow :
		error_status = 0
	return_result = json.dumps({'error_status':error_status,'inventories':inventories},ensure_ascii=False)
	#print(return_result)
	#close cursor
	cur.close()
	#conn_rollback
	try:
		conn.commit()
	except Exception:	
		conn.rollback()
	#close connection
	conn.close()
	return return_result
	
if __name__ == '__main__':
	query_from_mysql()
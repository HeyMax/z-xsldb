#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from z_import import create_table_based_on_excel_book
import xlrd
import sys
import pymysql
import json

class Recorder:
	def __init__(self, recordObject):
		self.recordObject = recordObject
		self.errorcode = 1
		
	def record_it(self, method, recordObject):
		# try:
		keyword_update_state = method(recordObject)
		# except Exception:
			# print(self.errorcode)
	
def hot_keywords_record(keywords):
	#establish connection
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Dw199719',db='QQQA',charset='utf8')
	#create cursor
	cur = conn.cursor()
	#use DB QQQA
	cur.execute("USE QQQA")
	
	#create_table_hot_keywords
	cur.execute("CREATE TABLE IF NOT EXISTS `HOTKEYWORDS` (`KEYWORD` VARCHAR(255) NOT NULL, `SEARCHINTEREST` INT, PRIMARY KEY(`KEYWORD`));")
	#insert on duplicate key
	for keyword in keywords:
		print(keyword)
		row_insert = "INSERT INTO `HOTKEYWORDS` (KEYWORD, SEARCHINTEREST) VALUES ('"+ keyword +"', 1) ON DUPLICATE KEY UPDATE SEARCHINTEREST = SEARCHINTEREST + 1;"
		cur.execute(row_insert)
	#close cursor
	cur.close()
	#conn_rollback
	try:
		conn.commit()
	except Exception:	
		conn.rollback()
	#close connection
	conn.close()
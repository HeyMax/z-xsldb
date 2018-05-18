#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlrd
import sys
import pymysql
	
def create_tables_based_on_excel_book(cur,path):
	try:
		book = xlrd.open_workbook(path)
	except IndexError:
		print("usage:z-import.py <inputfilename.xlsx>")
	
	for sheet in book.sheets():
		#create table for sheet
		print(sheet.name)
		cur.execute("DROP TABLE IF EXISTS `{0}`".format(sheet.name))
		cur.execute("CREATE TABLE IF NOT EXISTS `{0}` (`ID` INT(11) NOT NULL AUTO_INCREMENT, `DATE` TEXT , `Question` TEXT, `Answer` TEXT, PRIMARY KEY(`ID`)) AUTO_INCREMENT=1;".format(sheet.name))
		#extract data from each row
		for row in range(1,sheet.nrows):
			sqlstr=[]
			for col in range(0,sheet.ncols):
				if str(sheet.cell(row,col).value):
					sqlstr.append(str(sheet.cell(row,col).value))
				else:
					sqlstr.append(" ")
			row_insert = "INSERT INTO `"+sheet.name+"` (DATE, Question, Answer) VALUES(%s, %s, %s)" 
			#insert values into table
			cur.execute(row_insert,sqlstr[:3])
			
if __name__ == "__main__":
	#establish connection
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Dw199719',db='QQQA',charset='utf8')

	#create cursor
	cur = conn.cursor()
	#use DB QQQA
	cur.execute("USE QQQA")
	
	#create tables based on XXX.xlsx
	create_tables_based_on_excel_book(cur,str(sys.argv[1]))
	
	#close cursor
	cur.close()
	#conn_rollback
	try:
		conn.commit()
	except Exception:	
		conn.rollback()
	#close connection
	conn.close()
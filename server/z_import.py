#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlrd
import sys
import pymysql
	
def create_table_based_on_excel_book(cur,path):
	#establish connection
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Dw199719',db='QQQA',charset='utf8')
	#create cursor
	cur = conn.cursor()
	#use DB QQQA
	cur.execute("USE QQQA")
	
	try:
		book = xlrd.open_workbook(path)
	except IndexError:
		print("usage:z-import.py <inputfilename.xlsx>")
	
	#create table
	cur.execute("DROP TABLE IF EXISTS `QA`")
	cur.execute("CREATE TABLE IF NOT EXISTS `QA` (`ID` INT(11) NOT NULL AUTO_INCREMENT, `DATE` TEXT , `Question` TEXT, `Answer` TEXT, PRIMARY KEY(`ID`)) AUTO_INCREMENT=1;")
	
	#insert rows into table from sheets
	for sheet in book.sheets():
		print(sheet.name)
		#extract data from each row
		for row in range(1,sheet.nrows):
			sqlstr=[]
			for col in range(0,sheet.ncols):
				if str(sheet.cell(row,col).value):
					sqlstr.append(str(sheet.cell(row,col).value))
				else:
					sqlstr.append(" ")
			row_insert = "INSERT INTO `QA` (DATE, Question, Answer) VALUES(%s, %s, %s)" 
			#insert values into table
			cur.execute(row_insert,sqlstr[:3])
			
if __name__ == "__main__":

	
	#create table based on XXX.xlsx
	try:
		create_table_based_on_excel_book(cur,str(sys.argv[1]))
	except IndexError:
		print("usage:z-import.py <inputfilename.xlsx>")
		
	#close cursor
	cur.close()
	#conn_rollback
	try:
		conn.commit()
	except Exception:	
		conn.rollback()
	#close connection
	conn.close()
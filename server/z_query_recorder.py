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
		
	def record_it(self, recordObject=self.recordObject, method=create_table_based_on_excel_book):
		try:
			return method(recordObject)
		except Exception:
			return self.errorcode
	

#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlrd
import sys
import pymysql
import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

def download_import_QQ_xlsx():
	os.system('bash /root/download_import.sh')
			
if __name__ == "__main__":
	#create scheduler
	scheduler = BackgroundScheduler()
	#add_job&trigger-interval
	scheduler.add_job(download_import_QQ_xlsx,'interval',days=1,start_date=datetime.datetime.now().date())
	#run it
	scheduler.start()
	try:
		while True:
			time.sleep(5)
	except SystemExit:
		scheduler.shutdown()
		print("Exception happend")
		client.close()
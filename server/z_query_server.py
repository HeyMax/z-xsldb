from __future__ import unicode_literals
from flask import Flask
from flask import make_response
from z_query import query_from_mysql
from flask import request
from flask_cors import *
from z_query_recorder import Recorder
from z_query_recorder import hot_keywords_record
import pymysql
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)
HKWD_recorder = Recorder("HotKeywords")

#query_by_keywords	
@app.route('/result/', methods=['POST'], strict_slashes=False)
def query():
	jsondata = request.get_json('keywords')
	print(jsondata)
	if request.method == 'POST':
		#SQL query_exe
		query_exe = "select Question,Answer from `QA` where concat(Question,',',Answer) like '%{}%'".format(keywords[0])
		if len(jsondata['keywords']) > 1:
			for keyword in range(1,len(jsondata['keywords'])):
				query_exe = query_exe + " and concat(Question,',',Answer) like '%{}%'".format(jsondata['keywords'][keyword])	
		query_result = query_from_mysql('QQQA', query_exe, ['Q', 'A'])#json.loads(keywords, object_hook=JSONObject).keywords
		#rst = make_response(query_result)
		#rst.headers['Access-Control-Allow-Origin'] = '*'
		HKWD_recorder.record_it(hot_keywords_record, jsondata['keywords'])
		return query_result

#get_hot_keywords
@app.route('/hotkeywords/', methods=['GET'], strict_slashes=False)
def get_hottop_keys():
	query_exe = 'select * from `HOTKEYWORDS` order by SEARCHINTEREST DESC'
	return query_from_mysql('QQQA', query_exe, ['Keyword', 'Heat'])
	
if __name__ == '__main__':
	app.run(host='172.20.16.164', port=7878, debug=True)
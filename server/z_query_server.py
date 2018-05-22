from flask import Flask
from flask import make_response
from z_query import query_from_mysql
from flask import request
from flask_cors import *
from z_query_recorder import Recorder
from z_query_recorder import hot_keywords_record
import json


app = Flask(__name__)
CORS(app, supports_credentials=True)
HKWD_recorder = Recorder("HotKeywords")
	
@app.route('/result/', methods=['POST'], strict_slashes=False)
def query():
	jsondata = request.get_json('keywords')
	print(jsondata)
	if request.method == 'POST':
		query_result = query_from_mysql(jsondata['keywords'])#json.loads(keywords, object_hook=JSONObject).keywords
		#rst = make_response(query_result)
		#rst.headers['Access-Control-Allow-Origin'] = '*'
		HKWD_recorder.record_it(hot_keywords_record, jsondata['keywords'])
		return query_result
	
if __name__ == '__main__':
	app.run(host='172.20.16.164', port=7878, debug=True)
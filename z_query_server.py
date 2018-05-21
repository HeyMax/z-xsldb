from flask import Flask
from flask import make_response
from z_query import query_from_mysql
import json

# class JSONObject:
	# def __init__(self,d):
		# self.__dict__ = d
		
app = Flask(__name__)

@app.route('/result/<keywords>')
def query(keywords):
	query_result = query_from_mysql(keywords)#json.loads(keywords, object_hook=JSONObject).keywords
	rst = make_response(query_result)
	rst.headers['Access-Control-Allow-Origin'] = '*'
	return rst, 200
	
if __name__ == '__main__':
	app.run(host='172.20.16.160', port=7878, debug=True)
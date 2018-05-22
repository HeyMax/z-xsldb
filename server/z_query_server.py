from flask import Flask
from flask import make_response
from z_query import query_from_mysql
from flask import request
from flask_cors import *
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)
	
@app.route('/result/', methods=['POST'], strict_slashes=False)
def query():
	print(request.get_json('keywords'))
	if request.method == 'POST':
		query_result = query_from_mysql(request.get_json('keywords')['keywords'])#json.loads(keywords, object_hook=JSONObject).keywords
		#rst = make_response(query_result)
		#rst.headers['Access-Control-Allow-Origin'] = '*'
		return query_result
	
if __name__ == '__main__':
	app.run(host='172.20.16.160', port=7878, debug=True)
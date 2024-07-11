from flask import Flask
from flask import json
import logging
import datetime

app = Flask(__name__)

@app.route('/healthz')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    app.logger.info('${timestamp} "GET/"')
    app.logger.debug('DEBUG message')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"db_connection_count":1,"post_count":7}}),
            status=200,
            mimetype='application/json'
    )

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    app.logger.info('${timestamp} "GET /metrics HTTP/1.1"')
    return response

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

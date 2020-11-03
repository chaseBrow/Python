# app.py
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        print("get")
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
#
# @app.route('/test')
# def test_page():
#     # look inside `templates` and serve `index.html`
#     return render_template('index.html')


here is the data b'POST / HTTP/1.1\r\nHost: localhost:3080\r\nConnection: keep-alive\r\nContent-Length: 5\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36\r\nContent-Type: text/plain;charset=UTF-8\r\nAccept: */*\r\nOrigin: http://localhost:8080\r\nSec-Fetch-Site: same-site\r\nSec-Fetch-Mode: cors\r\nSec-Fetch-Dest: empty\r\nReferer: http://localhost:8080/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\n\r\nchase'

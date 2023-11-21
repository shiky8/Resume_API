from flask import Flask
app = Flask(__name__)
from functools import wraps
from flask import request, abort,jsonify
import ssl
import json
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('host.cert', 'host.key')
read_cv = open("cv2.json")
my_cv=json.load(read_cv)
# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.args.get('key') and request.args.get('key') == key:
            return view_function(*args, **kwargs)
        # print("key = ",key)
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@app.route('/cv/')
@require_appkey
def cv():
    return jsonify(my_cv)

@app.route('/personal_info/', methods=['GET'])
@require_appkey
def personal_info():
    return jsonify(my_cv[0]["personal_info"])

@app.route('/links/', methods=['GET'])
@require_appkey
def links():
    return jsonify(my_cv[0]["links"])

@app.route('/objective/', methods=['GET'])
@require_appkey
def objective():
    return jsonify(my_cv[0]["objective"])

@app.route('/skills/', methods=['GET'])
@require_appkey
def skills():
    return jsonify(my_cv[0]["skills"])

@app.route('/Soft_skills/', methods=['GET'])
@require_appkey
def Soft_skills():
    return jsonify(my_cv[0]["Soft_skills"])

@app.route('/progamming/', methods=['GET'])
@require_appkey
def progamming():
    return jsonify(my_cv[0]["progamming language"])

@app.route('/language/', methods=['GET'])
@require_appkey
def language():
    return jsonify(my_cv[0]["language"])

@app.route('/Awards/', methods=['GET'])
@require_appkey
def Awards():
    return jsonify(my_cv[0]["Awards"])

@app.route('/education/', methods=['GET'])
@require_appkey
def education():
    return jsonify(my_cv[0]["education"])

@app.route('/certificates/', methods=['GET'])
@require_appkey
def certificates():
    return jsonify(my_cv[0]["certificates"])

@app.route('/experience/', methods=['GET'])
@require_appkey
def experience():
    return jsonify(my_cv[0]["experience"])

@app.route('/project/', methods=['GET'])
@require_appkey
def project():
    return jsonify(my_cv[0]["project"])

@app.route('/Badges/', methods=['GET'])
@require_appkey
def Badges():
    return jsonify(my_cv[0]["Badges"])
@app.route('/')
def home():
    return "hi shiky"

app.run(host='0.0.0.0', debug = False, ssl_context=context)

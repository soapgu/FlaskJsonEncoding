from flask import Flask,jsonify
import json
from markupsafe import escape

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = False;

#set = app.config.from_pyfile("config.py");
#print("load config" + str(set));
print(app.config);
app.json.ensure_ascii=False;

@app.route("/")
def hello_world():
    data = {'message': 'test utf-8,中文！'}
    #return json.dumps(data,ensure_ascii=False);
    #response = jsonify(data)
    return data
   #return "<p>中文你好!</p>"

@app.route('/mp3/<song>')
def show_user_profile(song):
    # show the user profile for that song
    return f'Song: {escape(song)}'
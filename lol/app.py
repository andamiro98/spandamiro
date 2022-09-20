from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

from pymongo import MongoClient
import certifi
from datetime import datetime

ca = certifi.where();
client = MongoClient('mongodb+srv://test:sparta@cluster0.q5fchzu.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     tlsCAFile=ca)
db = client.myloldictionary


@app.route('/')
def main():
    lists = list(db.loldb.find({}, {'_id': False}))
    return render_template("index.html", lists=lists)

@app.route('/write')
def write():
    return render_template("write.html")

@app.route("/api/posts", methods=["POST"])
def save_post():
    title_receive = request.form['title_give']
    name_receive = request.form['name_give']
    position_receive = request.form['position_give']
    star_receive = request.form['star_give']
    desc_receive = request.form['desc_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'img{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'image': f'{filename}.{extension}',
        'title': title_receive,
        'name': name_receive,
        'position': position_receive,
        'star': star_receive,
        'desc': desc_receive
    }

    db.loldb.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# dependencies
import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask import Response
import json

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/songs'
# terminal error told me to add this below
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

# You can put as many http methods as you want in 'methods' and use conditionals OR
# split into different functions and make multiple of the same @app.routes with each differnet route function
@app.route('/api/v1/songs', methods=['GET', 'POST'])
def get_all_songs():
    songs = models.Songs.query.all()
    my_dict = {}

    for index, song in enumerate(songs):
        my_dict.update({ index: str(song) })

    return jsonify(my_dict)

if __name__ == '__main__':
    app.debug = True
    app.run()

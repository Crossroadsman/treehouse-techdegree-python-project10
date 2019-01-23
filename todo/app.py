import os

from flask import Flask, g, jsonify, render_template, send_from_directory

import config
import models
from resources.todos import todos_api


app = Flask(__name__)
app.register_blueprint(todos_api, url_prefix=config.API_URL_PREFIX)


@app.route('/')
def my_todos():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    """This is to get rid of the annoying 404 for the favicon"""
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'  # this mimetype per flask docs
    )


# ----------------

if __name__ == '__main__':

    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)

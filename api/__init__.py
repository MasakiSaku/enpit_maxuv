from flask import Flask, make_response, jsonify
from .views.book import book_router
from .views.bookshelf import bookshelf_router
from api.database import db
import config


def create_app():
    
    app = Flask(__name__)

    #DBの設定
    app.config.from_object('config.Config')
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)
    app.register_blueprint(book_router, url_prefix='/api')
    app.register_blueprint(bookshelf_router, url_prefix='/api')

    return app

app = create_app()
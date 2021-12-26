from singletondb import *
from flask import Flask, request
from flask_restful import Api
from chain import *
from itemsdb import *
from cacheditems import *

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    cached_items = ItemsCache()
    cached_items.update()

    @app.route('/get-items/', methods = ['GET', 'POST', 'DELETE', 'PUT'])
    def proc():
        get_proc = GetProcessor(cached_items)
        get_proc.set_next(PostProcessor(cached_items)).set_next(DeleteProcessor(cached_items)).set_next(PutProcessor(cached_items))
        return get_proc.process(request.method)
    app.run(debug = True)
    DBConnection.get_instance().conn.close()
# & d:/SomeSourceFiles/ML/lab1/.venv/Scripts/python.exe d:/SomeSourceFiles/architecture/lab3/main.py

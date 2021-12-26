from singletondb import *
from flask import Flask, request
from flask_restful import Api
from chain import *
from itemsdb import *

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    @app.route('/get_items/', methods = ['GET', 'POST', 'DELETE', 'PUT'])
    def proc():
        get_proc = GetProcessor()
        get_proc.set_next(PostProcessor()).set_next(DeleteProcessor()).set_next(PutProcessor())
        return get_proc.process(request.method)
    app.run(debug = True)
    DBConnection.get_instance().conn.close()

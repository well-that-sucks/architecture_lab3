from itembuilder import *
from flask_restful import reqparse

class Facade:
    def __init__(self, cache):
        self.items_db = ItemsDB()
        self.cache = cache

    def get(self):
        return self.cache.get_cache()


    def update(self):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('item_id')
        reqparser.add_argument('item_name')
        reqparser.add_argument('description')
        reqparser.add_argument('quantity')
        reqparser.add_argument('price')
        reqparser.add_argument('supplier_id')
        args = reqparser.parse_args()
        self.items_db.update(args)

    def delete(self):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('item_id')
        args = reqparser.parse_args()
        self.items_db.delete(args['item_id'])

    def insert(self):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('item_id')
        reqparser.add_argument('item_name')
        reqparser.add_argument('description')
        reqparser.add_argument('quantity')
        reqparser.add_argument('price')
        reqparser.add_argument('supplier_id')
        args = reqparser.parse_args()
        self.items_db.insert(args)
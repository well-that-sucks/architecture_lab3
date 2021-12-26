from itembuilder import *
from flask_restful import reqparse

class Facade:
    def __init__(self):
        self.items_db = ItemsDB()

    def get(self):
        builder_manager = BuilderManager()
        builder = DatabaseItemBuilder()
        builder_manager.set_builder(builder)
        builder_manager.build()
        items_from_db = builder.get_items()
        builder = FirstServiceItemBuilder()
        builder_manager.set_builder(builder)
        builder_manager.build()
        items_from_service1 = builder.get_items()
        builder = SecondServiceItemBuilder()
        builder_manager.set_builder(builder)
        builder_manager.build()
        items_from_service2 = builder.get_items()
        return items_from_db.add_items(items_from_service1).add_items(items_from_service2).items

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
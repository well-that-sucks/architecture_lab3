from flask import Flask
from flask_restful import Api

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    @app.route('/price-list/', methods = ['GET'])
    def proc_pricelist():
        hardcoded_pricelist_itemset = [{'item_id': 101, 'item_name': 'Jack Daniels', 'price': 10},
                                    {'item_id': 102, 'item_name': 'Captain Morgan Spiced Gold', 'price': 40}, 
                                    {'item_id': 103, 'item_name': 'Martini Asti', 'price': 20},
                                    {'item_id': 104, 'item_name': 'Fiorelli Bianco', 'price': 25},
                                    {'item_id': 105, 'item_name': 'Bacardi Spiced', 'price': 35}]
        return {'items': hardcoded_pricelist_itemset}
    
    @app.route('/details/<int:id>', methods = ['GET'])
    def proc_details(id):
        hardcoded_details_itemset = [{'item_id': 101, 'description': 'Whiskey', 'quantity': 119, 'supplier_id': 4},
                            {'item_id': 102, 'description': 'Rome', 'quantity': 54, 'supplier_id': 1}, 
                            {'item_id': 103, 'description': 'Wine', 'quantity': 99, 'supplier_id': 2},
                            {'item_id': 104, 'description': 'Fragolino', 'quantity': 5, 'supplier_id': 4},
                            {'item_id': 105, 'description': 'Rome', 'quantity': 140, 'supplier_id': 5}]
        for item in hardcoded_details_itemset:
            if item['item_id'] == id:
                return item

    app.run(port = 5002, debug = True)
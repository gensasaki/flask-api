from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Special store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.0
            }
        ]
    }
]

@app.route('/', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port=5000)

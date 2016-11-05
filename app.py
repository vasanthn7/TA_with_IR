#!bin/python
from flask import Flask, jsonify, request
from getrecipe import get_recipe
from getdetail import get_detail
from ImageRecog import get_ing
app = Flask(__name__)

@app.route('/api/recipe/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks':tasks})
@app.route('/api/image', methods=['GET'])
def image_recog():
    url = request.args.get('url')
    page  = request.args.get('page')
    obj = get_ing(url)
    ing = obj.return_ing()
    obj1 = get_recipe(ing,page)
    return obj1.return_recipe()

@app.route('/api', methods=['GET'])
def get_task():
    ing = request.args.get('ingredients')
    page  = request.args.get('page')
    obj = get_recipe(ing,page)
    return obj.return_recipe()

@app.route('/api/details/<string:id>', methods=['GET'])
def get_details(id):
    obj = get_detail(id)
    return obj.return_detail()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

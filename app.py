#!bin/python
from flask import Flask, jsonify, request
from getrecipe import get_recipe
from getdetail import get_detail
app = Flask(__name__)

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
# l = [
#     {'a':1, 'b':2},
#     {'c':3, 'd':4}
# ]

@app.route('/api/recipe/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks':tasks})

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

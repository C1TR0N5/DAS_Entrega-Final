from flask import Blueprint, request, render_template, jsonify
from model import item_model, facade, data_db
from repository.item_db import ItemRepo
import requests



blueprint = Blueprint('item_controller', __name__)
itemRepo = ItemRepo()

Adapter = item_model.Adapter()

@blueprint.route('/')
def main():    
    return render_template('index.html')

@blueprint.route('/add_item', methods=['POST'])
def addItem():
    
    if request.method == 'POST':

        sku = request.form['sku']
        sku_adapter = Adapter.with_sku(sku)
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        exp_date = request.form['exp_date']

        item = (item_model.ItemBuilder()
                .with_sku(sku_adapter)
                .with_name(name)
                .with_description(description)
                .with_price(price)
                .with_quantity(quantity)
                .with_expiration_date(exp_date)
        )
        
        

        inserted = itemRepo.add(item)

        if inserted:
            return 'Insertado'
        
        return 'No se insertó'
       


@blueprint.route('/get_item', methods=['GET'])
def getItem():

    if request.method == 'GET':
        items = itemRepo.get_all()  

        return jsonify(items)


@blueprint.route('/delete_item', methods=['POST'])
def deleteItem():

    if request.method == 'POST':
        sku = request.form['item_id']

    try:
        success = itemRepo.delete(sku)
        if success:
            return 'Elemento eliminado correctamente'
        else:
            return 'No se pudo eliminar el elemento', 500

    except Exception as e:
        return f'Error al intentar eliminar el elemento: {e}', 500
    
    
@blueprint.route('/converter', methods=['GET', 'POST'])
def currency_converter():
    converter_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=7b52c31d973e54a40972abb73d1e168a'
    data = requests.get(converter_api).json()
        
    mxn, usd = facade.Facade().operations(data)

    arrayItems = itemRepo.get_all()
    
    
    list_new = list()
    for item in arrayItems:
        convertion = item[3] * usd
        list_new.append({"SKU": item[0], "Name": item[1] , "Description": item[2], "Price": convertion, "Currency" : usd, "Quantity": item[4]})
        

    return jsonify(list_new)
from controller.item_controller import addItem, getItem, deleteItem, currency_converter, Adapter

def test_addItem():
    assert addItem() == "Item agregado correctamente" or "Item no agregado"

def test_getItem():
    assert getItem() != None or ""

def test_deleteItem():
    assert deleteItem() == "Item eliminado correctamente" or 'Item no eliminado' or 'Error al intentar eliminar el item'

def test_currency_converter():
    assert currency_converter() != None or "" 

def test_adapter():
    assert Adapter != None or ""


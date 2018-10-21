from app.model.item import Item
import json

def query_all():
    data = Item.query.all()
    return data
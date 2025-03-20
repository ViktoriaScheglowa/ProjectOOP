import json
import os

from src.product import Product
from src.category import Category

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

def creat_objects_from_json(data):

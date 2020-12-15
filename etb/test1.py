from flask import Blueprint
test1 = Blueprint("test1", __name__)

name = "Sam"

def myfunc(name1):
     print(name1)
     return print(name1)
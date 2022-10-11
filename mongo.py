from flask import Response
from pymongo import MongoClient
from bson import json_util

# Conexión a la BD de mongo
# MONGO_URI = 'mongodb://localhost:27017'
MONGO_URI = 'mongodb+srv://IAPEXDBMONGO:<password>@iapex.rbjpplk.mongodb.net/?retryWrites=true&w=majority'
conn = MongoClient(MONGO_URI)
db = conn.iapex
person = db.persons

def insertPerson(Person) :
    insertP = person.insert_one(Person)

def listPersons(Person):
    #lista = person.find({"estado": Person.estado})# ESTE ES EL QUE DEBERIA DE IR
    
    lista = person.find() #ESTE ES PARA PRUEBAS
    results = []
    for x in lista:
        results.append(x)
    return results

    # lista = person.find() #ESTE ES PARA PRUEBAS BORRAR
    # response = json_util.dumps(lista)
    # return Response(response, mimetype='application/json')


def getPersons(pers):
    results = []
    for x in pers:
        ax = person.find_one({"_id": x})
        results.append(ax)
    response = json_util.dumps(results)
    return Response(response, mimetype='application/json')

def getAllPersons():
    results = person.find()
    response = json_util.dumps(results)
    return Response(response, mimetype='application/json')



from flask import Flask
from flask import request
from flask import json
from flask_cors import CORS, cross_origin
import mongo
import main

app = Flask(__name__)

CORS(app)

@cross_origin
@app.route("/")
def hello():
        return "Bienvenido a IAPEX"

@cross_origin
@app.route('/person', methods = ['POST'])
def postPerson():    
    content = request.get_json()
    mongo.insertPerson(content)
    return "Listo"

@cross_origin
@app.route('/buscar', methods = ['POST'])
def postFindPerson():
        content = request.get_json() #esta es la descripcion de la persona
        comparar = mongo.listPersons(content) # aqui busco las personas del mismo estado para poder comparar
        
        #EN ESTA FUNCION ESTARIA BUSCANDO LAS 5 PERSONAS MAS PARECIDAS A EL content(que sean del mismo estado)
        print(content)
        print(comparar)
        results = main.buscarPersona(content, comparar)
        return mongo.getPersons(results)


@cross_origin
@app.route('/registros', methods = ['GET'])
def getPersons():
        results = mongo.getAllPersons()
        return results


if __name__ == "__main__":
         app.run(host="0.0.0.0",debug=True)
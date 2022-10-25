from operator import methodcaller
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
#operaciones en el sistema
import os

#Generar el servidor en Flask (backend)
servidorWeb = Flask(__name__)

#Anotacion @
@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

#procesar datos a traves del form
@servidorWeb.route("/modeloIA", methods=["POST"])
def modeloForm():
    #procesar datos de entrada
    contenido = request.form
    print(contenido)
    #los json en python son diccionarios, lo convertimos 
    return jsonify({"resultado":"datos recibidos"})

#procesar datos dl archivo y guardarlos en la ruta del servidor, imprimir las lineas
@servidorWeb.route("/modeloFile", methods=["POST"])
def modeloFile():
    f = request.files['file']
    #trabajar con el file name pero usando otra biblioteca werkzug.utils
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd,'files',filename)
    f.save(path)
    file = open(path,'r')
    for line in file:
        print(line)
    return jsonify({"resultado":"datos recibidos"})

if  __name__ == '__main__':
    servidorWeb.run(debug = False, host = '0.0.0.0', port = '8080')


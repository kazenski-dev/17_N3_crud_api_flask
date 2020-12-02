from http import HTTPStatus
from __init__ import app
from service import StudentService
from flask import request, jsonify, Response

# - FUNCIONA  --------------------- FUNCAO MPEAMENTO 
@app.route("/") # mapear o recurso
def presentation():
    #retorno uma string que quero apresentar na tela
    return "Welcome to N3 - Crud using API with Python and Flask", HTTPStatus.OK

# - FUNCIONA  --------------------- FUNCAO SALVAR 
@app.route("/insert/student", methods=['POST']) #post para cadastrar
def save():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.save(received_data)
        return "Registro salvo com sucesso", HTTPStatus.CREATED
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO LISTAR TODOS 
@app.route("/list/all", methods=['GET']) #get sempre listagem
def list_all():

    try:
        list_it = StudentService()
        return jsonify(list_it.list_all())
       
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO LISTAR POR CPF
@app.route("/list/cpf", methods=['GET']) #get sempre listagem
def listar_by_cpf():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.list_by_id(received_data)
        return jsonify(person_service.list_by_id(received_data))
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO LISTAR POR EMAIL 
@app.route("/list/email", methods=['GET']) #get sempre listagem
def listar_by_email():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.list_by_email(received_data)
        return jsonify(person_service.list_by_email(received_data))
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO UPDATE NAME 
@app.route("/update/name", methods=['PUT']) #update
def update_by_name():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.update_name(received_data)
        return "NAME Update Finished", HTTPStatus.CREATED
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO UPDATE EMAIL 
@app.route("/update/email", methods=['PUT']) #update
def update_by_email():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.update_email(received_data)
        return "EMAIL Update Finished", HTTPStatus.CREATED
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

# - FUNCIONA  --------------------- FUNCAO EXCLUIR 
@app.route("/delete/student", methods=['DELETE'])
def delete_by_cpf():

    received_data = request.json
    if received_data is None:
        return "Invalid Json", HTTPStatus.BAD_REQUEST
    try:
        person_service = StudentService()
        person_service.delete(received_data)
        return "Delete Finished", HTTPStatus.CREATED
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

#---------------------------
if __name__ == "__main__":
    app.run(debug=True)
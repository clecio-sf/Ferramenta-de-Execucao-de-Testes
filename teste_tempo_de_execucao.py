from os import remove
from consultas_sql import *
from consultas_mongo_ref import *
from consultas_mongo_embedded import *
import mysql.connector
import pymongo
import timeit


def conecta_sql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="certificados2"
    )
    cursor = conn.cursor()

    return cursor, conn


def conecta_mongo():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    database = client['certificados']

    # substituir "participante_participacao" para a coluna que vai ser usada na consulta

    # para c1 utilizar mycol = database["evento"]
    # para c2 utilizar mycol = database["participante_participacao"]
    # para c3 utilizar mycol = database["atividade"]
    # para c4 utilizar mycol = database["participante_participacao"]
    # para c5 utilizar mycol = database["participante_participacao"]

    # para consultas mongo_embedded utilizar mycol = database["certificados"]
    mycol = database["evento"]

    return client, database, mycol


def teste_velocidade_sql():
    cursor, conn = conecta_sql()
    cursor.execute(c1_sql)

    # caso queira ver o resultado da consulta descomentar abaixo

    # for x in cursor:
    #     print(x)


def testa_sql():
    total_sql = []

    for i in range(6):
        inicio = timeit.default_timer()
        teste_velocidade_sql()
        fim = timeit.default_timer()
        total_sql.append(fim - inicio)

    total_sql.remove(max(total_sql)) and remove(min(total_sql))

    return total_sql


def teste_velocidade_mongo():
    cliente, database, mycol = conecta_mongo()
    mydoc = mycol.aggregate(c1_mongo_ref)

    # caso queira ver o resultado da consulta descomentar abaixo

    # for x in mydoc:
    #     print(x)


def testa_mongo():
    total_mongo = []

    for i in range(6):
        inicio = timeit.default_timer()
        teste_velocidade_mongo()
        fim = timeit.default_timer()
        total_mongo.append(fim - inicio)

    total_mongo.remove(max(total_mongo)) and remove(min(total_mongo))

    return total_mongo


if __name__ == '__main__':

    resultados_sql = testa_sql()
    resultados_mongo = testa_mongo()

    print(f'resultado SQL: {resultados_sql}')
    print(f'resultado Mongo: {resultados_mongo}')

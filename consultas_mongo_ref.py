# total de atividade por evento
c1_mongo_ref = [
    {'$lookup': {
        'from': 'atividade',
        'localField': 'id',
        'foreignField': 'evento_id',
        'as': 'atividade'
    }},
    {'$unwind': '$atividade'},
    {'$group': {
        '_id': '$id',
        'evento': {'$addToSet': {'$concat': ['$nome', ' - ', '$sigla']}},
        'total':{'$sum': 1}
    }},
    {'$unwind': '$evento'},
    {'$project': {'_id': 0}},
    {'$sort': {'total': -1}}
]

# total de participante por evento
c2_mongo_ref = [
    {'$lookup': {
        'from': 'evento',
        'localField': 'participacao.evento_id',
        'foreignField': 'id',
        'as': 'evento'
    }},
    {'$unwind': '$evento'},
    {'$group': {
        '_id': '$evento.id',
        'Evento': {'$addToSet': '$evento.nome'},
        'Total_Participante': {'$sum': 1}
    }},
    {'$unwind': '$Evento'},
    {'$project': {'_id': 0}},
    {'$sort': {'Total_Participante': -1}}
]

# Quais as atividade e os tipos de atividades de um evento
c3_mongo_ref = [
    {'$lookup': {
        'from': 'evento',
        'localField': 'evento_id',
        'foreignField': 'id',
        'as': 'evento'
    }},
    {'$lookup': {
        'from': 'tipo_funcao_atividade',
        'localField': 'tipo_atividade_id',
        'foreignField': 'id',
        'as': 'tipo_atividade'
    }},
    {'$unwind': '$evento'},
    {'$unwind': '$tipo_atividade'},
    {'$match': {'evento.sigla': 'Week-IT', 'evento.ano': '2019',
                'tipo_atividade.tipo': 'Tipo Atividade'}},
    {'$project': {'_id': 0, 'titulo': 1, 'id': 1,
                  'evento.ano': 1, 'tipo_atividade.nome': 1}},
    {'$sort': {'titulo': 1}}
]

# Total de certificados por evento
c4_mongo_ref = [
    {'$lookup': {
        'from': 'evento',
        'localField': 'participacao.evento_id',
        'foreignField': 'id',
        'as': 'evento'
    }},
    {'$unwind': '$participacao'},
    {'$group': {
        '_id': '$participacao.evento_id',
        'total': {'$sum': 1}
    }},
    {'$sort': {'total': -1}}
]

# Quais as atividade que um aluno X participou
c5_mongo_ref = [
    {'$match': {'dados_pessoais.CPF': '00000000002'}},
    {'$unwind': '$participacao'},
    {'$lookup': {
        'from': 'evento',
        'localField': 'participacao.evento_id',
        'foreignField': 'id',
        'as': 'evento'
    }},
    {'$group': {
        '_id': '$dados_pessoais.nome_completo',
        'nome': {'$addToSet': '$dados_pessoais.nome_completo'},
        'eventos': {'$push': "$evento.nome"}
    }},
    {'$unwind': '$nome'},
    {'$project': {'_id': 0}}
]

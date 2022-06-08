# total de atividade por evento
c1_mongo_embedded = [
    {'$unwind': '$participacao'},
    {'$group': {
        '_id': '$participacao.evento.id',
        'evento': {'$addToSet': '$participacao.evento.nome'},
        'atividades': {'$addToSet': '$participacao.atividade.titulo'},
    }},
    {'$unwind': '$evento'},
    {'$project': {
        'total': {'$size': '$atividades'}, 'evento': 1, '_id': 0
    }},
    {'$sort': {'total': -1}}
]

# total de participante por evento
c2_mongo_embedded = [
    {'$unwind': '$participacao'},
    {'$group': {
        '_id': '$participacao.evento.id',
        'evento': {'$addToSet': '$participacao.evento.nome'},
        'participantes': {'$addToSet': '$dados_pessoais.id'},
    }},
    {'$unwind': '$evento'},
    {'$project': {
        'total': {'$size': '$participantes'}, 'evento': 1, '_id': 0
    }},
    {'$sort': {'total': -1}}
]

# Quais as atividade e os tipos de atividades de um evento
c3_mongo_embedded = [
    {'$unwind': "$participacao"},
    {'$match': {'participacao.evento.sigla': 'Week-IT',
                'participacao.evento.ano': "2019"}},
    {'$group': {
        '_id': '$participacao.tipo_atividade.id',
        'titulo': {'$addToSet': '$participacao.atividade.titulo'},
        'ano': {'$addToSet': '$participacao.evento.ano'}
    }},
    {'$sort': {'titulo': 1}}
]

# Total de certificados por evento
c4_mongo_embedded = [
    {'$unwind': '$participacao'},
    {'$group': {
        '_id': '$participacao.evento.id',
        'evento': {'$addToSet': '$participacao.evento.nome'},
        'participantes': {'$push': '$dados_pessoais.id'},
    }},
    {'$unwind': '$evento'},
    {'$project': {
        'total': {'$size': '$participantes'}, 'evento': 1, '_id': 0
    }},
    {'$sort': {'total': -1}}
]

# Quais as atividade que um aluno X participou
c5_mongo_embedded = [
    {'$match': {'dados_pessoais.CPF': '00000000016'}},
    {'$unwind': '$participacao'},
    {'$group': {
        '_id': '$dados_pessoais.nome_completo',
        'evento': {'$push': {'$concat': ['$participacao.evento.nome', ' - ', '$participacao.evento.sigla', ' ano ', '$participacao.evento.ano']}},
        'total':{'$sum': 1}
    }},
    {'$sort': {'total': -1}}
]


# Total de atividades por evento
c1_sql = """
select CONCAT(evento.nome," (", evento.sigla, ")") Evento, evento.ano Ano, count(atividade.id) Total
from evento
join atividade on evento.id = atividade.evento_id
group by evento.id
order by Total desc
    """

# Total de participante por evento
c2_sql = """
SELECT CONCAT(c.nome," (", c.sigla, ")") Evento, c.ano, COUNT(DISTINCT participante_id) TotalParticipante
FROM participacao a 
join atividade b on a.atividade_id = b.id
join evento c on c.id = b.evento_id
group by a.evento_id
ORDER BY TotalParticipante DESC;
"""

# Quais as Atividades e os tipos de atividade de um Evento
c3_sql = """
SELECT b.titulo, b.id, c.nome, c.id
FROM evento a 
JOIN atividade b ON a.id = b.evento_id
JOIN tipo_atividade c ON c.id = b.tipo_atividade_id
WHERE a.sigla="week-it" AND a.ano=2019
ORDER BY b.titulo;
"""

# Total de Certificado por Evento
c4_sql = """
SELECT CONCAT(c.nome," (", c.sigla, ")") Evento, c.ano, COUNT(participante_id) TotalCertificado
FROM participacao a 
join atividade b on a.atividade_id = b.id
join evento c on c.id = b.evento_id
group by a.evento_id
ORDER BY TotalCertificado DESC;
"""

# Quais os eventos que um aluno x participou
c5_sql = """
SELECT participante.nome_completo, evento.nome
FROM participante
JOIN participacao ON participante.id = participacao.participante_id
JOIN atividade ON participacao.atividade_id = atividade.id
JOIN evento ON atividade.evento_id = evento.id
WHERE participante.cpf = '00000000002'
"""

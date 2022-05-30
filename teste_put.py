import requests

headers = {'Authorization': 'Token e96d404ffe092fd497ddd06fda65566e48c613e1'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com id 11
# curso = requests.get(url=f'{url_base_cursos}11/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}11/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP 200
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']

import requests

headers = {'Authorization': 'Token e96d404ffe092fd497ddd06fda65566e48c613e1'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url_base_cursos, headers=headers)
print(resultado.json())

# print(resultado.status_code)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 4

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação com JavaScript'

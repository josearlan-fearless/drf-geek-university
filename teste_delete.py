import requests

headers = {'Authorization': 'Token e96d404ffe092fd497ddd06fda65566e48c613e1'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(f'{url_base_cursos}11/', headers=headers)

# Testando o código HTTP 204
assert resultado.status_code == 204

# depois de deletar se tentar novamente retornará o código 404, não econtrado.
# print(resultado.text)

# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0

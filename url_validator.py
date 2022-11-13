import re


# cep_pattern = re.compile('[0-9]{5}[-]{1}?[0-9]{2}')
# search_cep_in_address = cep_pattern.search(address)

# if search_cep_in_address:
#     cep = search_cep_in_address.group()

#     print(cep)
# else:
#     raise(AttributeError('O endereço não tem CEP!'))

url = 'http://www.bytebank.com.br/cambio'

url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

url_matching_pattern = url_pattern.match(url)

print(url_matching_pattern)

if url_matching_pattern:
    print('Is valid')
else: 
    print('Is not valid')

# Para usar o manupulador de URL você deve usar a URL base: alxbank.com/cambio?dolar

from class_extractor import ManipulateURL

url_test  = ManipulateURL('bytebank.com/cambio?dolar=5&real=2&quantity=10&include_conversion=dolar')

get_url_test = url_test.convert_values()

print(get_url_test)

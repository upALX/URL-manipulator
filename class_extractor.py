import re
from decimal import Decimal
# url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'


class ManipulateURL:
    def __init__(self, external_url: str):
        self.url = self.clear_url(external_url)
        self.validate_url(external_url)

    def clear_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validate_url(self, external_url):
        if not self.url:
            raise ValueError("A URL não foi informada e está vazia!")

        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        url_validate_match_pattern = url_pattern.match(external_url)


        if url_validate_match_pattern is None:
            print('A URL está None!')
            raise(AttributeError('A URL informada não condiz com o padrão base! Você está colocando a URL mal digitada.'))

    def get_parameters_by_url(self):
        url = self.url
        url_flag_parameters = url.find('?')
        url_index_start_parameters = url[url_flag_parameters]
        url_array_divided_by_flag = url.split(url_index_start_parameters)
        url_parameters = url_array_divided_by_flag[1]
        return url_parameters

    def validate_key_name(self, key_name):
        url = self.url
        key_name_existent = url.find(key_name)

        if key_name_existent == -1:
            raise(KeyError('O key name informado não existe na URL!')) 
        if key_name.strip() == '':
            raise(KeyError('Você não está informando um key name para busca!'))
        if key_name.strip() == None:
            raise(AttributeError('O atributo informado não é suportado!'))

    def get_param_value_by_key_name(self, key_name: str):
        print('Passou no get param')
        key_name_stripped = key_name.strip()
        self.validate_key_name(key_name_stripped)
        index_number_at_key_name = self.url.find(key_name_stripped)
        get_value_param = index_number_at_key_name + len(key_name_stripped) + 1
        stopper = self.url.find('&', get_value_param)

        if stopper == -1:
            value_from_parameter =  self.url[get_value_param:]
        
        else:
            value_from_parameter = self.url[get_value_param:stopper]

        return value_from_parameter

    def set_add_parameter_in_url(self, parameter_name: str):
        url = self.url 
        new_url = []
        new_url.append(url+'&'+parameter_name)

        return new_url
    
    def convert_values(self):
        dolar_value_informated = self.get_param_value_by_key_name('dolar')
        real_value_informated = self.get_param_value_by_key_name('real')
        quantity = self.get_param_value_by_key_name('quantity')
        include_conversion = self.get_param_value_by_key_name('include_conversion')
        print(f'Real: {real_value_informated}. Dolar: {dolar_value_informated}. Quantity: {quantity}. Tipo: {include_conversion}')


        if include_conversion == 'dolar':
            real_value_converted_to_dolar = Decimal(dolar_value_informated) / Decimal(real_value_informated)
            print(f'O valor em dolares para a quantidade de {quantity} moedas em real a um preço de R$ {real_value_informated} é igual a: $ {real_value_converted_to_dolar}') 
        elif include_conversion == 'real':
            dolar_value_converted_to_real = Decimal(real_value_informated) * Decimal(dolar_value_informated)
            print(f'O valor em real de {real_value_informated} doláres a um preço de {dolar_value_informated} doláres é igual a {dolar_value_converted_to_real}')
        else:
            print('Os valores ou valor passado na URL está fora do padrão esperado!')

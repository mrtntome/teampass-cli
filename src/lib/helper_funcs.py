from json import dumps
from tabulate import tabulate
from base64 import urlsafe_b64encode
from io import BytesIO
from os.path import isfile
from sys import exit

def json_pp(response, indent=4):
    json_str = dumps(response.json(), indent=indent)
    print(json_str)
    return None

def table_pp(response, sensitive_fields=[], tablefmt='simple'):
    json_data = response.json()
    if type(json_data) is dict:
        table_rows = json_data.values()
    elif type(json_data) is list:
        table_rows = json_data
    for row in table_rows:
        for field in sensitive_fields:
            del row[field]
    table_str = tabulate(table_rows, headers='keys', tablefmt=tablefmt)
    print(f'{table_str}\n')
    return None

def bstream2file(response, filename):
    if isfile(filename):
        print('File already exists!!!')
        exit(1)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f'output saved to {filename}')

def encode_params(args, encoded_key='', params=[]):
    params_values = [args[param] for param in params]
    params_str = ';'.join(params_values)
    params_byte = urlsafe_b64encode(params_str.encode('ascii'))
    params_b64 = params_byte.decode('ascii')
    args[encoded_key] = params_b64
    return args

def b64encode_str(param):
    params_b64 = urlsafe_b64encode(param.encode('ascii')).decode('ascii')
    return params_b64
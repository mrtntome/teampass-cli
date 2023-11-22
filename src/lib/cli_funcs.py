from lib.teampass_api import teampass_api_get, teampass_api_post
from lib.helper_funcs import json_pp, table_pp, bstream2file, encode_params, b64encode_str

def list_folders(args):
    for arg in ['api_endpoint', 'api_key', 'user_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')

    response = teampass_api_get('read', 'userfolders', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        table_pp(response)
    return None

def list_items(args):
    for arg in ['api_endpoint', 'api_key', 'user_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    if (args["show_pw"] is False):
        sensitive_fields = ['pw']
    else:
        sensitive_fields = []
    response = teampass_api_get('read', 'userpw', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        table_pp(response, sensitive_fields=sensitive_fields)
    return None

# API is broken (see https://github.com/nilsteampassnet/TeamPass/issues/3006)
def list_files(args):
    for arg in ['api_endpoint', 'api_key', 'item_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    response = teampass_api_get('read', 'listfiles', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        table_pp(response)
    return None

# API is broken (see https://github.com/nilsteampassnet/TeamPass/issues/3006)
def download_file(args):
    for arg in ['api_endpoint', 'api_key', 'file_id', 'output']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    output_filename = args["output"]
    response = teampass_api_get('read', 'files', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        bstream2file(response, output_filename)
    return None

# API is broken, retrieves passwords from all folders instead of specified
def read_folder(args):
    for arg in ['api_endpoint', 'api_key', 'folder_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    if (args["show_pw"] is False):
        sensitive_fields = ['pw']
    else:
        sensitive_fields = []
    response = teampass_api_get('read', 'folder', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        table_pp(response, sensitive_fields=sensitive_fields)
    return None

def read_item(args):
    for arg in ['api_endpoint', 'api_key', 'item_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    if (args["show_pw"] is False):
        sensitive_fields = ['pw']
    else:
        sensitive_fields = []
    response = teampass_api_get('read', 'items', args)
    if 'err' in response.json():
        json_pp(response)
    else:
        table_pp(response, sensitive_fields=sensitive_fields)
    return None

def find_items(args):
    return None

def add_folder(args):
    for arg in ['api_endpoint', 'api_key', 'title', 'complexity_level', 'parent_id']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    args['renewal_period'] = '0'
    args['personal'] = '0'
    args = encode_params(args, encoded_key='folder_params_b64', params=['title', 'complexity_level', 'parent_id', 'renewal_period', 'personal'])
    response = teampass_api_get('add', 'folder', args)
    json_pp(response)
    return None

def add_item(args):
    for arg in ['api_endpoint', 'api_key', 'label', 'password', 'description', 'folder_id', 'login', 'email', 'url', 'tags', 'acm']:
        if (args[arg] is None):
            try:
                args[arg] = str(input(f'{arg}: '))
            except Exception as err:
                print(f'An error occurred: {err}')
    for arg in ['label', 'password', 'description', 'folder_id', 'login', 'email', 'url', 'tags', 'acm']:
        args[arg] = b64encode_str(args[arg])
    response = teampass_api_get('add', 'item', args)
    json_pp(response)
    return None

# Not Working, API functionality broken/not implemented
def add_file(args):
    return None

def update_folder(args):
    return None

def update_item(args):
    return None

def delete_folder(args):
    return None

def delete_item(args):
    return None


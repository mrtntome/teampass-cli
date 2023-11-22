from requests import get, post, HTTPError
from string import Template
from sys import exit

def teampass_api_get(action, target, args):
    master_template = Template('${api_endpoint}/api/index.php/${action_subtemplate}?apikey=${api_key}')
    # todo check action
    allowed_actions = ['read', 'find', 'add', 'update', 'delete']
    # todo check target
    allowed_targets = {
        'read'      : ['folder', 'items', 'userpw', 'userfolders', 'listfiles', 'files'],
        'find'      : ['item'],
        'add'       : ['item', 'folder'],
        'update'    : ['item', 'folder'],
        'delete'    : ['item', 'folder'],
    }
    # todo check args
    required_args = {
        ('read', 'folder')      : ['folder_id'],
        ('read', 'items')       : ['item_id'],
        ('read', 'userpw')      : ['user_id'],
        ('read', 'userfolders') : ['user_id'],
        ('read', 'listfiles')   : ['item_id'], 
        ('read', 'files')       : ['file_id'], 
        ('find', 'item')        : ['folder_id', 'search_str'],
        ('add', 'item')         : ['label', 'password', 'description', 'folder_id', 'login', 'email', 'url', 'tags', 'acm'],
        ('add', 'folder')       : ['folder_params_b64'],
        ('update', 'item')      : ['item_id', 'label', 'password', 'description', 'folder_id', 'login', 'email', 'url', 'tags', 'acm'],
        ('update', 'folder')    : ['folder_id', 'title', 'complexity_level', 'renewal_period'],
        ('delete', 'item')      : ['item_id'],
        ('delete', 'folder')    : ['folder_id'],
    }
    # this could be replaced with a more efficient data structure, eg. dataframe
    action_subtemplates = {
        ('read', 'folder')      : 'read/folder/${folder_id}',
        ('read', 'items')       : 'read/items/${item_id}',
        ('read', 'userpw')      : 'read/userpw/${user_id}',
        ('read', 'userfolders') : 'read/userfolders/${user_id}',
        ('read', 'listfiles')   : 'read/listfiles/${item_id}', 
        ('read', 'files')       : 'read/files/${file_id}', 
        ('find', 'item')        : 'find/item/${folder_id}/${search_str}',
        ('add', 'item')         : 'add/item/${label};${password};${description};${folder_id};${login};${email};${url};${tags};${acm}',
        ('add', 'folder')       : 'add/folder/${folder_params_b64}',
        ('update', 'item')      : 'update/item/${item_id}/${label};${password};${description};${folder_id};${login};${email};${url};${tags};${acm}',
        ('update', 'folder')    : 'update/folder/${folder_id}/${title};${complexity_level};${renewal_period}',
        ('delete', 'item')      : 'delete/item/${item_id}',
        ('delete', 'folder')    : 'delete/folder/${folder_id}',
    }
    url_template = Template(master_template.safe_substitute(action_subtemplate=action_subtemplates[action, target]))
    url = url_template.substitute(args)
    print(f'\nGET {url}\n')
    try:
        response = get(url, timeout=args['timeout'])
        response.raise_for_status()
    except Exception as err:
        print(f'An error occurred: {err}')
        exit(1)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        exit(1)
    return response

def teampass_api_post(action, target, args):
    master_template = Template('${api_endpoint}/api/index.php/${action_subtemplate}?apikey=${api_key}')
    allowed_actions = ['add']
    allowed_targets = {
        'add'   : ['file'],
    }
    required_args = {
        ('add', 'file')    : ['item_id', 'file', 'filename'],
    }
    action_subtemplates = {
        ('add', 'file')      : 'add/file',
    }
    url_template = Template(master_template.safe_substitute(action_subtemplate=action_subtemplates[action, target]))
    url = url_template.substitute(args)

    if (action=='add' and target=='file'):
        try:
            response = post(url, files=args, timeout=args['timeout'])
            response.raise_for_status()
        except Exception as err:
            print(f'An error occurred: {err}')
            exit(1)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            exit(1)
    return response
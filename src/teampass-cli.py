from argparse import ArgumentParser
from lib.cli_funcs import list_folders, list_items, list_files, download_file, read_folder, read_item, add_folder, add_item

def main():
    main_parser = ArgumentParser(prog='teampass-cli', description='Simple TeamPass command line client')
    subparsers = main_parser.add_subparsers(title='subcommands', dest='subparser')

    listfolders_parser = subparsers.add_parser('listfolders', help='list accessible folders')
    listfolders_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    listfolders_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    listfolders_parser.add_argument('--user-id', metavar='ID', dest='user_id', type=str, default=None, help='user id used to log in the webUI')
    listfolders_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    listfolders_parser.set_defaults(func=list_folders)

    listitems_parser = subparsers.add_parser('listitems', help='list accessible items')
    listitems_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    listitems_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    listitems_parser.add_argument('--user-id', metavar='ID', dest='user_id', type=str, default=None, help='user id used to log in the webUI')
    listitems_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    listitems_parser.add_argument('--show-pw', action='store_true', dest='show_pw', help='show passwords in the output')
    listitems_parser.set_defaults(func=list_items)

    listfiles_parser = subparsers.add_parser('listfiles', help='list files attached to item')
    listfiles_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    listfiles_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    listfiles_parser.add_argument('--item-id', metavar='ID', dest='item_id', type=str, default=None, help='id (not label) of the target item')
    listfiles_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    listfiles_parser.set_defaults(func=list_files)

    downloadfile_parser = subparsers.add_parser('downloadfile', help='download file attached to item')
    downloadfile_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    downloadfile_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    downloadfile_parser.add_argument('--file-id', metavar='ID', dest='file_id', type=str, default=None, help='id (not filename) of the target file')
    downloadfile_parser.add_argument('--output', metavar='FILENAME', dest='output', type=str, default=None, help='output file')
    downloadfile_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    downloadfile_parser.set_defaults(func=download_file)

    readfolder_parser = subparsers.add_parser('readfolder', help='read content of folder(s)')
    readfolder_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    readfolder_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    readfolder_parser.add_argument('--folder-id', metavar='ID', dest='folder_id', type=str, default=None, help='id (not name) of the target folder')
    readfolder_parser.add_argument('--output', metavar='FILENAME', dest='output', type=str, default=None, help='output file')
    readfolder_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    readfolder_parser.add_argument('--show-pw', action='store_true', dest='show_pw', help='show passwords in the output')
    readfolder_parser.set_defaults(func=read_folder)

    readfolder_parser = subparsers.add_parser('readitem', help='read content of folder(s)')
    readfolder_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    readfolder_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    readfolder_parser.add_argument('--item-id', metavar='ID', dest='item_id', type=str, default=None, help='id (not label) of the target item')
    readfolder_parser.add_argument('--output', metavar='FILENAME', dest='output', type=str, default=None, help='output file')
    readfolder_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    readfolder_parser.add_argument('--show-pw', action='store_true', dest='show_pw', help='show passwords in the output')
    readfolder_parser.set_defaults(func=read_item)

    addfolder_parser = subparsers.add_parser('addfolder', help='add a folder')
    addfolder_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    addfolder_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    addfolder_parser.add_argument('--title', metavar='TITLE', dest='title', type=str, default=None, help='title of the folder')
    addfolder_parser.add_argument('--complexity-level', metavar='N', dest='complexity_level', type=str, default='0', choices=['0', '25', '50', '60', '70', '80', '90'], help='required complexity level for passwords')
    addfolder_parser.add_argument('--parent-id', metavar='ID', dest='parent_id', type=str, default=None, help='id (not name) of parent folder')
    addfolder_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    addfolder_parser.set_defaults(func=add_folder)

    additem_parser = subparsers.add_parser('additem', help='add an item to a folder')
    additem_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    additem_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    additem_parser.add_argument('--label', metavar='LABEL', dest='label', type=str, default=None, help='label for the item')
    additem_parser.add_argument('--password', metavar='PASSWORD', dest='password', type=str, default=None, help='password field of entry')
    additem_parser.add_argument('--description', metavar='DESCRIPTION', dest='description', type=str, default=None, help='description of the item')
    additem_parser.add_argument('--folder-id', metavar='ID', dest='folder_id', type=str, default=None, help='id (not name) of parent folder')
    additem_parser.add_argument('--login', metavar='LOGIN', dest='login', type=str, default=None, help='login field of entry')
    additem_parser.add_argument('--email', metavar='EMAIL', dest='email', type=str, default=None, help='email field of entry')
    additem_parser.add_argument('--url', metavar='URL', dest='url', type=str, default=None, help='url field of entry')
    additem_parser.add_argument('--tags', metavar='TAG', dest='tags', type=str, default=None, help='space separated tags for the entry')
    additem_parser.add_argument('--acm', metavar='N', dest='acm', type=str, default='0', choices=['0', '1'], help='anyone can modify?')
    additem_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    additem_parser.set_defaults(func=add_item)

    # addfile_parser = subparsers.add_parser('addfile', help='attach file to an item')
    # addfile_parser.add_argument('--api-endpoint', metavar='URL', dest='api_endpoint', type=str, default=None, help='url of the API endpoint')
    # addfile_parser.add_argument('--api-key', metavar='KEY', dest='api_key', type=str, default=None, help='key obtained through the webUI')
    # addfile_parser.add_argument('--timeout', metavar='SECONDS', dest='timeout', type=int, default=20, help='wait time for the http response (default: 20)')
    # addfile_parser.set_defaults(func=add_file)

    parsed_args = main_parser.parse_args()
    if (parsed_args.subparser is None):
        main_parser.print_help()
        return None
    args_dict = vars(parsed_args)
    parsed_args.func(args_dict)
    return None

if __name__ == "__main__":
    main()
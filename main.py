import sys
import csv
import os

CLIENT_TALBE = '.cleints.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append (client_name)

    else:
        print('Client already is in client\'s list')


def _initialize_clients_from_storage():
    with open(CLIENT_TALBE, 'r' ) as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        
        for row in reader:
            clients.append(row)
            

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field
        
def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')
        
        if client_name == 'exit':
            client_name = None
            break
        

    if not client_name:
        sys.exit()
        
    return client_name


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TALBE)
    with open(tmp_table_name, mode = 'w') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clients)
        
        os.remove(CLIENT_TALBE)
        os.rename(tmp_table_name, CLIENT_TALBE)


def _add_comma():
    global clients
    clients +=','


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def _print_wellcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    

if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_wellcome()
    command = input()
    command = command.upper()
    
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
        
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the client name?')
    
        updated_client(client_name, updated_name)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client()
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list '.format(client_name))
    else:
        print('Invalid command')
        
    _save_clients_to_storage()    
        
    
    
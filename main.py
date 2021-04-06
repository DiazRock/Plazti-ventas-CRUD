clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients
    clients += client_name


def _add_comma():
    global clients
    clients +=','


def list_clients():
    global clients
    
    print(clients)


def _print_wellcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    

if __name__ == '__main__':
    list_clients()
    create_client('David')
    print(clients)
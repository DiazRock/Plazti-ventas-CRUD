import unittest
from pyunitreport import HTMLTestRunner
from clients.services import ClientService
from pv import CLIENT_TABLE
from clients.models import Client
import csv

class PVServicesTests(unittest.TestCase):
    
    def setUp(self):
        self.table_name = CLIENT_TABLE
        self.client_service = ClientService(self.table_name)
    
    def test_create_client(self):
        client_to_insert = Client(
            name='Alejandro',
            company='Home',
            email = 'a@a.com',
            position='boss',
            uid= 55
        )
        self.client_service.create_client(client_to_insert)
        with open(self.table_name, mode= 'r') as f:
            reader = csv.DictReader(f, fieldnames= Client.schema())
            l = list(reader)
            to_compare = vars(client_to_insert)
            to_compare['uid'] = str(to_compare['uid'])
            self.assertTrue ( dict (l[-1]), to_compare)

    def test_update_client(self):
        
        pass

    def test_list_client(self):
        
        pass

    def test_delete_client(self):
        
        pass
    
    def tearDown(self):
        pass
    
if __name__ == "__main__":
    unittest.main(verbosity = 2, 
                  testRunner= HTMLTestRunner(output= 'report', report_name='platzi-ventas-report'))
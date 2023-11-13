from model.da.database import DatabaseManager
from model.entity.user import *
from model.entity.invoice import Invoice


class InvoiceDa(DatabaseManager):
    def find_by_customer_name(self,name):
        self.make_engine()
        return self.session.query(Invoice).filter(Customer.name == name)



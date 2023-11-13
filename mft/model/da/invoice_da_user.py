from mysqlx import *
from sqlalchemy import *
from sqlalchemy.orm import *

from mft.model.da.database import DatabaseManager
from mft.model.entity.invoice_user import Invoice


class User:
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    family = Column(String)
    gender = Column(String)
    role = Column(String)
    score = Column(Integer)
    username = Column(String)
    password = Column(String)
    user_id = Column(Integer, ForeignKey = "user.id")

    user = relationship("User")


class InvoiceDa(DatabaseManager):
    def find_by_customer_name(self,name):
        self.make_engine()
        return self.session.query(Invoice).filter(User.name == name)



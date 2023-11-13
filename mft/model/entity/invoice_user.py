from sqlalchemy import Column, Integer, String, ForeignKey

from mft.model.entity.base import Base
from sqlalchemy.orm import relationship


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customer.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")

    def __repr__(self):
        return str(self.__dict__)

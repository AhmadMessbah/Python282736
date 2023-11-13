from mft.model.da.database import DatabaseManager
from mft.model.entity.rent import Rent

from sqlalchemy import between


class RentDa(DatabaseManager):
    def find_by_sender_code(self,sender_code):
        pass
    
    
    def find_by_renter_code(self,renter_code):
        pass
    
    
    def find_by_stuff_code(self,stuff_code):
        pass
    
    
    def find_by_rent_date_range(self,start_date, end_date):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent.rent_date, start_date,end_date))
        self.session.close()
        return result
    
    
    def find_by_return_date_range(self,start_date, end_date):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent.return_date, start_date, end_date))
        self.session.close()
        return result
    
    
    def find_by_rent_price_range(self,start_price, end_price):
        self.make_engine()
        result = self.session.query(Rent).filter(between(Rent.rent_price, start_price, end_price))
        self.session.close()
        return result
    
    
    def find_by_information(self,information):
        self.make_engine()
        result = self.session.query(Rent).filter(Rent.information.like(information))
        self.session.close()
        return result
    
    
    def find_by_rent_status(self,rent_status):
        pass

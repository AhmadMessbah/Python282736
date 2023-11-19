import time

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import text, and_, or_, between

from mft.model.entity.base import Base

from sqlalchemy.orm import sessionmaker

import sqlalchemy_utils
from sqlalchemy_utils import database_exists, create_database


class DatabaseManager:
    def make_engine(self):
        if not database_exists('mysql+pymysql://root:root123@localhost:3306/rent_db'):
            create_database('mysql+pymysql://root:root123@localhost:3306/rent_db')
        self.engine = create_engine('mysql+pymysql://root:root123@localhost:3306/rent_db')

        # Create Tables
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def save(self, entity):
        self.make_engine()
        entity = self.session.add()
        self.session.commit()
        self.session.close()
        return entity

    def edit(self, entity):
        self.make_engine()
        entity = self.session.merge(entity)
        self.session.commit()
        self.session.close()
        return entity

    def remove(self, entity):
        self.make_engine()
        entity = self.session.delete(entity)
        self.session.commit()
        self.session.close()
        return entity

    def find_all(self, class_name):
        self.make_engine()
        entity_list = self.session.query(class_name).all()
        self.session.close()
        return entity_list

    def find_by_code(self, class_name, code):
        self.make_engine()
        entity = self.session.get(class_name, code)
        self.session.close()
        return entity

    def find_by_name(self, class_name, name):
        self.make_engine()
        entity = self.session.get(class_name, name)
        self.session.close()
        return entity

    def find_by_family(self, class_name, family):
        self.make_engine()
        entity = self.session.get(class_name, family)
        self.session.close()
        return entity

    def find_by_score(self, class_name, score):
        self.make_engine()
        entity = self.session.get(class_name, score)
        self.session.close()
        return entity

    def find_by_username(self, class_name, username):
        self.make_engine()
        entity = self.session.get(class_name, username)
        self.session.close()
        return entity

    def find_by_role(self, class_name, role):
        self.make_engine()
        entity = self.session.get(class_name, role)
        self.session.close()
        return entity

    def find_by_gender(self, class_name, gender):
        self.make_engine()
        entity = self.session.get(class_name, gender)
        self.session.close()
        return entity

    def find_by_age(self, class_name, age):
        self.make_engine()
        entity = self.session.get(class_name,age)
        self.session.close()
        return entity

    def find_by_status(self, class_name, status):
        self.make_engine()
        entity = self.session.get(class_name,status)
        self.session.close()
        return entity

    def find_by_email(self, class_name, email):
        self.make_engine()
        entity = self.session.get(class_name,email)
        self.session.close()
        return entity

    def find_by_state(self, class_name, state):
        self.make_engine()
        entity = self.session.get(class_name, state)
        self.session.close()
        return entity

    def find_by_city(self, class_name, city):
        self.make_engine()
        entity = self.session.get(class_name, city)
        self.session.close()
        return entity

    def find_by_phone(self, class_name, phone):
        self.make_engine()
        entity = self.session.get(class_name, phone)
        self.session.close()
        return entity

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    name = Column(String, nullable=False)
    equipments = relationship('Equipment', backref='owner')


class EquipmentModel(Base):
    __tablename__ = 'equipment_models'

    name = Column(String, primary_key=True)
    max_term_of_use_in_days = Column(Integer, nullable=False)


class Equipment(Base):
    __tablename__ = 'equipment'

    inventory_number = Column(String, primary_key=True)
    model_name = Column(String, ForeignKey('equipment_models.name'))
    term_of_use_in_days = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

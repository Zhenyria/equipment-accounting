from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    name = Column(String, primary_key=True, nullable=False)

    def __init__(self, name):
        self.name = name


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    department_name = Column(String, ForeignKey('departments.name'))
    name = Column(String, nullable=False)
    equipments = relationship('Equipment', backref='owner')

    def __init__(self, name, department_name, equipments=None):
        self.name = name
        self.department_name = department_name
        self.equipments = equipments or []


class EquipmentModel(Base):
    __tablename__ = 'equipment_models'

    name = Column(String, primary_key=True)
    max_term_of_use_in_days = Column(Integer, nullable=False)

    def __init__(self, name, max_term_of_use_in_days):
        self.name = name
        self.max_term_of_use_in_days = max_term_of_use_in_days


class Equipment(Base):
    __tablename__ = 'equipments'

    inventory_number = Column(String, primary_key=True)
    model_name = Column(String, ForeignKey('equipment_models.name'), nullable=False)
    start_of_using = Column(DATE, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    def __init__(self, inventory_number, model_name, start_of_using):
        self.inventory_number = inventory_number
        self.model_name = model_name
        self.start_of_using = start_of_using

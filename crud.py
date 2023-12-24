from sqlalchemy.orm import Session

import models


class DepartmentOperations:
    @staticmethod
    def create(db: Session, department: models.Department):
        db.add(department)
        db.commit()
        db.refresh(department)
        return department

    @staticmethod
    def get(db: Session, name: str):
        return db.query(models.Department).filter(models.Department.name == name).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(models.Department).all()


class UserOperations:
    @staticmethod
    def create(db: Session, user: models.User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


class EquipmentModelOperations:
    @staticmethod
    def create(db: Session, equipment_model: models.EquipmentModel):
        db.add(equipment_model)
        db.commit()
        db.refresh(equipment_model)
        return equipment_model

    @staticmethod
    def get_all(db: Session):
        return db.query(models.EquipmentModel).all()


class Equipment:
    @staticmethod
    def create(db: Session, equipment: models.Equipment):
        db.add(equipment)
        db.commit()
        db.refresh(equipment)
        return equipment

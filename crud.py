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

    @staticmethod
    def remove(db: Session, name: str):
        department = DepartmentOperations.get(db, name)
        if department is not None:
            db.delete(department)
            db.commit()


class UserOperations:
    @staticmethod
    def create(db: Session, user: models.User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all_by_department_name(db: Session, department_name: str):
        return db.query(models.User).filter(models.User.department_name == department_name).all()

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

from sqlalchemy import text, Date
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
    def get_all(db: Session):
        return db.query(models.User).all()

    @staticmethod
    def get(db: Session, id: int):
        return db.query(models.User).filter(models.User.id == id).first()

    @staticmethod
    def get_all_by_department_name(db: Session, department_name: str):
        return db.query(models.User).filter(models.User.department_name == department_name).all()

    @staticmethod
    def remove(db: Session, id: int):
        user = UserOperations.get(db, id)
        if user is not None:
            if len(user.equipments) > 0:
                raise ValueError(f"Невозможно удалить пользователя {id}, так как за ним закреплено оборудование")
            db.delete(user)
            db.commit()


class EquipmentModelOperations:

    @staticmethod
    def create(db: Session, equipment_model: models.EquipmentModel):
        db.add(equipment_model)
        db.commit()
        db.refresh(equipment_model)
        return equipment_model

    @staticmethod
    def get(db: Session, name: str):
        return db.query(models.EquipmentModel).filter(models.EquipmentModel.name == name).first()

    @staticmethod
    def get_all(db: Session):
        return db.query(models.EquipmentModel).all()

    @staticmethod
    def remove(db: Session, name: str):
        equipment_model = EquipmentModelOperations.get(db, name)
        if equipment_model is not None:
            related_equipments = EquipmentOperations.get_all_by_model_name(db, name)
            if len(related_equipments) > 0:
                raise ValueError(
                    f"Невозможно удалить наименование {name}, так как с данным наименованим найдено оборудование"
                )
            db.delete(equipment_model)
            db.commit()


class EquipmentOperations:
    @staticmethod
    def create(db: Session, equipment: models.Equipment):
        db.add(equipment)
        db.commit()
        db.refresh(equipment)
        return equipment

    @staticmethod
    def get(db: Session, inventory_number: str):
        return db.query(models.Equipment).filter(models.Equipment.inventory_number == inventory_number).first()

    @staticmethod
    def get_all_by_model_name(db: Session, model_name: str):
        return db.query(models.Equipment).filter(models.Equipment.model_name == model_name).all()

    @staticmethod
    def get_expired(db: Session):
        return (db.query(models.Equipment)
                .join(models.EquipmentModel, models.Equipment.name == models.EquipmentModel.model_name)
                .filter((models.Equipment.start_of_using
                         + text("interval '1 day'")
                         * models.EquipmentModel.max_term_of_use_in_days) > Date).all())

    @staticmethod
    def set_owner(db: Session, inventory_number: str, user_id: int):
        equipment = EquipmentOperations.get(db, inventory_number)
        if equipment is not None:
            equipment.user_id = user_id
            db.commit()
        else:
            raise ValueError(f"Оборудование {inventory_number} не найдено")

    @staticmethod
    def remove(db: Session, inventory_number: str):
        equipment = EquipmentOperations.get(db, inventory_number)
        if equipment is not None:
            db.delete(equipment)
            db.commit()

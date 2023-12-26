from datetime import date

import database
from crud import DepartmentOperations, UserOperations, EquipmentModelOperations, EquipmentOperations
from dto import convert_to_dtos
from models import Department, User, EquipmentModel, Equipment


class DepartmentService:

    @staticmethod
    def create(name: str):
        with database.get_session() as session:
            if DepartmentService.get(name) is not None:
                raise ValueError(f"Департамент '{name}' уже существует")
            return DepartmentOperations.create(session, Department(name)).name

    @staticmethod
    def get(name: str):
        with database.get_session() as session:
            return DepartmentOperations.get(session, name)

    @staticmethod
    def get_all():
        with database.get_session() as session:
            return [department.name for department in DepartmentOperations.get_all(session)]

    @staticmethod
    def remove(name: str):
        relates_users = UserService.get_all_by_department(name)
        if len(relates_users) != 0:
            raise ValueError(f"Департамент {name} имеет связанных пользователей и не может быть удалён")

        with database.get_session() as session:
            DepartmentOperations.remove(session, name)


class UserService:

    @staticmethod
    def create(name: str, department_name: str):
        with database.get_session() as session:
            if DepartmentService.get(department_name) is None:
                raise ValueError(f"Департамент {department_name} не найден")
            return UserOperations.create(session, User(name=name, department_name=department_name))

    @staticmethod
    def get_all(ids: list[int] = None):
        with database.get_session() as session:
            return UserOperations.get_all(session, ids)

    @staticmethod
    def get_all_by_department(department_name: str):
        with database.get_session() as session:
            return UserOperations.get_all_by_department_name(session, department_name)

    @staticmethod
    def remove(id: int):
        with database.get_session() as session:
            UserOperations.remove(session, id)


class EquipmentModelService:
    @staticmethod
    def create(name: str, max_term_of_use_in_days: int):
        if EquipmentModelService.get(name) is not None:
            raise ValueError(f"Модель оборудования {name} уже существует")
        with database.get_session() as session:
            EquipmentModelOperations.create(session, EquipmentModel(name, max_term_of_use_in_days))

    @staticmethod
    def get(name: str):
        with database.get_session() as session:
            return EquipmentModelOperations.get(session, name)

    @staticmethod
    def get_all(names: list[str] = None):
        with database.get_session() as session:
            return EquipmentModelOperations.get_all(session, names)

    @staticmethod
    def remove(name: str):
        with database.get_session() as session:
            return EquipmentModelOperations.remove(session, name)


class EquipmentService:
    @staticmethod
    def create(inventory_number: str, model_name: str):
        equipment_model = EquipmentModelService.get(model_name)
        if equipment_model is None:
            raise ValueError(f"Модель оборудования {model_name} не найдена")
        with database.get_session() as session:
            return EquipmentOperations.create(session, Equipment(inventory_number, model_name, date.today()))

    @staticmethod
    def get_all():
        with database.get_session() as session:
            equipments = EquipmentOperations.get_all(session)
            equipments_models_names = [equipment.model_name for equipment in equipments]
            users_ids = []
            for equipment in equipments:
                user_id = equipment.user_id
                if user_id is not None:
                    users_ids.append(user_id)
            return convert_to_dtos(equipments,
                                   EquipmentModelService.get_all(equipments_models_names),
                                   UserService.get_all(users_ids))

    @staticmethod
    def get_expired():
        with database.get_session() as session:
            equipments = EquipmentOperations.get_expired(session)
            equipments_models_names = [equipment.model_name for equipment in equipments]
            users_ids = []
            for equipment in equipments:
                user_id = equipment.user_id
                if user_id is not None:
                    users_ids.append(user_id)
            return convert_to_dtos(equipments,
                                   EquipmentModelService.get_all(equipments_models_names),
                                   UserService.get_all(users_ids))

    @staticmethod
    def set_owner(inventory_number: str, user_id: int):
        found_users = UserService.get_all([user_id])
        if len(found_users) == 0:
            raise ValueError(f"User with id {user_id} does not exist")
        with database.get_session() as session:
            EquipmentOperations.set_owner(session, inventory_number, user_id)

    @staticmethod
    def remove_owner(inventory_number: str):
        with database.get_session() as session:
            EquipmentOperations.remove_owner(session, inventory_number)

    @staticmethod
    def remove(inventory_number: str):
        with database.get_session() as session:
            EquipmentOperations.remove(session, inventory_number)

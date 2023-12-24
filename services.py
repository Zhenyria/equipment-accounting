import database
from crud import DepartmentOperations, UserOperations, EquipmentModelOperations
from models import Department, User, EquipmentModel


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
    def get_all():
        with database.get_session() as session:
            return UserOperations.get_all(session)

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
            return EquipmentModelOperations.create(session, EquipmentModel(name, max_term_of_use_in_days))

    @staticmethod
    def get(name: str):
        with database.get_session() as session:
            return EquipmentModelOperations.get(session, name)

    @staticmethod
    def get_all():
        with database.get_session() as session:
            return EquipmentModelOperations.get_all(session)

    @staticmethod
    def remove(name: str):
        with database.get_session() as session:
            return EquipmentModelOperations.remove(session, name)


class EquipmentService:
    @staticmethod
    def create(inventory_number: str, model_name: int):
        return 0  # TODO

    @staticmethod
    def get_all():
        return 0  # TODO

    @staticmethod
    def get_expired():
        return 0  # TODO

    @staticmethod
    def set_owner(inventory_number: str, user_id: int):
        return 0  # TODO

    @staticmethod
    def remove(inventory_number: str):
        return 0  # TODO

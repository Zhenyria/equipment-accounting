import database
from crud import DepartmentOperations, UserOperations
from models import Department, User


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


class UserService:

    @staticmethod
    def create(name: str, department_name: str):
        with database.get_session() as session:
            if DepartmentService.get(department_name) is None:
                raise ValueError(f"Департамент {department_name} не найден")
            return UserOperations.create(session, User(name=name, department_name=department_name))

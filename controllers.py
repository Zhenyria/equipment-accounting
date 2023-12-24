from services import DepartmentService, UserService

department_service = DepartmentService()
user_service = UserService()


class DepartmentController:

    @staticmethod
    def create(name: str):
        return department_service.create(name)

    @staticmethod
    def get_all():
        return department_service.get_all()


class UserController:

    @staticmethod
    def create(name: str, department_name: str):
        return user_service.create(name, department_name).id

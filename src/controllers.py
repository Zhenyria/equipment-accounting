from services import DepartmentService, UserService, EquipmentService, EquipmentModelService

department_service = DepartmentService()
user_service = UserService()
equipment_model_service = EquipmentModelService()
equipment_service = EquipmentService()


class DepartmentController:

    @staticmethod
    def create(name: str):
        return department_service.create(name)

    @staticmethod
    def get_all():
        return department_service.get_all()

    @staticmethod
    def remove(name: str):
        department_service.remove(name)
        return f"Департамент {name} успешно удалён"


class UserController:

    @staticmethod
    def create(name: str, department_name: str):
        return user_service.create(name, department_name).id

    @staticmethod
    def get_all():
        return [{"id": user.id, "name": user.name, "department_name": user.department_name}
                for user
                in user_service.get_all()]

    @staticmethod
    def remove(id: int):
        user_service.remove(id)
        return f"Пользователь {id} успешно удалён"


class EquipmentModelController:
    @staticmethod
    def create(name: str, max_term_of_use_in_days: int):
        equipment_model_service.create(name, max_term_of_use_in_days)

    @staticmethod
    def get_all():
        return [equipment_model.name for equipment_model in equipment_model_service.get_all()]

    @staticmethod
    def remove(name: str):
        equipment_model_service.remove(name)
        return f"Модель оборудования {name} успешно удалена"


class EquipmentController:
    @staticmethod
    def create(inventory_number: str, model_name: str):
        return equipment_service.create(inventory_number, model_name)

    @staticmethod
    def get_all():
        return equipment_service.get_all()

    @staticmethod
    def get_expired():
        return equipment_service.get_expired()

    @staticmethod
    def set_owner(inventory_number: str, user_id: int):
        equipment_service.set_owner(inventory_number, user_id)
        return f"Оборудование {inventory_number} передано пользователю {user_id}"

    @staticmethod
    def remove(inventory_number: str):
        equipment_service.remove(inventory_number)
        return f"Оборудование {inventory_number} успешно удалено"

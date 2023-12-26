from datetime import date, timedelta

from models import Equipment, EquipmentModel, User


class EquipmentDto:
    inventory_number: str
    model_name: str
    start_of_using: date
    is_expired: bool
    user_id: int
    user_name: str

    def __init__(self,
                 inventory_number: str,
                 model_name: str,
                 start_of_using: date,
                 is_expired: bool,
                 user_id: int,
                 user_name: str):
        self.inventory_number = inventory_number
        self.model_name = model_name
        self.start_of_using = start_of_using
        self.is_expired = is_expired
        self.user_id = user_id
        self.user_name = user_name


def convert_to_dtos(equipments: list[Equipment], equipments_models: list[EquipmentModel], users: list[User]):
    max_terms_of_use_in_days_by_model_names = {equipments_model.name: equipments_model.max_term_of_use_in_days
                                               for equipments_model
                                               in equipments_models}

    users_by_ids = {user.id: user.name for user in users}

    dtos = []
    for equipment in equipments:
        model_name = equipment.model_name
        start_of_using = equipment.start_of_using

        is_expired = (start_of_using
                      + timedelta(days=max_terms_of_use_in_days_by_model_names[model_name])
                      < date.today())

        user_id = equipment.user_id
        user_name = users_by_ids[user_id] if equipment.user_id else None

        dtos.append(EquipmentDto(equipment.inventory_number,
                                 model_name,
                                 start_of_using,
                                 is_expired,
                                 user_id,
                                 user_name))

    return dtos

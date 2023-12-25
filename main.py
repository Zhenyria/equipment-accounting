import tkinter as tk

from database import create_tables
from views import DepartmentView, UserView, EquipmentModelView

department_view = DepartmentView()
user_view = UserView()
equipment_model_view = EquipmentModelView()


def main():
    create_tables()

    window = tk.Tk()

    def on_click_create_department_view():
        department_view.create_view()

    def on_click_show_departments_view():
        department_view.get_all_view()

    def on_click_create_user_view():
        user_view.create_view()

    def on_click_show_users_view():
        user_view.get_all_view()

    def on_click_create_equipment_model_view():
        equipment_model_view.create_view()

    def on_click_show_equipment_models_view():
        equipment_model_view.get_all_view()

    departments_label = tk.Label(window, text="Департаменты")
    departments_label.pack(padx=4, pady=4)

    create_department_button = tk.Button(window, text="Создать департамент", command=on_click_create_department_view)
    create_department_button.pack(padx=4, pady=4)

    show_all_departments_button = tk.Button(window, text="Список департаментов", command=on_click_show_departments_view)
    show_all_departments_button.pack(padx=4, pady=4)

    users_label = tk.Label(window, text="Пользователи")
    users_label.pack(padx=4, pady=4)

    create_user_button = tk.Button(window, text="Создать пользователя", command=on_click_create_user_view)
    create_user_button.pack(padx=4, pady=4)

    show_all_users_button = tk.Button(window, text="Список пользователей", command=on_click_show_users_view)
    show_all_users_button.pack(padx=4, pady=4)

    equipment_model_label = tk.Label(window, text="Модели оборудования")
    equipment_model_label.pack(padx=4, pady=4)

    create_equipment_model_button = tk.Button(window,
                                              text="Создать модель оборудования",
                                              command=on_click_create_equipment_model_view)
    create_equipment_model_button.pack(padx=4, pady=4)

    show_all_equipment_model_button = tk.Button(window,
                                                text="Список моделей оборудования",
                                                command=on_click_show_equipment_models_view)
    show_all_equipment_model_button.pack(padx=4, pady=4)

    window.mainloop()


if __name__ == "__main__":
    main()

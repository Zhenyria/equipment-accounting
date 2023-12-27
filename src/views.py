# views.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import controllers

department_controller = controllers.DepartmentController()
user_controller = controllers.UserController()
equipment_model_controller = controllers.EquipmentModelController()
equipment_controller = controllers.EquipmentController()


class DepartmentView:
    @staticmethod
    def create_view():
        window = tk.Tk()

        name_label = tk.Label(window, text="Имя департамента")
        name_label.pack(padx=4, pady=4)

        name_entry = tk.Entry(window)
        name_entry.pack(padx=4, pady=4)

        def create_department():
            name = name_entry.get()
            if name == '':
                show_error_window("Имя департамента не может быть пустым")
                return

            try:
                created_department_name = department_controller.create(name)
                show_success_window(f"Департамент {created_department_name} создан")
                window.destroy()
            except ValueError as e:
                show_error_window(str(e))

        button = tk.Button(window, text="Создать департамент", command=create_department)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        departments = department_controller.get_all()

        def remove_department(frame, department_name):
            try:
                response_message = department_controller.remove(department_name)
                show_success_window(response_message)
                frame.destroy()
            except ValueError as e:
                show_error_window(str(e))

        def create_line(department_name):
            frame = tk.Frame(window)
            frame.pack()

            label = tk.Label(frame, text=str(department_name))
            label.pack(side=tk.LEFT, padx=4, pady=4)

            button = tk.Button(frame, text="Удалить", command=lambda: remove_department(frame, department_name))
            button.pack(side=tk.LEFT, padx=4, pady=4)

        for department in departments:
            create_line(department)

        window.mainloop()


class UserView:

    @staticmethod
    def create_view():
        window = tk.Tk()

        # User name
        user_name_label = tk.Label(window, text="Имя пользователя")
        user_name_label.pack(padx=4, pady=4)

        user_name_field = tk.Entry(window)
        user_name_field.pack(padx=4, pady=4)

        # Department
        department_label = tk.Label(window, text="Департамент")
        department_label.pack(padx=4, pady=4)

        departments_names = department_controller.get_all()

        department_field = tk.StringVar(window)
        department_ddl = ttk.Combobox(window, textvariable=department_field, values=list(departments_names))
        department_ddl.pack(padx=4, pady=4)

        def create_user():
            user_name = user_name_field.get()

            if user_name == "":
                show_error_window("Имя пользователя не может быть пустым")
                return

            department_name = department_field.get()

            try:
                user_id = user_controller.create(user_name, department_name)
                show_success_window(f"Пользователь {user_id} успешно создан")
                window.destroy()
            except ValueError as e:
                show_error_window(str(e))

        button = tk.Button(window, text="Создать пользователя", command=create_user)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        users = user_controller.get_all()

        def remove_user(frame, user_id: int):
            try:
                response_message = user_controller.remove(user_id)
                show_success_window(response_message)
                frame.destroy()
            except ValueError as e:
                show_error_window(str(e))

        def create_line(user_data):
            frame = tk.Frame(window)
            frame.pack()

            label = tk.Label(frame, text=f"{user_data['department_name']}, {user_data['name']}")
            label.pack(side=tk.LEFT, padx=4, pady=4)

            button = tk.Button(frame,
                               text="Удалить",
                               command=lambda: remove_user(frame, user_data["id"]))
            button.pack(side=tk.LEFT, padx=4, pady=4)

        for user in users:
            create_line(user)

        window.mainloop()


class EquipmentModelView:

    @staticmethod
    def create_view():
        window = tk.Tk()

        equipment_name_label = tk.Label(window, text="Название оборудования")
        equipment_name_label.pack(padx=4, pady=4)

        equipment_name_entry = tk.Entry(window)
        equipment_name_entry.pack(padx=4, pady=4)

        equipment_max_term_of_use_in_days_label = tk.Label(window, text="Срок службы оборудования")
        equipment_max_term_of_use_in_days_label.pack(padx=4, pady=4)

        equipment_max_term_of_use_in_days_entry = tk.Entry(window)
        equipment_max_term_of_use_in_days_entry.pack(padx=4, pady=4)

        def create_equipment():
            equipment_name = equipment_name_entry.get()

            if equipment_name == '':
                show_error_window("Название оборудования не может быть пустым")
                return

            equipment_max_term_of_use_in_days = equipment_max_term_of_use_in_days_entry.get()

            if equipment_max_term_of_use_in_days == '':
                show_error_window("Максимальный срок использования оборудования не может быть пустым")
                return

            try:
                equipment_model_controller.create(equipment_name, int(equipment_max_term_of_use_in_days))
                show_success_window(f"Модель оборудования {equipment_name} создана")
                window.destroy()
            except ValueError as e:
                show_error_window(str(e))

        button = tk.Button(window, text="Создать модель оборудования", command=create_equipment)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        equipment_models_names = equipment_model_controller.get_all()

        def remove_equipment_model(frame, equipment_model_name):
            try:
                response_message = equipment_model_controller.remove(equipment_model_name)
                show_success_window(response_message)
                frame.destroy()
            except ValueError as e:
                show_error_window(str(e))

        def create_line(equipment_model):
            frame = tk.Frame(window)
            frame.pack()

            label = tk.Label(frame, text=equipment_model)
            label.pack(side=tk.LEFT, padx=4, pady=4)

            button = tk.Button(frame, text="Удалить", command=lambda: remove_equipment_model(frame, equipment_model))
            button.pack(side=tk.LEFT, padx=4, pady=4)

        for equipment_model_name in equipment_models_names:
            create_line(equipment_model_name)

        window.mainloop()


class EquipmentView:

    @staticmethod
    def create_view():
        window = tk.Tk()

        # Inventory number
        inventory_number_label = tk.Label(window, text="Инвентарный номер")
        inventory_number_label.pack(padx=4, pady=4)

        inventory_number_entry = tk.Entry(window)
        inventory_number_entry.pack(padx=4, pady=4)

        # Equipment model
        equipment_model_label = tk.Label(window, text="Модель оборудования")
        equipment_model_label.pack(padx=4, pady=4)

        equipment_models = equipment_model_controller.get_all()

        equipment_model_field = tk.StringVar(window)
        equipment_model_ddl = ttk.Combobox(window, textvariable=equipment_model_field, values=list(equipment_models))
        equipment_model_ddl.pack(padx=4, pady=4)

        def on_click():
            inventory_number = inventory_number_entry.get()
            equipment_model = equipment_model_field.get()
            try:
                equipment_controller.create(inventory_number, equipment_model)
                show_success_window(
                    f"Оборудование {equipment_model} с инвентарным номером {inventory_number} зарегистрировано"
                )
            except ValueError as e:
                show_error_window(str(e))

        button = tk.Button(window, text="Создать оборудование", command=on_click)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        equipments = equipment_controller.get_all()
        for equipment in equipments:
            frame = tk.Frame(window)  # TODO: fix removing. variables scope is other in python
            frame.pack()

            owner_name = equipment.user_name
            is_expired = equipment.is_expired
            label = tk.Label(frame,
                             text=f"{equipment.model_name} {equipment.inventory_number}. "
                                  f"Ответственный: {owner_name if owner_name is not None else 'отсутствует'}"
                                  f"{'. Подлежит замене' if is_expired else ''}",
                             fg="red" if is_expired else "black")
            label.pack(side=tk.LEFT, padx=4, pady=4)

            # TODO: update list after change
            change_owner_button = tk.Button(
                frame,
                text="Изменить ответственного",
                command=lambda inventory_number=equipment.inventory_number: EquipmentView.change_owner(inventory_number)
            )
            change_owner_button.pack(side=tk.LEFT, padx=4, pady=4)

            def remove_owner(inventory_number):
                try:  # TODO
                    equipment_controller.remove_owner(inventory_number)
                    show_success_window("Ответственный удален")
                    label.config(text=f"{equipment.model_name} {equipment.inventory_number}. "
                                      "Ответственный: отсутствует"
                                      f"{'. Подлежит замене' if is_expired else ''}",
                                 fg="red" if is_expired else "black")
                except ValueError as e:
                    show_error_window(str(e))

            remove_owner_button = tk.Button(
                frame,
                text="Удалить ответственного",
                command=lambda inventory_number=equipment.inventory_number: remove_owner(inventory_number)
            )
            remove_owner_button.pack(side=tk.LEFT, padx=4, pady=4)

            def remove(inventory_number):
                try:
                    response_message = equipment_controller.remove(inventory_number)
                    show_success_window(response_message)
                    frame.destroy()
                except ValueError as e:
                    show_error_window(str(e))

            remove_button = tk.Button(
                frame,
                text="Удалить",
                command=lambda inventory_number=equipment.inventory_number: remove(inventory_number)
            )
            remove_button.pack(side=tk.LEFT, padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def change_owner(inventory_number: str):
        window = tk.Tk()

        frame = tk.Frame(window)
        frame.pack()

        users = user_controller.get_all()

        users_ids_by_names_with_indexes = {f"{user['name']} ({user['id']})": user['id'] for user in users}

        user_field = tk.StringVar(window)
        users_ddl = ttk.Combobox(window, textvariable=user_field, values=list(users_ids_by_names_with_indexes.keys()))
        users_ddl.pack(padx=4, pady=4)

        def on_click():
            selected_user = user_field.get()

            if selected_user == "":
                show_error_window("Выберите пользователя")

            selected_user_id = users_ids_by_names_with_indexes[selected_user]
            try:
                response_message = controllers.EquipmentController.set_owner(inventory_number, int(selected_user_id))
                show_success_window(response_message)
            except ValueError as e:
                show_error_window(str(e))

        submit_button = tk.Button(frame, text="Изменить ответственного", command=on_click)
        submit_button.pack(side=tk.LEFT, padx=4, pady=4)


def show_success_window(message: str):
    messagebox.showinfo("Успешно", message)


def show_error_window(error_message: str):
    messagebox.showerror("Ошибка", error_message)

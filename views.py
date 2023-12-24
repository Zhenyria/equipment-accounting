# views.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import controllers

department_controller = controllers.DepartmentController()
user_controller = controllers.UserController()


class DepartmentView:
    @staticmethod
    def create_view():
        window = tk.Tk()

        name_label = tk.Label(window, text="Имя департамента")
        name_label.pack(padx=4, pady=4)

        name_entry = tk.Entry(window)
        name_entry.pack(padx=4, pady=4)

        def on_click():
            name = name_entry.get()
            try:
                created_department_name = department_controller.create(name)
                messagebox.showinfo("Успешно", f"Департамент {created_department_name} создан")
            except ValueError as e:
                messagebox.showinfo("Ошибка", message=str(e))

        button = tk.Button(window, text="Создать департамент", command=on_click)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        departments = department_controller.get_all()
        for department in departments:
            frame = tk.Frame(window)
            frame.pack()

            label = tk.Label(frame, text=str(department))
            label.pack(side=tk.LEFT, padx=4, pady=4)

            def on_click(department_name):
                try:
                    response_message = department_controller.remove(department_name)
                    messagebox.showinfo("Успешно", message=response_message)
                    frame.destroy()
                except ValueError as e:
                    messagebox.showinfo("Ошибка", message=str(e))

            button = tk.Button(frame,
                               text="Удалить",
                               command=lambda department_name=department: on_click(department_name))
            button.pack(side=tk.LEFT, padx=4, pady=4)

        window.mainloop()


class UserView:

    @staticmethod
    def create_view():
        window = tk.Tk()

        # User name
        name_label = tk.Label(window, text="Имя пользователя")
        name_label.pack(padx=4, pady=4)

        name_field = tk.Entry(window)
        name_field.pack(padx=4, pady=4)

        # Department
        dep_label = tk.Label(window, text="Департамент")
        dep_label.pack(padx=4, pady=4)

        departments_names = department_controller.get_all()

        department_field = tk.StringVar(window)
        department_ddl = ttk.Combobox(window, textvariable=department_field, values=list(departments_names))
        department_ddl.pack(padx=4, pady=4)

        def on_click():
            name = name_field.get()
            department_name = department_field.get()

            try:
                user_id = user_controller.create(name, department_name)
                messagebox.showinfo("Выполнено", f"Пользователь {user_id} успешно создан")
            except ValueError as e:
                messagebox.showinfo("Ошибка", message=str(e))

        button = tk.Button(window, text="Создать пользователя", command=on_click)
        button.pack(padx=4, pady=4)

        window.mainloop()

    @staticmethod
    def get_all_view():
        window = tk.Tk()

        users = user_controller.get_all()
        for user in users:
            frame = tk.Frame(window)  # TODO: fix removing
            frame.pack()

            label = tk.Label(frame, text=f"{user['department_name']}, {user['name']}")
            label.pack(side=tk.LEFT, padx=4, pady=4)

            def on_click(user_id):
                try:
                    response_message = user_controller.remove(user_id)
                    messagebox.showinfo("Успешно", message=response_message)
                except ValueError as e:
                    messagebox.showinfo("Ошибка", message=str(e))
                finally:
                    frame.destroy()

            button = tk.Button(frame,
                               text="Удалить",
                               command=lambda user_id=user["id"]: on_click(user_id))
            button.pack(side=tk.LEFT, padx=4, pady=4)

        window.mainloop()

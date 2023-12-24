import tkinter as tk

from database import create_tables
from views import DepartmentView, UserView

department_view = DepartmentView()
user_view = UserView()


def main():
    create_tables()

    window = tk.Tk()

    def on_click_create_department_view():
        department_view.create_department_view()

    def on_click_show_departments_view():
        department_view.get_all_departments_view()

    def on_click_create_user_view():
        user_view.create_user()

    tk.Label(window, text="Департаменты")

    create_department_button = tk.Button(window, text="Создать департамент", command=on_click_create_department_view)
    create_department_button.pack(padx=4, pady=4)

    show_all_departments_button = tk.Button(window, text="Список департаментов", command=on_click_show_departments_view)
    show_all_departments_button.pack(padx=4, pady=4)

    tk.Label(window, text="Пользователи")

    create_user_button = tk.Button(window, text="Создать пользователя", command=on_click_create_user_view)
    create_user_button.pack(padx=4, pady=4)

    window.mainloop()


if __name__ == "__main__":
    main()

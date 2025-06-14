import tkinter as tk
from tkinter import filedialog

class NotepadApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Блокнот")
        self.window.geometry("500x400")

        # Текстовое поле
        self.text_area = tk.Text(self.window, width=60, height=20, font=("Arial", 14))
        self.text_area.pack(pady=10)

        # Стек для хранения удалённых символов
        self.deleted_chars = []

        # Меню
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Выход", command=self.window.quit)

        # Кнопки для удаления и восстановления символов
        self.delete_button = tk.Button(self.window, text="Удалить", width=20, height=2, font=("Arial", 14), command=self.delete_char)
        self.delete_button.pack(pady=5)

        self.undo_button = tk.Button(self.window, text="Вернуть", width=20, height=2, font=("Arial", 14), command=self.undo_delete)
        self.undo_button.pack(pady=5)

        self.window.mainloop()

    def delete_char(self):
        # Удаляем последний символ и сохраняем его в стек
        current_text = self.text_area.get("1.0", tk.END)[:-1]  # Получаем весь текст без последнего символа
        if current_text:
            deleted_char = current_text[-1]  # Берём последний символ
            self.deleted_chars.append(deleted_char)  # Сохраняем его в стек
            self.text_area.delete("1.0", tk.END)  # Очищаем текстовое поле
            self.text_area.insert("1.0", current_text[:-1])  # Вставляем оставшийся текст

    def undo_delete(self):
        # Восстанавливаем последний удалённый символ
        if self.deleted_chars:
            last_deleted = self.deleted_chars.pop()  # Берём последний удалённый символ
            current_text = self.text_area.get("1.0", tk.END)
            self.text_area.delete("1.0", tk.END)  # Очищаем текстовое поле
            self.text_area.insert("1.0", current_text[:-1] + last_deleted)  # Вставляем его обратно

    def open_file(self):
        # Открыть файл
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)  # Очищаем текстовое поле
                self.text_area.insert("1.0", content)  # Вставляем содержимое файла

    def save_file(self):
        # Сохранить файл
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)  # Сохраняем содержимое текстового поля в файл

NotepadApp()
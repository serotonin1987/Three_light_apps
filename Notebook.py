import tkinter as tk
from tkinter import filedialog

class NotepadApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Блокнот")
        self.window.geometry("500x400")

        self.text_area = tk.Text(self.window, width=60, height=20, font=("Arial", 14))
        self.text_area.pack(pady=10)

        self.deleted_chars = []

        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Выход", command=self.window.quit)

        self.delete_button = tk.Button(self.window, text="Удалить", width=20, height=2, font=("Arial", 14), command=self.delete_char)
        self.delete_button.pack(pady=5)

        self.undo_button = tk.Button(self.window, text="Вернуть", width=20, height=2, font=("Arial", 14), command=self.undo_delete)
        self.undo_button.pack(pady=5)

        self.window.mainloop()

    def delete_char(self):
        current_text = self.text_area.get("1.0", tk.END)[:-1]
        if current_text:
            deleted_char = current_text[-1]
            self.deleted_chars.append(deleted_char)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", current_text[:-1])

    def undo_delete(self):
        if self.deleted_chars:
            last_deleted = self.deleted_chars.pop()
            current_text = self.text_area.get("1.0", tk.END)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", current_text[:-1] + last_deleted)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)

NotepadApp()

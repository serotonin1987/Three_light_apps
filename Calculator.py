import tkinter as tk

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        
        # Устанавливаем размер окна (ширина x высота)
        self.window.geometry("400x500")

        self.entry = tk.Entry(self.window, width=30, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("X", 5, 0)  # Кнопка для удаления последнего символа
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_click(x)
            tk.Button(self.window, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col)

        self.window.mainloop()

    def on_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Ошибка")
        elif char == "X":
            # Удаляем последний символ
            current_text = self.entry.get()
            self.entry.delete(len(current_text)-1, tk.END)
        else:
            self.entry.insert(tk.END, char)

CalculatorApp()
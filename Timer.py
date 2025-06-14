import tkinter as tk

class TimerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Таймер")
        self.window.geometry("500x600")  # Увеличим высоту окна

        # Переменные для хранения времени
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        # Метка для отображения времени
        self.time_label = tk.Label(self.window, text="00:00:00", font=("Arial", 30))
        self.time_label.pack(pady=20)

        # Поля для ввода времени
        self.hours_entry_label = tk.Label(self.window, text="Часы:", font=("Arial", 14))
        self.hours_entry_label.pack(pady=5)
        self.hours_entry = tk.Entry(self.window, font=("Arial", 14), width=10)
        self.hours_entry.pack(pady=5)

        self.minutes_entry_label = tk.Label(self.window, text="Минуты:", font=("Arial", 14))
        self.minutes_entry_label.pack(pady=5)
        self.minutes_entry = tk.Entry(self.window, font=("Arial", 14), width=10)
        self.minutes_entry.pack(pady=5)

        self.seconds_entry_label = tk.Label(self.window, text="Секунды:", font=("Arial", 14))
        self.seconds_entry_label.pack(pady=5)
        self.seconds_entry = tk.Entry(self.window, font=("Arial", 14), width=10)
        self.seconds_entry.pack(pady=5)

        # Кнопки
        self.start_button = tk.Button(self.window, text="Старт", width=20, height=2, font=("Arial", 14), command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.window, text="Стоп", width=20, height=2, font=("Arial", 14), command=self.stop_timer)
        self.stop_button.pack(pady=5)

        self.resume_button = tk.Button(self.window, text="Продолжить", width=20, height=2, font=("Arial", 14), command=self.resume_timer)
        self.resume_button.pack(pady=5)

        self.reset_button = tk.Button(self.window, text="Сброс", width=20, height=2, font=("Arial", 14), command=self.reset_timer)
        self.reset_button.pack(pady=5)

        self.is_running = False

        self.window.mainloop()

    def update_time(self):
        if self.is_running:
            # Обновляем отображаемое время
            time_str = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
            self.time_label.config(text=time_str)

            # Проверяем, если время истекло, останавливаем таймер
            if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
                self.stop_timer()
                return

            # Уменьшаем время
            self.seconds -= 1
            if self.seconds < 0:
                self.seconds = 59
                self.minutes -= 1
                if self.minutes < 0:
                    self.minutes = 59
                    self.hours -= 1

            # Запланировать следующий вызов
            self.window.after(1000, self.update_time)

    def start_timer(self):
        # Получаем значения из полей ввода
        try:
            self.hours = int(self.hours_entry.get())  # Часы
            self.minutes = int(self.minutes_entry.get())  # Минуты
            self.seconds = int(self.seconds_entry.get())  # Секунды
        except ValueError:
            self.hours = self.minutes = self.seconds = 0

        if self.hours >= 0 and self.minutes >= 0 and self.seconds >= 0:
            self.is_running = True
            self.update_time()

    def stop_timer(self):
        self.is_running = False

    def resume_timer(self):
        if not self.is_running and (self.hours > 0 or self.minutes > 0 or self.seconds > 0):
            self.is_running = True
            self.update_time()

    def reset_timer(self):
        self.is_running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time_label.config(text="00:00:00")

        # Очищаем поля ввода
        self.hours_entry.delete(0, tk.END)
        self.minutes_entry.delete(0, tk.END)
        self.seconds_entry.delete(0, tk.END)

# Запуск
TimerApp()
class Calculator:
    def __init__(self):
        self.history = []
    def calculate(self, a, b, operation):
        if operation == "+":
            res = a + b
        elif operation == "-":
            res = a - b
        elif operation == "*":
            res = a * b
        elif operation == "/":
            if b == 0:
                return "Грешка: Деление на нула!"
            res = a / b
        else:
            return "Невалидна операция!"
        self.history.append(f"{a} {operation} {b} = {res}")
        return res
    def get_summary(self):
        if not self.history:
            return "Няма извършени изчисления."
        return f"Общ брой операции досега: {len(self.history)}"
    def clear_history(self):
        self.history.clear()
        return "Историята беше изтрита успешно."
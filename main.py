from models import Calculator
import os

def main():
    calc = Calculator()
    while True:
        print("\n=== КАЛКУЛАТОР ===")
        print("1. Изчисление")
        print("2. Преглед на историята")
        print("3. Статистика и изчистване")
        print("4. Изход")
        choice = input("Изберете опция (1-4): ")
        if choice == "1":
            try:
                num1 = float(input("Въведете първо число: "))
                op = input("Изберете операция (+, -, *, /): ")
                num2 = float(input("Въведете второ число: "))
                result = calc.calculate(num1, num2, op)
                print(f"\n>>> РЕЗУЛТАТ: {result}")
            except ValueError:
                print("\n!!! Грешка: Моля въвеждайте само числа.")
        elif choice == "2":
            print("\n--- ИСТОРИЯ НА ИЗЧИСЛЕНИЯТА ---")
            if not calc.history:
                print("Историята е празна.")
            else:
                for entry in calc.history:
                    print(f" • {entry}")
        elif choice == "3":
            print(f"\n{calc.get_summary()}")
            confirm = input("Желаете ли да изчистите историята? (y/n): ")
            if confirm.lower() == 'y':
                print(calc.clear_history())
        elif choice == "4":
            print("Вие затворихте калкулатора.")
            break
        else:
            print("Невалиден избор, опитайте пак.")
if __name__ == "__main__":
    main()
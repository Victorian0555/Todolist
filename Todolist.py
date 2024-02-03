from datetime import date

def create_todo_list():
    current_date = date.today()
    tasks = []
    print("Введите задачи (для завершения введите пустую строку):")
    while True:
        task = input()
        if not task:
            break
        tasks.append(task)
    filename = f"todo_list_{current_date}.txt"
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Файл {filename} успешно создан!")

if __name__ == "__main__":
    create_todo_list()
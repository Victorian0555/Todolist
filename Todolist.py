from datetime import date

def create_todo_list():
    current_date = date.today().strftime("%Y-%m-%d")
    tasks = []
    print("- - - - - - TO - DO - LIST - - - - - -")
    print("Введите задачи (для завершения введите пустую строку):")
    while True:
        task = input()
        if not task:
            break
        tasks.append(task)
    filename = f"todo_list_{current_date}.txt"
    with open(filename, "w") as file:
        file.write("- - - - - - TO - DO - LIST - - - - - -\n")
        for i, task in enumerate(tasks, 1):
            file.write(f"{i}. {task}\n")
    print(f"Файл {filename} успешно создан!")

if __name__ == "__main__":
    create_todo_list()

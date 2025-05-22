from collections import deque
import time

def process_tasks(tasks):
    print(f"Запуск задач в: {time.strftime('%H:%M:%S')}")
    while tasks:
        task_name, timed = tasks.popleft()        # .popleft удаляет и возвращает 1 элемент из очереди
        start_time = time.strftime('%H:%M:%S')
        print(f"Начало обработки задачи: {task_name} в {time.strftime('%H:%M:%S')}")
        time.sleep(timed)  # Имитация выполнения задачи (остановка кода)
        print(f"Задача {task_name} завершена в {time.strftime('%H:%M:%S')}")
        time.sleep(3)           # время между выполнениями задач, сек
    print("Все задачи завершены.")

# Создаем очередь задач: (имя задачи, время выполнения)
tasks = deque([("Открыть глаза", 2),("Позавтракать", 3),("Почистить зубы", 1),("Закрыть глаза", 2),])

process_tasks(tasks)
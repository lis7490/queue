from collections import deque
import time

def process_tasks(tasks):
    print(f"Запуск задач в: {time.strftime('%H:%M:%S')}")
    while tasks:
        task_name, timed = tasks.popleft()        # .popleft удаляет и возвращает 1 элемент из очереди
        start_time = time.strftime('%H:%M:%S')
        print(f"Начало обработки задачи '{task_name}' в {start_time}, длительность {timed} сек")     # тут .popleft возвращает первый элемент из очереди
        time.sleep(timed)  # Имитация выполнения задачи (остановка кода)
    print("Все задачи завершены.")

# Создаем очередь задач: (имя задачи, время выполнения)
tasks = deque([("Задача 1", 2),("Задача 2", 3),("Задача 3", 1),("Задача 4", 2),])

process_tasks(tasks)
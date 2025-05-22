from collections import deque
import time


queue = deque()

# Enqueue — добавление задач
queue.append("Помыть посуду")
queue.append("Почитать книгу")
queue.append("Написать код")

# Dequeue — обработка задач
start_time = time.strftime('%H:%M:%S')
print(f"Запуск задач в {start_time}")
while queue:
    task = queue.popleft()  # Извлекаем первую задачу
    time1 = 2
    print(f"Выполняется задача: {task}, начало выполнения: {time.strftime('%H:%M:%S')}, время выполнения {time1} сек")
    time.sleep(time1)
print("Все задачи завершены")
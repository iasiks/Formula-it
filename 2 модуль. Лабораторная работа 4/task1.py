import datetime
from typing import Optional, List

class Task:
    """
    Базовый класс для описания общих свойств задач

    Атрибуты:
    title (str): Название задачи
    due_date (datatime): Срок выполнения задачи
    description (str): Описание задачи
    _is_completed (bool): Указывает выполнена ли задача
    """

    def __init__(self, title: str, due_date: datetime, description: str) -> None:
        self.title = title
        self._due_date = due_date # Инкапсуляция: дедлайн задачи не должен изменяться напрямую.
        self.description = description
        self._is_completed = False # Инкапсуляция: статус задачи не должен изменяться напрямую.

    @property
    def due_date(self)->datetime:
        return self._due_date
    @due_date.setter
    def due_date(self,new_date: datetime):
        if not isinstance(new_date,datetime):
            raise ValueError("Дедлайн должен быть указан в формате datetime(год, месяц, число)")
        self._due_date = new_date

    @property
    def is_completed(self) -> bool:
        """
        Возвращает статус выполнения задачи.
            bool: True, если задача выполнена, иначе False.
        """
        return self._is_completed


    def mark_completed(self) -> None:
        """
        Отмечает задачу как выполненную.
        """
        self._is_completed = True

    def update_description(self, new_description: str) -> None:
        """
        Обновляет описание задачи.

        Аргументы:
        new_description (str): Новое описание задачи.
        """
        self.description = new_description

    def __str__(self) -> str:
        return f"Задача:{self.title}. Срок выполнения задачи: {self.due_date}. Описание задачи: {self.description}. Статус задачи: {self.is_completed}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title={self.title!r}, due_date={self.due_date!r}, description={self.description!r})"

class PersonalTask(Task):
    """
    Дочерний класс для установки личных задач

    Атрибуты:
        priority (int): Приоритет задачи (1 - низкий, 2 - средний, 3 - высокий).
        reminder_time (Optional[datetime]): Время напоминания о задаче.
    """

    def __init__(self, title: str, due_date: datetime, description:str,  priority: int = 1, reminder_time:Optional [datetime] = None) -> None:
        """
        Конструктор класса PersonalTask.

        Аргументы:
            title (str): Название задачи.
            due_date (datetime): Срок выполнения задачи.
            description (str): Описание задачи
            priority (int, optional): Приоритет задачи. По умолчанию 1.
            reminder_time (Optional[datetime], optional): Время напоминания. По умолчанию None.
        """
        super().__init__(title, due_date,description)
        self.priority = priority
        self._reminder_time = reminder_time #Инкапсуляция: время напоминания не должно изменяться напрямую.

    @property
    def reminder_time(self) -> Optional [datetime]:
        return self._reminder_time

    @reminder_time.setter
    def reminder_time(self, value: datetime) -> None:
        """
        Устанавливает время напоминания.

        Аргументы:
            value (datetime): Новое время напоминания.
        """
        if not isinstance(value, datetime):
            raise ValueError("Время напоминания должно быть указано в формате datetime(год, месяц, число)")
        if value > self.due_date:
            raise ValueError("Время напоминания не может быть позже срока выполнения задачи")
        self._reminder_time = value

    def __str__(self) -> str:
        """Перегружает метод __str__ для добавления информации о приоритете."""
        base_str = super().__str__()
        return f"{base_str}. Приоритет:{self.priority}"

    def __repr__(self) -> str:
        """Перегружает метод __repr__ для добавления информации о приоритете."""
        return f"{self.__class__.__name__}(title={self.title!r}, due_date={self.due_date!r}, description={self.description!r}, priority={self.priority!r})"

    def reschedule(self, new_due_date: datetime) -> None:
        """
        Переносит срок выполнения задачи.

        Аргументы:
            new_due_date (datetime): Новый срок выполнения задачи.
        """
        self.due_date = new_due_date



class WorkTask(Task):
    """
    Дочерний класс для представления рабочей задачи.

    Атрибуты:
        project_name (str): Название проекта, к которому относится задача.
        assigned_to (List[str]): Список сотрудников, назначенных на задачу.
    """
    def __init__(self, title: str, due_date: datetime, description: str, project_name: str, assigned_to: List[str]) -> None:
        super().__init__(title,due_date,description)
        self.project_name = project_name
        self.assigned_to = assigned_to

    def assign_to_user(self,user:str) -> None:
        """
        Назначает задачу на сотрудника.

        Аргументы:
            user (str): Имя сотрудника.
        """
        self.assigned_to.append(user)

    def generate_report(self) -> str:
        """
        Генерирует отчет по задаче.

        Возвращает:
            str: Отчет в виде строки.
        """
        return f"Задача: {self.title}, Проект: {self.project_name}, Назначена: {', '.join(self.assigned_to)}"

    def __str__(self) -> str:
        """Перегружает метод __str__ для добавления информации о проекте."""
        base_str = super().__str__()
        return f"{base_str}, Проект: {self.project_name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title={self.title!r}, due_date={self.due_date!r}, description={self.description!r}, project_name={self.project_name!r}, assigned_to={self.assigned_to!r})"

    def mark_complete(self) -> None:
        """
        Перегружает метод mark_complete для добавления логики уведомления.
        Причина перегрузки: необходимо уведомить всех назначенных сотрудников о завершении задачи.
        """
        super().mark_completed()
        print(f"Задача '{self.title}' выполнена. Уведомление отправлено: {', '.join(self.assigned_to)}")


if __name__ == "__main__":
    personal_task = PersonalTask("Купить продукты", datetime.datetime(2025,2,14), "Хлеб,молоко,яйца", 2)
    print(personal_task)
    print(repr(personal_task))
    personal_task.mark_completed()
    print(personal_task.is_completed)

    work_task = WorkTask("Написать отчет", datetime.datetime(2024, 12, 25), "Описание отчета", "Проект X", ["Иван", "Мария"])
    print(work_task)
    print(repr(work_task))
    work_task.mark_complete()
    work_task.update_description("Обновленное описание отчета")
    print(work_task.description)
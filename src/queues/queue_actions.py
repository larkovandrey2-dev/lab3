from typing import Any, Protocol

from src.queues.list_queue import ListQueue
from src.queues.linked_queue import LinkedQueue
from src.queues.stacks_queue import StacksQueue


class QueueInterface(Protocol):
    def enqueue(self, value: Any) -> None: ...
    def dequeue(self) -> Any: ...
    def front(self) -> Any: ...
    def is_empty(self) -> bool: ...
    def __len__(self) -> int: ...


QUEUES: dict[str, type] = {
    "list": ListQueue,
    "linked": LinkedQueue,
    "stackq": StacksQueue,
}


def queue_action(queue: QueueInterface, action: str, value=None) -> Any:
    """
        Выполняет действие над очередью на основе переданной команды.

        Args:
            queue (QueueInterface): Объект очереди, реализующий QueueInterface.
            action (str): Название действия ('enqueue', 'dequeue', 'front', 'size', 'empty').
            value (Any, optional): Значение для добавления (только для 'enqueue'). По умолчанию None.

        Returns:
            Any: Результат выполнения действия (элемент очереди, размер, булево значение).

        Raises:
            ValueError: Если для 'enqueue' не передано значение или если передана неизвестная команда.
        """
    if action == "enqueue":
        if value is None:
            raise ValueError("enqueue требует аргумент")
        queue.enqueue(value)
        return f"enqueue({value})"

    if action == "dequeue":
        return queue.dequeue()

    if action == "front":
        return queue.front()

    if action == "size":
        return len(queue)

    if action == "empty":
        return queue.is_empty()

    raise ValueError(f"Неизвестная команда: {action}")

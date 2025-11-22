from typing import Any, Protocol

from src.stacks.list_stack import Stack
from src.stacks.queue_stack import QueueStack
from src.stacks.linked_stack import LinkedStack


class StackInterface(Protocol):
    def push(self, value: Any) -> None: ...
    def pop(self) -> Any: ...
    def peek(self) -> Any: ...
    def is_empty(self) -> bool: ...
    def __len__(self) -> int: ...


STACKS: dict[str, type] = {
    "list": Stack,
    "deque": QueueStack,
    "linked": LinkedStack,
}


def stack_action(stack: StackInterface, action: str, value=None) -> Any:
    if action == "push":
        if value is None:
            raise ValueError("push требует аргумент")
        stack.push(value)
        return f"push({value})"

    if action == "pop":
        return stack.pop()

    if action == "peek":
        return stack.peek()

    if action == "size":
        return len(stack)

    if action == "empty":
        return stack.is_empty()

    raise ValueError(f"Неизвестная команда: {action}")

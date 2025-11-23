import unittest
from src.stacks.stacks_actions import STACKS
from src.queues.queue_actions import QUEUES


class TestStructures(unittest.TestCase):

    def test_stack(self):
        for s_name in STACKS:
            s = STACKS[s_name]()
            s.push(1)
            s.push(2)
            self.assertEqual(s.peek(), 2)
            self.assertEqual(s.pop(), 2)
            self.assertEqual(len(s), 1)

    def test_queue(self):
        for q_name in QUEUES:
            q = QUEUES[q_name]()
            q.enqueue(1)
            q.enqueue(2)
            self.assertEqual(q.dequeue(), 1)
            self.assertEqual(q.front(), 2)

    def test_empty_errors(self):
        for s_name in STACKS:
            s = STACKS[s_name]()
            with self.assertRaises(ValueError):
                s.pop()
            with self.assertRaises(ValueError):
                s.peek()

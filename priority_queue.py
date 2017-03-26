""""Implement a priority queue in python3.
"""


import heapq
from itertools import count


class Task(dict):
    pass


class PriorityQueue:
    """Queue with priority."""

    removed = 'removed'

    def __init__(self):
        self._count = count()
        self.queue = []
        self._task_entry = {}

    def pop(self):
        while self.queue:
            task = heapq.heappop(self.queue)[-1]
            if task is not self.__class__.removed:
                # 删除注册信息
                del self._task_entry[task['name']]
                return task

        raise KeyError('Pop from an empty queue!')

    def remove(self, name):
        entry = self._task_entry.pop(name)
        entry[-1] = self.__class__.removed

    def push(self, task, priority=0):
        if 'name' not in task:
            raise KeyError('Task has no name!')

        if task['name'] in self._task_entry:
            raise KeyError('Task exists!')

        # 优先使用task指定的priority
        if 'priority' in task:
            priority = task['priority']

        # 创建唯一的index, 维持堆的稳定性
        index = next(self._count)

        # priority越大，代表优先级越高，由于heapq使用最小堆，所以此处存入队列的优先级取负数
        entry = [-priority, index, task]

        # 注册task
        self._task_entry[task['name']] = entry

        heapq.heappush(self.queue, entry)

    def __str__(self):
        s = []
        s.append('Priority queue:')
        for entry in sorted(self.queue):
            if entry[-1] != self.__class__.removed:
                s.append('<task:%s, priority:%s>' % (str(entry[-1]), -entry[0]))
        if len(s) == 1:
            return s[0] + '[]'
        return '\n'.join(s)

if __name__ == '__main__':
    pqueue = PriorityQueue()

    try:
        pqueue.pop()
    except KeyError as e:
        print(e)

    task1 = Task(name='mysql', job='store data')
    pqueue.push(task1, 1)
    print('Add task1:')
    print(pqueue)
    print('*'*20)

    task2 = Task(name='python', job='write backend code', priority=3)
    pqueue.push(task2)
    print('Add task2:')
    print(pqueue)
    print('*'*20)

    print('Add same name task:')
    task3 = Task(name='python', job='data analyse')
    try:
        pqueue.push(task3)
    except KeyError as e:
        print(e)
    print(pqueue)
    print('*'*20)

    print('Pop from queue:')
    task = pqueue.pop()
    print(str(task))
    print('*'*20)

    print('Remove task1')
    pqueue.remove('mysql')
    print(pqueue)



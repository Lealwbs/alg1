class Task:
    def __init__(self, start_time: float, end_time: float):
        self.start: float = start_time
        self.end: float = end_time 

    def getDuration(self):
        return self.end - self.start

class Scheduler:
    def __init__(self) -> None:
        self.tasks: dict[int:Task] = dict()
        self.ids: set[int] = set()

    def __str__(self) -> str:
        result: str = f"# Scheduler of Tasks object #"
        for id in self.ids:
            task: Task = self.tasks[id]
            result += f"\nTask {id}: {task.start}s - {task.end}s"
        return result

    def empty(self) -> bool:
        return self.size == 0

    def size(self) -> int:
        return len(self.ids)
    
    def get_free_id(self, given_id: int) -> int:
        if given_id not in set and given_id >= 0:
            return given_id
        
        for potential_id in range(self.size() + 1):
            if potential_id not in self.ids:
                return potential_id

    def add_task(self, start_time: float, end_time: float, id: int = -1) -> int:
        task: Task = Task(start_time=start_time, end_time=end_time)
        if task.getDuration() <= 0:
            return None
        
        id = self.get_free_id(id)
        self.ids.add(id)
        self.tasks[id] = task
        return id

    def remove_task(self, id) -> tuple[float, float]:
        task: Task = self.tasks.pop(id)
        self.ids.remove(id)
        return (task.start, task.end)

    def find_conflict(self, actual_id) -> set[int]:
        conflict_ids: set[int] = set()
        actual_task: Task = self.tasks[actual_id]
        for other_id in self.ids:
            if actual_id == other_id: continue
            other_task: Task = self.tasks[other_id]
            if (other_task.start < actual_task.start < other_task.end ) \
            or (other_task.start < actual_task.end < other_task.end):
                conflict_ids.add(other_id)
        return conflict_ids
        #     s        e
        #     #########
        # #######   ########
        # s     e   s      e


    def schedule_tasks(self) -> list[int]:
        pass
        # Algorithm TaskSchedule(T):
        # Input: A set T of tasks, such that each task has a start time si and a finish
        # time fi
        # Output: 
        # A nonconflicting schedule of the tasks in T using a minimum number
        # of machines
        # m ← 0 // optimal number of machines
        # while T 	= ∅ do
        # remove from T the task i with smallest start time si
        # if there is a machine j with no task conflicting with task i then
        # schedule task i on machine j
        # else
        # m ← m + 1 // add a new machine
        # schedule task i on machine m


if __name__ == "__main__":
    S: Scheduler = Scheduler()

    S.add_task(3, 5) #0
    S.add_task(4, 9) #1
    S.add_task(6, 11) #2
    S.add_task(10, 13) #3
    S.add_task(11, 12) #4

    S.add_task(3,4)
    S.add_task(3, 4.2)
    S.add_task(4, 4)
    S.add_task(4, 4.3)
    S.add_task(4, 9)
    S.add_task(8, 10)
    S.add_task(9, 10)
    S.add_task(9, 9)



    print(S)

    print(S.find_conflict(1))

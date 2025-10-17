class Task:
    def __init__(self, start_time: int, end_time: int, value: int):
        self.start: int = start_time
        self.end: int = end_time 
        self.value: int = value

    def getDuration(self) -> int:
        return self.end - self.start
    

class Scheduler:
    def __init__(self) -> None:
        self.tasks: dict[int:Task] = dict()
        self.max_id: int = 0

    def __str__(self) -> str:
        result: str = f"# TASKS #"
        for id in self.tasks:
            task = self.tasks[id]
            result += str(f"\nTask {id:>03}: {task.start:>4} to {task.end:<4} ({task.getDuration():>2}s) | {task.value}w")
        return result
    
    def size(self) -> int:
        return len(self.dict)

    def is_empty(self) -> bool:
        return self.size() == 0
            
    def add_task(self, start_time: int, end_time: int, value: int = 0, id: int = -1) -> int:
        if end_time - start_time <= 0:
            raise Exception(f"The task {id} end time {end_time} is less than or equal the start time {start_time}")
    
        if id == -1 or id in self.tasks: 
            self.max_id += 1
            id = self.max_id

        self.tasks[id] = Task(start_time=start_time, end_time=end_time, value=value)
        return id

    def pop_task(self, id) -> tuple[int, int]:
        task: Task = self.tasks.pop(id)
        return (task.start, task.end, task.value)
    
    def get_first_ended_task_id(self) -> int:
        earliest_time: int = float('inf')
        earliest_task_id: int = 0
        for id in self.tasks:
            task: Task = self.tasks[id]
            if task.end < earliest_time:
                earliest_time = task.end
                earliest_task_id = id
        return earliest_task_id

    def find_conflict(self, actual_id) -> list[int]:
        conflict_ids: set[int] = set()
        actual_task: Task = self.tasks[actual_id]
        for other_id in self.tasks:
            if actual_id == other_id: continue
            other_task: Task = self.tasks[other_id]
            # Condicional para verificar se as tarefas se sobreponhem
            if actual_task.start < other_task.end and other_task.start < actual_task.end:
                conflict_ids.add(other_id)
        return sorted(conflict_ids)
    
    def get_highest_conflict_task_degree(self) -> tuple[int, int]:
        id_most_conflicted_task: int = 0
        max_degree: int = 1
        for task_id in self.tasks:
            conflicts: list[int] = self.find_conflict(task_id) 
            if max_degree < len(conflicts):
                max_degree = len(conflicts)
                id_most_conflicted_task = task_id
        return (id_most_conflicted_task, max_degree)

    def one_machine_task_scheduler(self) -> list[int]:
        schedule: list[int] = list()
        
        # for task

        # A nonconflicting schedule of the tasks in T using a minimum number of machines
        # m ← 0 // optimal number of machines
        # while T 	= ∅ do
        # remove from T the task i with smallest start time si
        # if there is a machine j with no task conflicting with task i then
        # schedule task i on machine j
        # else
        # m ← m + 1 // add a new machine
        # schedule task i on machine m
    
    def many_machines_task_schedules(self, limit_machines: int = float('inf')):
        nonconflicting_schedule: dict[int:list]
        optimal_number_of_machines: int = 0

        notscheduled_tasks_ids = []

    def one_machine_task_scheduler_by_weigth(self):
        pass



if __name__ == "__main__":
    S: Scheduler = Scheduler()

    S.add_task(30, 50) #0
    S.add_task(40, 90) #1
    S.add_task(60, 110) #2
    S.add_task(100, 130) #3
    S.add_task(110, 120) #4

    S.add_task(30, 40) #5
    S.add_task(30, 42) #6
    S.add_task(40, 43) #7
    S.add_task(40, 90) #8
    S.add_task(80, 100) #9
    S.add_task(90, 100, id=150) #10

    print(S)

    for i in S.tasks:
        print(f"Conflitos de {i}: {S.find_conflict(i)}")

    print(S.get_highest_conflict_task_degree())
    #CONFLITOS:
    #0, 2, 6, 7, 8, 9

    print(S.get_first_ended_task_id())
class Task:
    def __init__(self, start_time: int, end_time: int):
        self.start: int = start_time
        self.end: int = end_time 


    def getDuration(self) -> int:
        return self.end - self.start



class Scheduler:
    def __init__(self) -> None:
        self.tasks: dict[int:Task] = dict()
        self.ids: set[int] = set()


    def __str__(self) -> str:
        result: str = f"# Scheduler of Tasks object #"
        for id in self.ids:
            task: Task = self.tasks[id]
            result += f"\nTask {id:>03}: {task.start:>4} to {task.end:<4} ({task.getDuration()}s)"
        return result


    def empty(self) -> bool:
        return self.size == 0


    def size(self) -> int:
        return len(self.ids)
    

    def get_free_id(self, given_id: int) -> int:
        if given_id not in self.ids and given_id >= 0:
            return given_id
        for potential_id in range(self.size() + 1):
            if potential_id not in self.ids:
                return potential_id


    def add_task(self, start_time: int, end_time: int, id: int = -1) -> int:
        task: Task = Task(start_time=start_time, end_time=end_time)
        if task.getDuration() <= 0:
            raise Exception("End time is less than or equal the Start time")
        id = self.get_free_id(id)
        self.ids.add(id)
        self.tasks[id] = task
        return id


    def remove_task(self, id) -> tuple[int, int]:
        task: Task = self.tasks.pop(id)
        self.ids.remove(id)
        return (task.start, task.end)
    

    def get_first_ended_task_id(self) -> int:
        earliest_time: int = float('inf')
        earliest_task_id: int = 0
        for id in self.ids:
            task: Task = self.tasks[id]
            if task.end < earliest_time:
                earliest_time = task.end
                earliest_task_id = id
        return earliest_task_id


    def find_conflict(self, actual_id) -> list[int]:
        conflict_ids: set[int] = set()
        actual_task: Task = self.tasks[actual_id]
        for other_id in self.ids:
            if actual_id == other_id: continue
            other_task: Task = self.tasks[other_id]
            # Condicional para verificar se as tarefas se sobreponhem
            if actual_task.start < other_task.end and other_task.start < actual_task.end:
                conflict_ids.add(other_id)
        return sorted(conflict_ids)
    

    def get_highest_conflict_task_degree(self) -> tuple[int, int]:
        id_most_conflicted_task: int = 0
        max_degree: int = 1
        for task_id in self.ids:
            conflicts: list[int] = self.find_conflict(task_id) 
            if max_degree < len(conflicts):
                max_degree = len(conflicts)
                id_most_conflicted_task = task_id
        return (id_most_conflicted_task, max_degree)


    def one_machine_task_scheduler(self) -> list[int]:
        schedule: list[int] = list()
        
        

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
    S.add_task(90, 100, 150) #10

    print(S)

    for i in S.ids:
        print(f"Conflitos de {i}: {S.find_conflict(i)}")

    print(S.get_highest_conflict_task_degree())
    #CONFLITOS:
    #0, 2, 6, 7, 8, 9

    print(S.get_first_ended_task_id())
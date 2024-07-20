# Write your solution here:
class Task:
    identifier = 0
    def __init__(self, description: str, programmer: str, workload: int):
        Task.identifier += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.identifier
        self.finished = False
        
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True
        
    def __str__(self):
        finished = "NOT FINISHED"
        if self.finished:
            finished = "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finished}"
        

class OrderBook:
    def __init__(self):
        self.orders = {}
        
    def add_order(self, description: str, programmer: str, workload: int):
        task = f"T{len(self.orders) + 1}"
        self.orders[task] = Task(description, programmer, workload)
        
    def all_orders(self):
        return [value for order, value in self.orders.items()]
    
    def programmers(self):
        return list(set([value.programmer for order, value in self.orders.items()]))
    
    def mark_finished(self, id: int):
        for order, value in self.orders.items():
            if id == value.id:
                value.mark_finished()
                return
        else:
            raise ValueError("No such task")  
        
    def finished_orders(self):
        return [value for order, value in self.orders.items() if value.finished]
    
    def unfinished_orders(self):
        return [value for order, value in self.orders.items() if not value.finished]

    def status_of_programmer(self, programmer: str):
        for oder, value in self.orders.items():
            if programmer == value.programmer:
                finished = [value.workload for order, value in self.orders.items()if value.programmer == programmer if value.finished ]
                sum_finished = sum(finished)
                unfinished = [value.workload for order, value in self.orders.items() if value.programmer == programmer  if not value.finished]
                sum_unfinished = sum(unfinished)
                return (len(finished), len(unfinished), sum_finished, sum_unfinished)
        else:
            raise ValueError("No such programmer")

    

if __name__ == "__main__":    
    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    print(t.unfinished_orders())
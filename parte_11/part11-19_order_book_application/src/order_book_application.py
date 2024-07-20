# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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
        for order, value in self.orders.items():
            if programmer == value.programmer:
                finished = [value.workload for order, value in self.orders.items()if value.programmer == programmer if value.finished ]
                sum_finished = sum(finished)
                unfinished = [value.workload for order, value in self.orders.items() if value.programmer == programmer  if not value.finished]
                sum_unfinished = sum(unfinished)
                return (len(finished), len(unfinished), sum_finished, sum_unfinished)
        else:
            raise ValueError("No such programmer")
        
class OrderBookApp:
    def __init__(self):
        self.order_app = OrderBook()
        
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def add_order(self):
        description = input("description: ")
        prog_work = input("programmer and workload estimate: ")
        try:
            programmer, workload = prog_work.split(" ")
            workload = int(workload)
            self.order_app.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished(self):
        finished = self.order_app.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else: 
            for order in finished:
                print(order)
                
    def list_unfinished(self):
        for order in self.order_app.unfinished_orders():
            print(order)
    
    def mark_finished(self):
        id_number = input("id: ")
        id_list = [value.id for order, value in self.order_app.orders.items()]
        
        try:
            id_number = int(id_number)
            if id_number in id_list:
                self.order_app.mark_finished(id_number)
                print("marked as finished")
            else:
                print("erroneous input")
        except ValueError:
            print("erroneous input")
            
    def programmers(self):
        all_programmers = self.order_app.programmers()
        for programmer in all_programmers:
            print(programmer)
        
    def status(self):
        programmer = input("programmer: ")
        try:
            finished, unfinished, done, scheduled = self.order_app.status_of_programmer(programmer)
            return f"tasks: finished {finished} not finished {unfinished}, hours: done {done} scheduled {scheduled}"
        except ValueError:
            return f"erroneous input"
        
    def execute(self):
        self.help()       
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished()
            elif command == 3:
                self.list_unfinished()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                print(self.status())
        
        


order = OrderBookApp()
order.execute()
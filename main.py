import csv

class Worker:
    id_counter = 1

    def __init__(self, name, surname, department, salary):
        self.id = Worker.id_counter
        Worker.id_counter += 1
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.id},{self.name},{self.surname},{self.department},{self.salary}"

class WorkerDB:
    def __init__(self):
        self.workers = []

    def add(self, worker):
        self.workers.append(worker)
        self.write_workers_to_csv()

    def delete(self, worker_id):
        self.workers = [worker for worker in self.workers if worker.id != worker_id]
        self.write_workers_to_csv()

    def read(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                id, name, surname, department, salary = row
                worker = Worker(name, surname, department, int(salary))
                worker.id = int(id)
                self.add(worker)

    def write_workers_to_csv(self):
        with open('workers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for worker in self.workers:
                writer.writerow([worker.id, worker.name, worker.surname, worker.department, worker.salary])

    def edit_worker(self, worker_id, attribute, value):
        for worker in self.workers:
            if worker.id == worker_id:
                setattr(worker, attribute, value)
                self.write_workers_to_csv()

    def sort_workers(self, field,):
        self.workers.sort(key=lambda x: getattr(x, field))
        self.write_workers_to_csv()

    def search_workers(self, query):
        results = [worker for worker in self.workers if query.lower() in str(worker).lower()]
        return results

    def display_workers(self):
        for worker in self.workers:
            print(worker)

def print_menu():
    print("\nMenu:")
    print("1. Add Worker")
    print("2. Delete Worker")
    print("3. Edit Worker")
    print("4. Sort Workers")
    print("5. Search Workers")
    print("6. Display Workers")
    print("7. Exit")
db = WorkerDB()
db.read('workers.csv')

while True:
    print_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        department = input("Enter department: ")
        salary = int(input("Enter salary: "))
        new_worker = Worker(name, surname, department, salary)
        db.add(new_worker)

    elif choice == "2":
        worker_id = int(input("Enter ID of the worker to delete: "))
        db.delete(worker_id)

    elif choice == "3":
        worker_id = int(input("Enter ID of the worker to edit: "))
        attribute = input("Enter attribute to edit (name, surname, department, salary): ")
        value = input("Enter new value: ")
        db.edit_worker(worker_id, attribute, value)

    elif choice == "4":
        field = input("Enter field to sort by (name, surname, department, salary): ")
        db.sort_workers(field)

    elif choice == "5":
        query = input("Enter search query: ")
        results = db.search_workers(query)
        print("Search Results:")
        for result in results:
            print(result)

    elif choice == "6":
        db.display_workers()

    elif choice == "7":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

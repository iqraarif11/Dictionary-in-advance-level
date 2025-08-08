todo = {
    "task1": {"title":"Read Book" , "status": "Incomplete"},
    "task2": {"title":"Code App" , "status": "Complete"}
}

#Access nested dictionary valus
print("First task title:", todo["task1"]["title"])

#Add a new task
todo["task3"] = {"title": "Pray", "status":"Incomplete"}

#Update a task's status
todo["task1"]["status"] = "Complete"

#loop through all tasks
for key, value in todo.items():
    print (f"{key}: {value['title']} - {value['status']}")
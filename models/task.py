class Task:

    def __init__(self, name, description, project=None, completed_amount=0, completed=False, id=None):
        self.name = name
        self.description = description
        self.id = id
        self.completed_amount = completed_amount
        self.completed = completed
        self.project = project

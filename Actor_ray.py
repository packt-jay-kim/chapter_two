import ray
ray.init()

@ray.remote
class multiplication():
    def __init__(self):
        self.task = 1
    def multiply(self):
        self.task *=7 
        return self.task

multiplication_answer = multiplication.remote()
print(multiplication_answer)

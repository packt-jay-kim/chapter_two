import ray

ray.init()

@ray.remote(num_gpus=2)
class Actor():
   def __init__(self):
      self.answer = 0
   def add(self):
      self.answer += 1
      return self.answer


A = Actor.remote()
ref = A.add.remote()


print(ray.get(ref))


import ray

ray.init()

@ray.remote
def example():
  return 8

for a in range(10):
  print(example.remote())



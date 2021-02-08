import ray

ray.init()

@ray.remote
def example():
    return 1

@ray.remote
def reference_example(test):
    return test

object_reference = example.remote()

ray.get(object_reference)

object_reference_two = reference_example.remote(object_reference)

print(ray.get(object_reference_two))

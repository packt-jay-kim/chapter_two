import ray

ray.init()

@ray.remote
def remote_example():
    return 10


object_reference = remote_example.remote()
ray.cancel(object_reference)



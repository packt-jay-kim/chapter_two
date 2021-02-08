import ray

ray.init()

@ray.remote(num_gpus=0.3)
def test_gpu():
    return 3


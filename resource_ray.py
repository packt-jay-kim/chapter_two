import ray

ray.init(num_gpus = 10, num_cpus= 20)

import ray

@ray.remote(num_gpus=4)
def example_resource():
    return 7

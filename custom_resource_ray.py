
import ray

ray.init()

@ray.remote(resources={'Custom': 3})
def test_custom():
    return 7



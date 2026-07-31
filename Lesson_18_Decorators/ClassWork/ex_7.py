def singleton(cls):
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance

@singleton
class Config:
    def __init__(self):
        self.debug = False

c1 = Config()
c2 = Config()
print(c1 is c2)
print(id(c1))
print(id(c2))

# False
# 4306008256
# 4305294736
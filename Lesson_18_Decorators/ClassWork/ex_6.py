def method_decorator(func):
    def wrapper(*args, **kwargs):
        print('---Decorator start---')
        result = func(*args, **kwargs)
        print('---Decorator end---')
        return result
    return wrapper


def class_decorator(cls):
    print('---Class decorator start---')
    cls.value = 42
    cls.version = '1.0'
    return cls


@class_decorator
class TestClass:
    name = 'TestClass'

    @method_decorator
    def info(self, user):
        return f'Hello {user}. This is {self.name}'


t = TestClass()
print(t.info('John'))
print(t.value)
print(t.version)
print(t.name)

"""Use a class 'instance' as a decorator demo.
Tracing decorator
"""
class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, function):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"** Tracer information - calling {function}")
            return function(*args, **kwargs)
        return wrap

    @property
    def enabled(self):
        return self._enabled
    
    @enabled.setter
    def enabled(self, is_enabled):
        self._enabled = is_enabled

if __name__ == "__main__":
    tracer = Trace()

    @tracer
    def rotate_list(l):
        return l[1:] + [l[0]]

    @tracer
    def append_reverse(i, l):
        l.append(i)
        return sorted(l, reverse=True)

    li = [1, 2, 3, 4, 5]

    li = append_reverse(19, li)
    print(li)
    li = rotate_list(li)
    print(li)
    
    tracer.enabled = False

    li = rotate_list(li)
    print(li)

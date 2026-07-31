# __call__
class CallTracker:
    def __init__(self):
        self.call_count = 0
        self.call_history = []

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        call_info = {
            'call_number': self.call_count,
            'args': args,
            'kwargs': kwargs
        }
        self.call_history.append(call_info)
        print(f"Call {self.call_count}: {args}, {kwargs}")
        return self.call_count

    def show_history(self):
        if not self.call_history:
            print("No calls made yet.")
        else:
            for call_info in self.call_history:
                print(f"Call {call_info['call_number']}: {call_info['args']}, {call_info['kwargs']}")


tracker = CallTracker()
tracker()
tracker('hello', 2, 3)
tracker(name='Python', version=3.10)
tracker.show_history()
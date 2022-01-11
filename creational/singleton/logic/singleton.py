class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class God(metaclass=SingletonMeta):
    _DAY_TO_WORK_DICT = {
        1: "Light was created",
        2: "Firmament was created",
        3: "Earth with plants and seas was created",
        4: "Sun, moon and stars were created",
        5: "Birds and sea creatures were created",
        6: "Animals and Humans were created",
        7: "I'm resting",
    }

    _LAST_DAY = 7

    def __init__(self):
        self._day = 1

    def do_something(self):
        print(self._DAY_TO_WORK_DICT[self._day])

        if self._day < self._LAST_DAY:
            self._day += 1

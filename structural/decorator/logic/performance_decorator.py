import time

from structural.decorator.logic.decorator import Decorator


class PerformanceDecorator(Decorator):
    def process(self, *args, **kwargs) -> None:
        start = time.time()
        self.wrappee.process(*args, **kwargs)
        print(f"Execution has took {time.time() - start:.3f} seconds")

import time


class Stub:
    def __init__(self, value: int) -> None:
        self.value = value

    def process(self, multiplier: int) -> None:
        steps = self.value * multiplier
        for step in range(0, steps):
            time.sleep(0.2)
            print(f"Step {step + 1} is completed")

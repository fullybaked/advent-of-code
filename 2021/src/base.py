class BaseAOC:
    def __init__(self, day: int):
        self._day = day

    def load(self):
        path = f"data/day{self._day}.txt"

        with open(path, "r") as f:
            data = f.readlines()

        return data

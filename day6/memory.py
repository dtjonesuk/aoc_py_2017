class MemoryBank:
    def __init__(self, banks:list[int]):
        self.ticks = 0
        self.banks = banks

    def balance(self):
        # find largest bank
        idx, value = max(enumerate(self.banks), key=lambda t: t[1])

        # zero the largest bank
        self.banks[idx] = 0

        # redistribute bank
        n = len(self.banks)
        all_get = value // n
        self.banks[:] = [x + all_get for x in self.banks]



        i = idx + 1
        some_get = value % n
        while some_get > 0:
            if i >= n:
                i = 0
            self.banks[i] += 1
            some_get -= 1
            i += 1

    def run(self):
        self.ticks = 0
        seen = set()
        when_seen = dict()
        while True:
            self.ticks += 1
            self.balance()
            current = tuple(self.banks)
            if current in seen:
                break
            seen.add(current)
            when_seen[current] = self.ticks
        return self.ticks, self.ticks - when_seen[current]

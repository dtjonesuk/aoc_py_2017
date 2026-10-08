class Spinlock:
    def __init__(self, cycles):
        self.cycles = cycles
        self.buffer = [0]
        self.position = 0

    def spin(self):
        # Moves position over the circular buffer 'cycles' times.
        self.position = (self.position + self.cycles) % len(self.buffer)

    def step(self, n: int):
        self.spin()
        self.buffer.insert(self.position + 1, n)
        self.position = (self.position + 1) % len(self.buffer)

    def get_next_number(self):
        return self.buffer[(self.position + 1) % len(self.buffer)]

    def run(self, times = 2017):
        for n in range(1, times + 1):
            self.step(n)

# Don't keep a buffer, since we know the required value will be in buffer[1] when we finish.
# Just track the buffer length and value of buffer[1]

class BufferlessSpinlock:
    def __init__(self, cycles):
        self.cycles = cycles
        self.position = 0
        self.buffer_size = 1
        self.value = -1

    def spin(self):
        # Moves position over the circular buffer 'cycles' times.
        # Add 1 to account for the number we 'inserted'
        self.position = (self.position + self.cycles + 1) % self.buffer_size
        self.buffer_size += 1

    def step(self, n: int):
        self.spin()
        # If number is to be inserted after buffer[0] then hold on to its value
        if self.position == 0:
            self.value = n

    def get_next_number(self):
        return self.value

    def run(self, times = 2017):
        for n in range(1, times + 1):
            self.step(n)
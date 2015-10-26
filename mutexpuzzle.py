PUZZLE_GOAL = 16384


class LockableAddress(object):
    def __init__(self, index, allocated=False, locked=False):
        self.index = index
        self.allocated = allocated
        self.locked = locked

    def __repr__(self):
        return 'LockableAddress(%r)' % self.index

    def toggle(self):
        if self.locked:
            pass
        self.allocated = (self.allocated is not True)  # toggles

    def lock(self):
        self.locked = True

    def allocate(self):
        self.allocated = True

    def islocked(self):
        return self.locked

    def isallocated(self):
        return self.allocated

    def __eq__(self, other):
        return (self.index == other.index)

    def __lt__(self, other):
        return (self.index < other.index)

    def __le__(self, other):
        return (self.index <= other.index)

    def __gt__(self, other):
        return (self.index > other.index)

    def __ge__(self, other):
        return (self.index >= other.index)


class LockableArray(object):
    def __init__(self, size):
        self.array = [LockableAddress(k) for k in range(2, size)]

    def propogate(self, address):
        address.allocate()
        address.lock()
        for entry in self.array:
            if entry <= address:
                continue
            if entry.index % address.index == 0:
                if not entry.islocked():
                    entry.toggle()

    def simulate(self):
        for item in self.array:
            if not item.isallocated():
                print("\rSimulating, %2.1f percent done" %
                      (100*item.index/(PUZZLE_GOAL)), end=''),
                self.propogate(item)

    def maxlocked(self):
        lockedlist = [address for address in self.array if address.islocked()]
        return max(lockedlist)


PuzzleArray = LockableArray(PUZZLE_GOAL)
PuzzleArray.simulate()
print()
print("Highest locked address is", PuzzleArray.maxlocked())

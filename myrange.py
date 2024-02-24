#myrange.py
import math

def get_range(start, stop = None, step = None, /):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1

    _require_int(start, 'start')
    _require_int(stop, 'stop')
    _require_int(step, 'step')

    return MyRange(start, stop, step)

def _require_int(value, name):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer, but was {value}')

class MyRange:
    def __init__(self, start, stop, step, /):

        self._start = start
        self._stop = stop
        self._step = step

    def __repr__(self):
        return f'MyRange({self._start}, {self._stop}, {self._step})'

    def __iter__(self):
        return MyRangeIterator(self)

    def __eq__(self, other):
        if type(other) is MyRange:
            return self.start() == other.start() \
                   and self.stop() == other.stop() \
                   and self.step() == other.step()
        else:
            return NotImplemented

    def __len__(self):
        return max(0, math.ceil((self._stop - self._start) / self._step))

    def __getitem__(self, index):
        if type(index) is int:
            if not 0 <= index < len(self): #one difference between this and regular ranges is that regular ranges can be indexed with negative numbers
                raise IndexError
            else:
                return self._start + index * self._step
        elif type(index) is slice:
            start, stop, step = index.indices(len(self))

            new_start = self._start + start * self._step
            new_stop = min(self._start + stop * self._step, self._stop)
            new_step = step * self._step

            return MyRange(new_start, new_stop, new_step)

        else:
            raise TypeError

    def __hash__(self):
        return hash((self._start, self._stop, self._step))
    

    def start(self):
        return self._start

    def stop(self):
        return self._stop

    def step(self):
        return self._step


class MyRangeIterator:
    def __init__(self, myrange):
        self._myrange = myrange
        self._next = self._myrange.start()

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self._myrange.stop():
            raise StopIteration
        result = self._next
        self._next += self._myrange.step()
        return result

#O(1) space complexity

#O(n) time complexity
        


        
        

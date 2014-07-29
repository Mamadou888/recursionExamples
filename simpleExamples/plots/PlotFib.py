"""
This class shows how the simple fibonnacci fcn increases in time at each
recursive call.
"""
import time
import itertools
import numpy as np
import matplotlib.pyplot as plt


class PlotFib:
    """ This simple class plots the time it takes to compute numbers in
    the fibonnacci sequence."""
    def __init__(self):
        self.cache = {0: 1, 1: 1}             # base cases 0 and

    def __str__(self):
        return "Plot Fibonnacci"

    def simple_fib(self, n):
        # Standard issue recursive fibonnacci cn
        if n < 2:                   # Base Case(s)
            return 1
        else:                       # Recursive Case
            return (self.simple_fib(n-1) + self.simple_fib(n-2))


    def cached_fib(self, n):
        # caches answers it knows
        if n in self.cache:
            return self.cache[n]
        elif not n in self.cache and not n is None:
            self.cache[n] = self.simple_fib(n)
            return self.cache[n]

    def plot(self, *args):
        pass

    def plot_function(self, function, n):
        points = []
        start = time.clock()
        for i in range(n):
            function(i)
            points.append((time.clock()-start) * 10000)
        return points

    def plot_simple(self, n):
        return self.plot_function(self.simple_fib, n)

    def plot_cached(self, n):
        return self.plot_function(self.cached_fib, n)


def main():
    pf = PlotFib()
    # print "plotting simple"
    simple = pf.plot_simple(15)
    # print "PRE", pf.cache
    cached1 = pf.plot_cached(15)
    # print "POST", pf.cache
    cached2 = pf.plot_cached(15)

    # ymax = np.argmax(simple[-1], cached[-1])
    # plt.xlim([0, 100])
    # plt.ylim([0, ymax])


    plt.plot(simple)
    plt.plot(cached1)
    plt.plot(cached2)
    # plt.plot(range(0,100))
    plt.legend(['simple','first cached', 'second cached'], loc='upper left')
    plt.show()


if __name__ == "__main__":
    main()

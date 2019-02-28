"""
__author__ = Hagai Har-Gil
"""
import numpy as np
import matplotlib.pyplot as plt


class CompareSeries:
    """ Compare Fibonacci series to prime numbers series """
    def __init__(self, n):
        self._validate_nonneg_int(n)
        self.n = n

    def _validate_nonneg_int(self, n):
        if not isinstance(n, int) or n < 0:
            raise TypeError("n must be a non-negative number")

    def compare(self):
        """ Run the comparison of the series """
        if self.n == 0:
            return np.array([])
        fib_arr = self.gen_fib_arr()
        prime_arr = self.gen_prime_arr()
        diff = fib_arr - prime_arr

        # Plots
        fig, ax = plt.subplots()
        ax.plot(diff)
        ax.set_title('Fibonacci - Primes')
        ax.set_xlabel('n')
        ax.set_ylabel('Difference')
        return diff

    def gen_fib_arr(self):
        """ Create a Fibonacci series up to some n """
        vals = (0, 1)
        result = [0, 1]
        for idx in range(self.n):
            vals = (vals[1], vals[0] + vals[1])
            result.append(vals[1])
        return np.array(result[:self.n])

    def gen_prime_arr(self):
        """
        Return a vector with the first n prime numbers
        """
        num = 3
        result = [2]
        primes_found = 0
        while primes_found < self.n-1:
            for divisor in range(num-1, 1, -1):
                if num % divisor == 0:
                    break
            else:
                primes_found += 1
                result.append(num)
            num += 1
        return np.array(result)


if __name__ == '__main__':
    print(CompareSeries(10).compare())
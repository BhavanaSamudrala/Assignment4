# Bhavana Samudrala
# student number- 11258695
# NSID- bhs053
# Instructor- Arlin Schaffel
# CMPT-145-L14

from collections import Counter

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far
        self.__inputs = []

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.__count += 1
        self.__inputs.append(value)
        k = self.__count           # convenience
        diff = value - self.__avg  # convenience
        self.__avg += diff / k


    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count

    def min(self):
        """
        Purpose:
            Return the minimum value seen so far.
        Post-conditions:
            (none)
        Return:
            The minimum seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        if len(self.__inputs) == 0:
            return None
        else:
            return min(self.__inputs)

    def max(self):
        """
        Purpose:
            Return the maximum value seen so far.
        Post-conditions:
            (none)
        Return:
            The maximum seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        if len(self.__inputs) == 0:
            return None
        else:
            return max(self.__inputs)

    def mode(self):
        """
        Purpose:
            Return the mode value seen so far.
        Post-conditions:
            (none)
        Return:
            The mode seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        data = Counter(self.__inputs)
        data_dict = dict(data)
        if len(self.__inputs) == 0:
            return None
        else:
            return [k for k, v in data_dict.items() if v == max(list(data.values()))][0]

    def range(self):
        """
        Purpose:
            Return the range for the input.
        Post-conditions:
            (none)
        Return:
            The range.
            Note: if no data has been seen, None is returned.

        """
        minValue = self.min()
        maxValue= self.max()

        if len(self.__inputs) == 0:
            return None
        else:
            return maxValue - minValue



def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to
        be considered equal.  See the Addendum in the assignment!
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance

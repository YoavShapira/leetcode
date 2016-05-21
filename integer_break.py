import functools
import math
import operator

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        max_product = 0

        for num_subsections in xrange(2, 100):
	        subsections = self.subsect(n, num_subsections)

	        product = functools.reduce(operator.mul, subsections, 1)
	        if product > max_product:
	        	max_product = product

        return max_product

    def subsect(self, n, num_subsections):
    	"""
    	:type n: int
    	:type num_subsections: int
    	:rtype: list
    	"""

    	# Split into a list of blocks starting at equal suze
        subsection_value = int(math.floor(n / num_subsections))
        subsections = []
        while len(subsections) < num_subsections:
        	subsections.append(subsection_value)

        # Increment elements by 1 as needed until sum is accurate
        subsections = self.ensure_sum(n, subsections)
        return subsections

    def ensure_sum(self, n, subsections):
    	"""
    	:type n: int
    	:type subsections: list
    	:rtype: list
    	"""

    	# Quick out if nothing needed
    	if sum(subsections) == n:
    		return subsections

    	# Adjust one element by 1 at a time
    	while sum(subsections) != n:
    		for i in xrange(len(subsections)):
    			subsections[i] += 1
    			if sum(subsections) == n:
    				return subsections

    	raise Exception("Couldn't make them sum up?")


if __name__ == '__main__':
	s = Solution()
	for n in xrange(28, 30):
		print "%d: %d" % (n, s.integerBreak(n))

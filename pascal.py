"""
https://leetcode.com/problems/pascals-triangle-ii/

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: list[int]
        """

        # Naive version generates triangle, picks row.
        # Can memoize for time.
        tri = self.gen_tri(rowIndex + 1)
        return tri[rowIndex]

    def gen_tri(self, rows):
    	"""
    	:type rows: int
    	:rtype: list[list]
    	"""

    	tri = []
    	for _ in range(rows): 
    		row = [1] # All rows start this way
    		if tri: # then we're in the second row or beyond
    			last_row = tri[-1] # reference the previous row
    			# this is the complicated part, it relies on the fact that zip
    			# stops at the shortest iterable, so for the second row, we have
    			# nothing in this list comprension, but the third row sums 1 and 1
    			# and the fourth row sums in pairs. It's a sliding window.
    			row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
    			# finally append the final 1 to the outside
    			row.append(1)
    		tri.append(row)
    	return tri

if __name__ == '__main__':
	s = Solution()
	for rowIndex in xrange(0, 10):
		print s.getRow(rowIndex)
        
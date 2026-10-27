# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
            # goal --> determine the weight for every single integer in our NL and multiply it to the integer itself and add them all together as a result.

            # calculating weight:
                # maxDepth - depth_int = weight
            # type check --> int? continue and if list then we increment our depth

            def findDepth(n, depth):
                if n.isInteger():
                    return depth
                
                max_depth = depth

                for element in n.getList():
                    max_depth = max(max_depth, findDepth(element, depth + 1))
                
                return max_depth
            

            max_depth = 0
            for n in nestedList:
                max_depth = max(max_depth, findDepth(n, 1))
            
            def calculateSum(n, depth):
                if n.isInteger():
                    weight = max_depth - depth + 1
                    return n.getInteger() * weight
                
                res = 0

                for element in n.getList():
                    res += calculateSum(element, depth + 1)
            
                return res

            final_sum = 0

            for n in nestedList:
                final_sum += calculateSum(n, 1)
            
            return final_sum






        
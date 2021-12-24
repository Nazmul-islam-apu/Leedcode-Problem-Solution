class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        l = len(heights)
        i = 0
        max_area = 0
        while (i < l):
            if not (stack) or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top_of_stack = stack.pop()
                if stack:
                    area = heights[top_of_stack] * (i - stack[-1] - 1)
                else:
                    area = heights[top_of_stack] * i
                print(area)
                max_area = max(area, max_area)

        while (stack):
            top_of_stack = stack.pop()
            if stack:
                area = heights[top_of_stack] * (i - stack[-1] - 1)
            else:
                area = heights[top_of_stack] * i
            max_area = max(area, max_area)

        return max_area
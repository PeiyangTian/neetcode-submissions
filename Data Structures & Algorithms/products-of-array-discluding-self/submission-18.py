class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                product *= i
                i += 1

        
        for i in nums:
            if zeros >= 2:
                res.append(0)
            elif zeros == 1:
                res.append(product if i == 0 else 0)
            else:
                res.append(product//i)
        return res
        

        

        
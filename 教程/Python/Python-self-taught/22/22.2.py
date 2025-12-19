#解法一

class Solution:
    def numberOfSteps(self, num: int) -> int:
        i=0
        while num!=0:
            if num%2==0:
                num=num/2
                i+=1
            else:
                num-=1
                i+=1
        return i
solution=Solution()
num=14
print(solution.numberOfSteps(num))

#解法二：在解法一的基础上稍微简化了一点

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=num
        i=0
        while n!=0:
            if n%2==0:
                n=n/2
                i+=1
            else:
                n-=1
                i+=1
        return i
solution=Solution()
num=14
print(solution.numberOfSteps(num))

#解法三：将i+=1放到了if-else语句外面、同时在while循环里面，时间复杂度降低了，空间复杂度提高了

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=num
        i=0
        while n!=0:
            if n%2==0:
                n=n/2
            else:
                n-=1
            i+=1
        return i
solution=Solution()
num=14
print(solution.numberOfSteps(num))

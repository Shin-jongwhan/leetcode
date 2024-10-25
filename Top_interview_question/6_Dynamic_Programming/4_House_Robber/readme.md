### https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
### <br/><br/>

## 풀이
### 이것도 전혀 감을 잡지 못 했다. 오래 생각하면 될 것 같긴한데, 한 1시간 정도 생각해봤지만 도저히 생각이 안 났다.
### 숫자 크기가 다른 경우에는 어떻게 비교할 수 있게 생각해봤는데, 만약 숫자가 같다면 이라는 조건을 어떻게 만족시켜야 할지 떠오르지가 않았다.
### <br/>

### 그래서 코드를 참고 했는데, 이것도 잘 이해가 안 된다. dynamic programming이 중간값을 저장하여 프로그래밍하는 것으로 알고 있는데... 물론 그 개념은 맞는 것 같은데.... 이상하게 문제의 방법적인 건 어렵다.
```
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        opt = [0] * n
        opt[0], opt[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            opt[i] = max(nums[i] + opt[i-2], opt[i-1])

        return opt[n-1]
```

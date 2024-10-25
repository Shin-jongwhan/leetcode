### https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
### <br/><br/>

## 풀이
### 이것도 전혀 감을 잡지 못 했다. 오래 생각하면 될 것 같긴한데, 한 1시간 정도 생각해봤지만 도저히 생각이 안 났다.
### 숫자 크기가 다른 경우에는 어떻게 비교할 수 있게 생각해봤는데, 만약 숫자가 같다면 이라는 조건을 어떻게 만족시켜야 할지 떠오르지가 않았다.
### <br/>

### 그래서 코드를 참고 했는데, 이것도 잘 이해가 안 된다. dynamic programming이 중간값을 저장하여 프로그래밍하는 것으로 알고 있는데... 물론 그 개념은 맞는 것 같은데 너무 어렵다.
#### 아래 코드에서도 대부분이 dp\[idx\]+num이 되지 않나? 뭔가 잘 모르겠다.
```
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, nums[0]]

        for idx, num in enumerate(nums[1:]):
            dp.append(max(dp[idx]+num, dp[idx+1]))

        return dp[-1]
```

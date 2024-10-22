### https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
### <br/><br/>

## 첫 시도(answer.py)
### 먼저 구현을 위해서 다음과 같이 만들었다.
### 이 코드는 이렇게 동작한다.
1. 2개 linked list를 다시 리스트로 만든 후
2. sorting
3. 다시 linked list로 변환
### <br/>

### 시간복잡도가 sorting으로 인해 최대 NlogN이고, O(N)의 과정을 3번 수행하게 된다. 그래서 많이 느리다.
#### ![image](https://github.com/user-attachments/assets/063b3236-afba-4754-9cfe-56c0ba890001)
### <br/><br/>

## 최적해 테스트(answer_best_score.py)
### 릿코드에서 가장 빠른 것으로 보여준 코드이다.
### <br/>

### 실제 수행에 걸린 시간
### 최대가 뜰 때도 있는데 잘 안 뜨고 왔다갔다 한다.
#### ![image](https://github.com/user-attachments/assets/1e6f2ae8-9fbf-4f7a-a52d-b4b9d4c938f1)
### <br/><br/>

## 두 번째 시도(answer2.py)
### 실제 수행에 걸린 시간
### best score가 나왔다.
#### ![image](https://github.com/user-attachments/assets/9c6aea17-ee7b-480a-bb21-0a8771b06bb8)
### <br/>

### 이 시도에서는 다음의 조건을 이용하였다.
- 0 <= length <= 50
- 두 linked list 모두 오름차순으로 정렬되어 있음
### <br/>

### 두 번째 시도에서는 첫 번째 시도에서의 다음의 비효율을 개선하였다.
- 리스트로 변환 후 다시 linked list로 만드는 것을 안 하고 두 linked list를 비교하여 바로 만듦
- 리스트로 변환하지 않기 때문에 sorting을 수행하지 않음
### <br/>

### 

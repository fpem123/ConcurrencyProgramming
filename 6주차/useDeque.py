'''
 - 20년 가을학기 분산병렬 프로그래밍
 - 5장 스레드 간의 통신
 - deque(double-ended queue) 사용
 - 이호섭
'''

import collections

doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))

for item in doubleEndedQueue:
    print("item {}".format(item))

print("Left Most Element: {}".format(doubleEndedQueue[0]))
print("Right Most Element: {}".format(doubleEndedQueue[-1]))

doubleEndedQueue.remove('1')
print("Removing Element: {}".format(doubleEndedQueue))

print()

# deque 에 원소 추가하기
doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))

doubleEndedQueue.append('1')
print("Dequeue: {}".format(doubleEndedQueue))

doubleEndedQueue.appendleft('6')
print("Dequeue: {}".format(doubleEndedQueue))

print()

# deque 에 원소 꺼내기
doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))

rightPop = doubleEndedQueue.pop()
print(rightPop)
print("Dequeue: {}".format(doubleEndedQueue))

leftPop = doubleEndedQueue.popleft()
print(leftPop)
print("Dequeue: {}".format(doubleEndedQueue))

print()

# deque 의 특정 위치에 원소 삽입하기
doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))

doubleEndedQueue.insert(4, 5)   # 3번 위치에 5 추가
print("Dequeue: {}".format(doubleEndedQueue))

print()

# deque 원소 회전하기
doubleEndedQueue = collections.deque('123456')
print("Dequeue: {}".format(doubleEndedQueue))
# 오른쪽으로 회전
doubleEndedQueue.rotate(3)
print("Dequeue: {}".format(doubleEndedQueue))
# 왼쪽으로 회전
doubleEndedQueue.rotate(-2)
print("Dequeue: {}".format(doubleEndedQueue))
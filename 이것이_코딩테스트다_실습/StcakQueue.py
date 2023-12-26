'''
그래프 탐색 알고리즘: DFS/BFS
탐색: 많은 양의 데이터 중 원하는 데이터를 찾는 과정
stack: 선입후출(LIFO), 입출구 동일
따로 라이브러리 사용안하고 리스트로 구현
'''
stack = []
stack.append(5)
stack.append(2)
stack.pop()
stack.append(1)
stack.append(7)
stack.pop()
# print(stack[::-1])
print(stack)

'''
// java
Stack<Integer> stack = new Stack<>();
stack.push(5);
stack.push(2);
stack.pop();
...
while(!stack.empty()) {
    System.out.print(stack.peek() + " ");
    stack.pop();
}
'''

'''
Queue: 선입선출(FIFO), 입출구 다른 터널
deque 라이브러리 사용하여 구현(리스트로 구현가능하지만 시간복잡도가 더 큼)
'''
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.popleft()
queue.append(1)
queue.append(7)
queue.popleft()
print(queue)
queue.reverse()
print(queue)

'''
// java
Queue<Integer> queue = new LinkedList<>();
queue.offer(5);
queue.offer(2);
queue.poll();
...
while(!queue.isEmpty()){
    System.out.print(queue.poll() + " ");
}
'''


import time, random
	
def evaluate_n2(A, n):
	# code for O(n^2)-time function
	sum = 0
	for i in range(0, n-1):
		for j in range(i, n-1):
			sum += A[i] * A[j]
	return sum
	
def evaluate_n(A, n):
	# code for O(n)-time function
	sum = 0
	for i in range(0, n-1):
		if A[i] % 2 == 0:
			sum += A[i]
	return sum
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = []
for i in range(n):
	number = random.randint(-1000,1000)
	A.append(number)

# evaluate_n2 호출
before1 = time.process_time()
evaluate_n2(A, n)
after1 = time.process_time()

# evaluate_n 호출
before2 = time.process_time()
evaluate_n(A, n)
after2 = time.process_time()

# 두 함수의 수행시간 출력
print("수행시간 =", after1 - before1)
print("수행시간 =", after2 - before2)
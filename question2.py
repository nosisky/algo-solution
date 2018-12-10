def solution(a, k):
    collector = []
    for i in range(len(a)):
        print((i-k) % len(a), i)
        collector.append(a[(i-k) % len(a)])
    print(collector)
    
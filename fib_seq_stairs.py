def climbStairs(n):
        fib_seq = []
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        for num in range(n):
            if len(fib_seq) == 0 or len(fib_seq) == 1:
                fib_seq.append(1)
            else:
                fib_seq.append(fib_seq[-2] + fib_seq[-1])
        return fib_seq[-1] + fib_seq[-2]
        

print(climbStairs(6))
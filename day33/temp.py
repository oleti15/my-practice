temperatures=[73,74,75,71,69,72,76,73]
n = len(temperatures)
ans = [0] * n
stack = []  
for i in range(n):
    while stack and temperatures[i] > temperatures[stack[-1]]:
        day = stack.pop()
        ans[day] = i - day
    stack.append(i)
print(ans)

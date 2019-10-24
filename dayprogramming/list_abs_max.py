####### ans
##def ans(v):
##    s=0
##    for i in range (0,len(v)-1):
##        s=s+abs(v[i]-v[i+1])
##    return s
##
#### all
##def perm(a):
##    length = len(a)
##    if length == 1:
##        return [a]
##    else:
##        result = []
##        for i in a:
##            b = a.copy()
##            b.remove(i)
##            b.sort()
##            for j in perm(b):
##                j.insert(0, i)
##                if j not in result:
##                    result.append(j)
##        return result
##
##def solution(v):
##    answer=0
##    re=[]
##    c=perm(v)
##    for i in range(len(c)):
##        re.append(ans(c[i]))
##        answer=max(re)
##    return answer
##
##
##
##v=[20,8,10,1,4,15]
##


##def factorial(n):
##    return n * factorial(n-1) if n > 1 else 1
##factorial(len(v))



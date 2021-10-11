def solution(s):
    sol1, sol2 = 0, 0
    
    while True:
        if s == '1':
            break
        
        sol1 += 1
        sol2 += s.count('0')
        s = s.replace('0', '')
        length = len(s)
        
        k = ''
        while length > 0:
            length, r = divmod(length, 2)
            k += str(r)
        s = k
        if s == '1':
            break
        
    return [sol1, sol2]
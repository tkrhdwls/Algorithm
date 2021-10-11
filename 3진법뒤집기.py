def solution(n):
    digit = ''
    answer = 0
    
    while n > 0:
        n, r = divmod(n, 3)
        digit += str(r) # 앞뒤 반전 바로 적용
    
    s = 1
    for i in digit:
        answer += int(i) * (3 ** (len(digit) - s))
        s += 1
    return answer
    
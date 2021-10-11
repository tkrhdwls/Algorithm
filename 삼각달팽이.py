def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0 # 초기값 x+=1을 하기에 일부러 x=-1로 설정
    num = 1

    for i in range(n): # i는 방향을 나타냄
        for j in range(i, n): # 한 방향 안에서 숫자를 채워가는 걸 한 텀으로 본다면 j는 한 텀의 크기를 뜻함
            # 아래로
            if i % 3 == 0:
                x += 1
                
            # 오른쪽
            elif i % 3 == 1:
                y += 1
                
            # 위로
            elif i % 3 == 2:
                x -= 1
                y -= 1
                
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer
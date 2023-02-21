def solution(elements):
    n=len(elements)
    elements*=2
    arr = []
    for i in range(1,n+1):
        if i == n:
            arr.append(sum(elements[0:n+1]))
        else:
            for j in range(n):
                arr.append(sum(elements[j:j+i]))
    return len(set(arr))

solution([7,9,1,1,4])
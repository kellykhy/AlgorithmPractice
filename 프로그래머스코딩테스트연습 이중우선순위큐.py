def solution(operations):
    answer = []
    queue = []
    for op in operations:
        if 'I' in op:
            queue.append(int(list(op.split())[1]))
        elif '-' in op:
            queue.remove(min(queue))
        else:
            queue.remove(max(queue))
    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# return = [-45, 45]

##미완성

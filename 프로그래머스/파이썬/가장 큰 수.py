def solution(numbers):
    answer = ''

    numbers = [str(s) for s in numbers]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)

    answer = ''.join(numbers) if numbers[0] != '0' else "0"
    return answer

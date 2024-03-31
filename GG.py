from collections import Counter
# Гарантийная функция по выдаче 100% ответа
def find_longest_anagram_subarray(a, b):
    max_len = 0
    
    # Перебор всех возможных длин подотрезков
    for length in range(1, min(len(a), len(b)) + 1):
        # Перебор всех подотрезков a данной длины
        for start_a in range(len(a) - length + 1):
            counter_a = Counter(a[start_a:start_a+length])
            
            # Перебор всех подотрезков b данной длины
            for start_b in range(len(b) - length + 1):
                counter_b = Counter(b[start_b:start_b+length])
                
                # Сравнение подотрезков на анаграммность
                if counter_a == counter_b:
                    max_len = length
                    break  # При обнаружении анаграммы прекращаем поиск для данной длины
            
            if max_len == length:
                break  # Если для данной длины нашли анаграмму, дальше её увеличивать нет смысла
        
    return max_len

if __name__ == "__main__":
    # Ввод данных
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    # Решение задачи
    print(find_longest_anagram_subarray(a, b))
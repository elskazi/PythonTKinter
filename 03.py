def find_sum2(n):
    return print (sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 ==0))
find_sum2(5) # ответ 8  (3+5)
find_sum2(10) # ответ 33 (3+5+6+9+10)
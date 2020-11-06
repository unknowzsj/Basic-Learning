resort = ['Neimeng', 'Lanzhou', 'Xinjiang', 'Xian', 'Dalian']

'''原始顺序'''
print(resort)

# 不改变顺序
'''按照字母顺序排序'''
print(sorted(resort))
print(resort)
'''反向字母顺序'''
print(sorted(resort, reverse=True))
print(resort)

# 永久改变顺序
'''反向打印'''
resort.reverse()
print(resort)
resort.reverse()
print(resort)

# 永久改变顺序
'''按照字母顺序排序'''
resort.sort()
print(resort)
'''反向字母排序'''
resort.sort(reverse=True)
print(resort)

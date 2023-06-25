'''
S = 10
infinitesimal = 0.000001

a = S / 2

b = S / a
delta = a - b

print(f'这是第1轮，S={S}, a={a}, b={b}, delta={delta}, 是否结束：{delta < infinitesimal}')

a = (a + b) / 2
b = S / a
delta = a - b

print(f'这是第2轮，S={S}, a={a}, b={b}, delta={delta}, 是否结束：{delta < infinitesimal}')

a = (a + b) / 2
b = S / a
delta = a - b
print(f'这是第3轮，S={S}, a={a}, b={b}, delta={delta}, 是否结束：{delta < infinitesimal}')

a = (a + b) / 2
b = S / a
delta = a - b
print(f'这是第4轮，S={S}, a={a}, b={b}, delta={delta}, 是否结束：{delta < infinitesimal}')
'''

print('下面我们用循环来重新计算这个问题')

for S in range(1,101):

    infinitesimal = 0.000001

    a = S / 2

    counter = 1
    while True:
        b = S / a
        delta = a - b
        print(f'这是第{counter}轮，S={S}, a={a}, b={b}, delta={delta}, 是否结束：{delta < infinitesimal}')
    
        counter = counter + 1

        if delta < infinitesimal:
            break
        else:
            a = a = (a + b) / 2
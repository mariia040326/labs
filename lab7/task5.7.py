'''
Дана цілочислова прямокутна матриця. Визначити кількість рядків, які не містять
жодного нульового елемента.
'''
a=[
    [2,0,4,0],
    [4,6,1,2],
    [4,0,1,0],
    [1,0,3,7],
    [2,9,2,3]
]
s=0

for el in range(len(a)):
    if el>0:
        s+=el

print(s)


'''Трикутник задається координатами своїх вершин на площині:
 . Скласти програму для знаходження площі трикутника за
формулою Герона.'''
from math import sqrt
#0 позначення
'''x1,x2,x3-перші координати
y1,y2,y3-другі координати
ab,bc,ac-сторони трикутника
p-пів=периметр
s-площа'''
#1
x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
x3=int(input('x3='))
y3=int(input('y3='))
ab=sqrt((x2-x1)**2+(y2-y1)**2)
bc=sqrt((x3-x2)**2+(y3-y2)**2)
ac=sqrt((x3-x1)**2+(y3-y1)**2)
p=(ab+bc+ac)/2
s=sqrt(p*(p-ab)*(p-bc)*(p-ac))
print('={0:.2f}'.format(s))# laboratory4
# laboratory4
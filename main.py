n = 5
n = 5
n = None  # пустое значение для переменной

m = 1.89
print(m)

n = 5

print(type(n))  # type показывает тип переменной

'''
print(m)
print(m)
print(m)
print(m)
print(m)



'''


# print(m)
# print(m)
# print(m)

a = 5
b = 5.89
c = 'hello'
#print ( a,'-', b, '-'c)  # интрополяция
print(f"{a}- {b}- {c}")
print("{}- {}- {}".format(a,b,c))

input('введите первое число')   #ввод данных
a= input()   #ввод данных и сохранение в переменную 
b= input('введите втрое число')
print(a,'+',b,'=',a+b)


#Приведение значений
c=5.89
n=int(c)


input('введите первое число')   #ввод данных
a= int (input())   #ввод данных и сохранение в переменную 
b= int (input('введите втрое число'))
print(a,'+',b,'=',a+b)


#Округление

a=5.26262
b=22.36565
print(round(a*b,3))

username= input('Введите имя ')
if username=='Маша':
    print('ура это же Маша')
elif username=='Марина':
    print('Я так ждала вас марина')
elif username=='Миша':
    print('Миша топ')
else:
    print('Привет, ', username )


i=0
while i<5:
    # if i== 3:
    #     break
    i=i+1
else:
    print('Пожалуй')
    print('хватит ')
print(i)

n= int(input())
flag=True
i=2
while flag:
    if n%i ==0:
        flag=False
        print(i)
    elif i>n //2:
        print(n)
        flag=False
    i+=1 


    a='qwerty'

    for i in a:
        print(a[i])


line =''
for i in range(5):
    line =""
    for j in range(5):
        line+="*"
    print(line)
    
text = 'Съешь еще этих мяГКИх французских булочек' 
print(len(text))
print('еще' in text)
print(text.lower()) #нижний регистр
print(text.upper())
print(text.replace('еще','ЕЩЕ'))











'''Главный вождь племени Абба не умеет считать. В обмен на одну из его земель вождь другого племени предложил ему выбрать одну из трех куч с золотыми монетами. 
Но вождю племени Абба хочется получить наибольшее количество золотых монет. Помогите вождю сделать правильный выбор!

Входные данные
В первой строке входного файла INPUT.TXT записаны три натуральных числа через пробел. Каждое из чисел не превышает 10100. Числа записаны без ведущих нулей.

Выходные данные
В выходной файл OUTPUT.TXT нужно вывести одно целое число — максимальное количество монет, которые может взять вождь.'''
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
#a,b,c = int(data)
if a>b and a>c:
   output_data.write(str(a))
   print(a)
elif b>a and b>c:
   output_data.write(str(b))
   print(b)
elif c>b and c>a:
   output_data.write(str(c))   
   print(c)
   output_data.close()
   input_data.close()

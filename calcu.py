'''
Created by Thomas Lee on 2025/12/14
这是一个四则运算的计算器小游戏。
'''

output = '''
***********************************
这是一个四则运算的计算器小游戏。
您可以输入任意两个数字，然后输入操作符，
+ ：代表加法运算
- ：代表减法运算
* ：代表乘法运算
/ ：代表除法运算
计算器实时显示算式和结果。
************************************
'''

print(output)

tuichu:bool = False
while tuichu == False:
    num1 = int(input('请输入第一个数字:  '))
    num2 = int(input('请输出第二个数字:  '))
    op = input('请输入操作符:  ')
    result = 0


    def jisuan(num1: object, num2: object, op: object) -> None:
        if op == '+':
            result = num1+num2
            print('您输入的算式是：')
            print(str(num1) + op + str(num2)+'='+str(result))
        elif op == '-':
            result = num1-num2
            print('您输入的算式是：')
            print(str(num1) + op + str(num2)+'='+str(result))
        elif op == '*':
            result = num1*num2
            print('您输入的算式是：')
            print(str(num1) + op + str(num2)+'='+str(result))
        elif op == '/':
            result = round(num1/num2,2)  #保留两位小数
            print('您输入的算式是：')
            print(str(num1) + op + str(num2)+'='+str(result))
        else:
            print('此操作符未定义！请重新输入！')

    jisuan(num1,num2,op)

    someting: str = input('您还要继续计算吗？请输入：Y/N  ')
    if someting == 'N' or someting == 'n':
        tuichu = True
        break
    else:
        tuichu = False
        continue


import tkinter as tk
from turtle import width
from xml.etree.ElementPath import xpath_tokenizer

root = tk.Tk()
root.title('電卓')
root.geometry('405x455')

ope_list = ['+', '-', 'x', '÷']
num = 0
result = 0
ope = ''

flg = True

##計算結果表示用frame##
result_frame = tk.Frame(root)
result_frame.grid(column='0', row='0', columnspan='2')

##計算結果表示用label##
result_label = tk.Label(result_frame, text='0', font=('', 30))
result_label.grid(column='0', row='0')

##文字盤配置用frame##
number_frame = tk.Frame(root)
number_frame.grid(column='0', row='1')

##演算子配置用frame##
ope_frame = tk.Frame(root)
ope_frame.grid(column='1', row='1')

fonts=('', 20)

def set_num(i):
    global num

    if num == 0:
        num = i
        result_label['text'] = num
    else:
        num = num * 10 + i
        result_label['text'] = num

def cal(x):
    global flg
    global ope
    global num
    global result

    try:
        i = int(x)
        set_num(i)
    except ValueError:
        i = x

        if i == '=':
            if ope == '+':
                result += num
                num = 0
            elif ope == '-':
                result -= num
                num = 0
            elif ope == 'x':
                result *= num
                num = 0
            elif ope == '÷':
                result /= num
                num = 0
            result_label['text'] = result
            result = 0
            ope = ''
        else:
            if ope == '':
                ope = i
                result += num
                num = 0
            else:
                if ope == '+':
                    result += num
                    num = 0
                    result_label['text'] = result
                elif ope == '-':
                    result -= num
                    num = 0
                    result_label['text'] = result
                elif ope == 'x':
                    result *= num
                    num = 0
                    result_label['text'] = result
                elif ope == '÷':
                    result /= num
                    num = 0
                    result_label['text'] = result
                ope = i

# def cal(event):
#     global flg
#     global ope
#     global num
#     global result

#     try:
#         i = int(event.widget['text'])
#         set_num(i)
#     except ValueError:
#         i = event.widget['text']

#         if i == '=':
#             if ope == '+':
#                 result += num
#                 num = 0
#             elif ope == '-':
#                 result -= num
#                 num = 0
#             elif ope == 'x':
#                 result *= num
#                 num = 0
#             elif ope == '÷':
#                 result /= num
#                 num = 0
#             result_label['text'] = result
#             result = 0
#             ope = ''
#         else:
#             if ope == '':
#                 ope = i
#                 result += num
#                 num = 0
#             else:
#                 if ope == '+':
#                     result += num
#                     num = 0
#                     result_label['text'] = result
#                 elif ope == '-':
#                     result -= num
#                     num = 0
#                     result_label['text'] = result
#                 elif ope == 'x':
#                     result *= num
#                     num = 0
#                     result_label['text'] = result
#                 elif ope == '÷':
#                     result /= num
#                     num = 0
#                     result_label['text'] = result
#                 ope = i

cnt = 9
#文字盤の配置(for文利用)#
for i in range(3):
    a = -2
    for j in range(3):
        btn_num = cnt + a   #ボタンの数字用
        num_btn = tk.Button(number_frame, text=btn_num, height='4', width='5', font=fonts, command=lambda x=btn_num : cal(x))
        num_btn.grid(column=j, row=i)
        cnt -= 1
        a += 2

num_btn = tk.Button(number_frame, text='0', height='4', width='13', font=fonts, command=lambda x=0 : cal(x))
num_btn.grid(column='0', row='3', columnspan='2')

equal_btn = tk.Button(number_frame, text='=', height='4', width='5', font=fonts, command=lambda x='=' : cal(x))
equal_btn.grid(column='2', row='3')

cnt = 3
for i in range(4):
    ope_btn = tk.Button(ope_frame, text=ope_list[cnt], height=4, width=5, font=fonts, command=lambda x=ope_list[cnt] : cal(x))
    ope_btn.grid(column=0, row=i)
    cnt -= 1


##文字盤の配置(手打ち)##

# num0_btn = tk.Button(number_frame, text='0', height='4', width='13', font=fonts)
# num0_btn.grid(column='0', row='3', columnspan='2')
# num0_btn.bind('<Button-1>', cal)

# equal_btn = tk.Button(number_frame, text='=', height='4', width='5', font=fonts)
# equal_btn.grid(column='2', row='3')
# equal_btn.bind('<Button-1>', cal)

# num1_btn = tk.Button(number_frame, text='1', height='4', width='5', font=fonts)
# num1_btn.grid(column='0', row='2')
# num1_btn.bind('<Button-1>', cal)

# num2_btn = tk.Button(number_frame, text='2', height='4', width='5', font=fonts)
# num2_btn.grid(column='1', row='2')
# num2_btn.bind('<Button-1>', cal)

# num3_btn = tk.Button(number_frame, text='3', height='4', width='5', font=fonts)
# num3_btn.grid(column='2', row='2')
# num3_btn.bind('<Button-1>', cal)

# num4_btn = tk.Button(number_frame, text='4', height='4', width='5', font=fonts)
# num4_btn.grid(column='0', row='1')
# num4_btn.bind('<Button-1>', cal)

# num5_btn = tk.Button(number_frame, text='5', height='4', width='5', font=fonts)
# num5_btn.grid(column='1', row='1')
# num5_btn.bind('<Button-1>', cal)

# num6_btn = tk.Button(number_frame, text='6', height='4', width='5', font=fonts)
# num6_btn.grid(column='2', row='1')
# num6_btn.bind('<Button-1>', cal)

# num7_btn = tk.Button(number_frame, text='7', height='4', width='5', font=fonts)
# num7_btn.grid(column='0', row='0')
# num7_btn.bind('<Button-1>', cal)

# num8_btn = tk.Button(number_frame, text='8', height='4', width='5', font=fonts)
# num8_btn.grid(column='1', row='0')
# num8_btn.bind('<Button-1>', cal)

# num9_btn = tk.Button(number_frame, text='9', height='4', width='5', font=fonts)
# num9_btn.grid(column='2', row='0')
# num9_btn.bind('<Button-1>', cal)

# ope_plas = tk.Button(ope_frame, text='+', height='4', width='5', font=fonts)
# ope_plas.grid(column='0', row='3')
# ope_plas.bind('<Button-1>', cal)

# ope_minus = tk.Button(ope_frame, text='-', height='4', width='5', font=fonts)
# ope_minus.grid(column='0', row='2')
# ope_minus.bind('<Button-1>', cal)

# ope_multi = tk.Button(ope_frame, text='x', height='4', width='5', font=fonts)
# ope_multi.grid(column='0', row='1')
# ope_multi.bind('<Button-1>', cal)

# ope_division = tk.Button(ope_frame, text='÷', height='4', width='5', font=fonts)
# ope_division.grid(column='0', row='0')
# ope_division.bind('<Button-1>', cal)


root.mainloop()
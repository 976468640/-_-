# stage 01
label = {
    '0': [],
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']}
list1 = input().split(",")
num = 0
for n in list1:
    num += 1
if num == 0:             # 当没有输入任何数时，输出空列表
    print([])
if num == 1:             # 当输入单个数时，输出对应数字的列表
    print(label[n])
if num == 2:             # 输入两个数时
    x = label[list1[0]]  # 初始化需要遍历的字母字符列表x和y
    y = label[list1[1]]
    record = []
    sum = 0
    for i in x:          # 记录每次组合相加得到的字符串
        for j in y:
            record.append(i+j)
            sum += 1
    for a in range(sum):
        print(record[a], end=" ")
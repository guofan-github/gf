list1 = ['1', 'a', 'b', '3', '5', '8', '_']
list2 = []
for i in list1:
    print(i, type(i))
    try:
        if int(i):
            list2.append(int(i))
    except Exception as e:
        print(f'{i}不能转为数字')
print(list2)

# list1 = ['1','a','b','3','5','8','_']
# list2 = []
# for i in list1:
#     if i.isnumeric():
#         list2.append(int(i))
# print(list2)

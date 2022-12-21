from itertools import product

list1 = [['张三', '男', '未婚', 20], ['李四', '男', '已婚', 28], ['小红', '女', '未婚', 18], ['小芳', '女', '已婚', 25]]

v = list(product(["甲子","甲午","甲乙"], repeat=2))
output = open('data.xls', 'w', encoding='utf-8')
# output.write('name\tgender\tstatus\tage\n')
for i in range(len(v)):
    for j in range(len(v[i])):
        output.write(str(v[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
        output.write('\t')  # 相当于Tab一下，换一个单元格
    output.write('\n')  # 写完一行立马换行
output.close()

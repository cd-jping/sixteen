from itertools import product

HSEB = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子', '丁丑',
        '戊寅',
        '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰',
        '癸巳',
        '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未',
        '戊申',
        '己酉', '庚戌', '辛亥', '壬子', '癸丑', '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌',
        '癸亥']

v = list(product(HSEB, repeat=3))
print(len(v))

output = open('data2.csv', 'w', encoding='utf-8')
output.write('name\n')
for i in v[0:1000]:
    for j in i:
        output.write(j)
        output.write(" ")
    output.write('\n')
output.close()

print(v[0])
print(v[1])
print(v[99])
print(v[100])
print(len(v[1000:5000]))

# for i in range(len(v)):
#     for j in range(len(v[i])):
#         output.write(str(v[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
#         # output.write(' ')  # 相当于Tab一下，换一个单元格
#     output.write('\n')  # 写完一行立马换行
# output.close()

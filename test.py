from itertools import product


def create_portfolio(list_item, filename, encrypt_suffx, filename_peffix, start: int, end: int):
    output = open(filename, 'w', encoding='utf-8')
    output.write('collection_name\tencrypt_name\n')
    for i in list_item[start:end]:
        output.write(filename_peffix)
        for j in i:
            output.write(j)
        output.write('\t')
        for j in i:
            output.write(j)
            # output.write(" ")
        output.write(encrypt_suffx)
        output.write('\n')
    output.close()


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
# 0-1000 (不含1000) 生成结果前1000个
create_portfolio(list_item=v, filename="河图币-1227-[0-1000].xlsx", encrypt_suffx="火", filename_peffix="河图币-", start=0, end=1000)
create_portfolio(list_item=v, filename="洛书币-1227-[0-1000].xlsx", encrypt_suffx="木", filename_peffix="洛书币-", start=0, end=1000)
create_portfolio(list_item=v, filename="先八卦币-1227-[0-1000].xlsx", encrypt_suffx="金", filename_peffix="先八卦币-", start=0, end=1000)
create_portfolio(list_item=v, filename="后八卦币-1227-[0-1000].xlsx", encrypt_suffx="水", filename_peffix="后八卦币-", start=0, end=1000)
create_portfolio(list_item=v, filename="太极币-1227-[0-1000].xlsx", encrypt_suffx="土", filename_peffix="太极币-", start=0, end=1000)


# output = open('data2.xlsx', 'w', encoding='utf-8')
# output.write('collection_name\tlayer_name\n')
# for i in v[0:1000]:
#     for j in i:
#         output.write(j)
#         output.write(" ")
#     output.write('火')
#     output.write('\t')
#     output.write('河图币-')
#     for j in i:
#         output.write(j)
#     output.write('\n')
# output.close()


# for i in range(len(v)):
#     for j in range(len(v[i])):
#         output.write(str(v[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
#         # output.write(' ')  # 相当于Tab一下，换一个单元格
#     output.write('\n')  # 写完一行立马换行
# output.close()

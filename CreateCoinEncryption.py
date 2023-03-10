
from itertools import product


def create_portfolio(list_item, filename, encrypt_prefix, filename_prefix, start: int, end: int):
    output = open(filename, 'w')
    output.write('collection_name,encrypt_name\n')
    for i in list_item[start:end]:
        output.write(filename_prefix)
        for j in i:
            output.write(j)
        output.write(',')
        output.write(encrypt_prefix)
        for j in i:
            output.write(j)
            # output.write(" ")

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
# print(len(v))

print(v[0+4999])
# 0-1000 (不含1000) 生成结果前1000个

# 铸造日志

# 癸卯金兔系列 0 - 5000

# 2023 01 01 (包含以前) 铸造 单币 500 套 0 - 100; 100 - 500
# 2023 01 05 铸造 20 个 套币 500 - 520
# 2023 01 09 铸造 500 套 单币 520 - 1020
# 2023 02 02 铸造 100 个 套币 1020 - 1120
# 2023 02 03 铸造 100 套 单币 1120 - 1220

# 四象呈瑞系列 5000 - ????

# 2023 02 08 铸造 100 套 单币 5000 - 5100



# 河洛文化币（套）
# create_portfolio(list_item=v, filename="河洛文化币（套）-0202-[1020-1120].csv", encrypt_prefix="", filename_prefix="河洛文化币（套）金-", start=1020, end=1120)

# # 河洛文化币（单币）
create_portfolio(list_item=v, filename="河图币-0208-[5000-5100].csv", encrypt_prefix="金", filename_prefix="河图币-金-", start=5000, end=5100)
create_portfolio(list_item=v, filename="洛书币-0208-[5000-5100].csv", encrypt_prefix="金", filename_prefix="洛书币-金-", start=5000, end=5100)
create_portfolio(list_item=v, filename="伏羲币-0208-[5000-5100].csv", encrypt_prefix="金", filename_prefix="伏羲币-金-", start=5000, end=5100)
create_portfolio(list_item=v, filename="文王币-0208-[5000-5100].csv", encrypt_prefix="金", filename_prefix="文王币-金-", start=5000, end=5100)
create_portfolio(list_item=v, filename="太极币-0208-[5000-5100].csv", encrypt_prefix="金", filename_prefix="太极币-金-", start=5000, end=5100)
#
# create_portfolio(list_item=v, filename="太极币-TEST-[4999-5000].csv", encrypt_prefix="金", filename_prefix="太极币-金-", start=4999, end=5000)


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

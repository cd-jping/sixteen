from itertools import permutations, combinations, combinations_with_replacement, product
import pandas as pd
a = list(range(10))
b = list(range(10))
c = list(range(10))

listfinal = a + b


# print(v)


def deal():
    # 列表
    company_name_list = ['腾讯', '阿里巴巴', '字节跳动', '腾讯']
    v = list(product(range(1, 61), repeat=3))
    # list转dataframe
    print(v)
    df = pd.DataFrame(v, columns=['company_name'])

    # 保存到本地excel
    df.to_excel("test.xlsx", index=False)


deal()



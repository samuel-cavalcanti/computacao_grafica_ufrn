import random

M = 100

N = 10
m_cores = range(M)


color_table = dict()

# criando tabela
for element in range(N):
    # valor de cinza entre 0 e 1[]
    color_table[element] = round(0.1*element, 5)


# exibindo tabela
for chave in color_table:
    print(f'{chave}:{color_table[chave]}')

#     red, blue, green
red = (1, 0, 0)

verde = (0, 1, 0)

cor = (0.23, 0.1, 0.25)

gray = (red[0] + red[1] + red[2])/3

gray_2 = (cor[0] + cor[1] + cor[2])/3




for _ in range(M):
    nova_cor = (random.random(), random.random(), random.random())
    gray_scale = (nova_cor[0] + nova_cor[1] + nova_cor[2])/3
    index = round(gray_scale * N, 0)
    print(f' gray: {gray_scale} index: {index}, color: {color_table[index]}')


# # 1 - N
# # x - y

# # y = x*N


# index = round(gray * N, 0)

# print("escala de cinza:", gray)
# print(f'index: {index}, color: {color_table[index]}')

# index = round(gray_2 * N, 0)

# print("escala de cinza:", gray_2)
# print(f'index: {index}, color: {color_table[index]}')

M = int(input("Сумма вклада"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = list(per_cent.values())
deposit = [L[0]*M/100, L[1]*M/100, L[2]*M/100, L[3]*M/100]
map(int, deposit)
print(deposit)
max_deposit = max(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max_deposit)

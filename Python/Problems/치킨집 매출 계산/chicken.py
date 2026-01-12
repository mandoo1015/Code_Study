day_and_price = []

with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        day_and_price.append(line.strip().split('일: '))


price_tot = 0
days = 0
for day, price in day_and_price:
    days = int(day)
    price_tot += int(price)

print(price_tot / days)

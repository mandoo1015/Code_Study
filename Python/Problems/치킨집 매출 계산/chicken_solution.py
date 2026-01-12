with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    revenue_tot = 0
    days = 0
    for line in f:
        data = line.strip().split('일: ')
        # [1, 453400], [2, 388600], ...
        revenue = data[1]   # 하루 매출 

        revenue_tot += int(revenue)
        days += 1

print(revenue_tot / days)

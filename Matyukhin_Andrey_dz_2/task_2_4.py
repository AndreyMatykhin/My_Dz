task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for emp in task_list:  # Будем перебирать список
    print(f'Привет, {emp.split()[-1].lower().title()}!')  # Выводим приветствие, дополняя его отредактированным именем
    # (последним словом в строке из заданого списка)

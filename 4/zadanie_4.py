a = int(input("Введите длину шоколадки - "))
b = int(input("Введите ширину шоколадки - "))
c = int(input("Введите количество долек, которыое вы хотите получить поделив шоколадку на 2 части - "))
if c%a==0 or c%b==0:
    print(f"От шоколадки с сторонами {a} и {b} - можно отломить {c} долек.")
else:
    print(f"От данной шоколадки с размером {a} на {b}, отломить {c} долек - нельзя.")

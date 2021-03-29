from datetime import  datetime

x = input("Введите время в формате 21:23 = ")
user_time=x.split(':')
h=int(user_time[0])
m=int(user_time[1])

dic_hour_r = {
    0: ["двенадцать часов", "первого", "час" ], 
    1: ["час", "второго",  "два"], 
    2: ["два часа", "третьего", "три"], 
    3: ["три часа", "четверого", "четыре" ], 
    4: ["четыречаса", "пятого", "пять"], 
    5: ["пять часа", "шестого", "шесть"],
    6: ["шесть часов", "седьмого", "семь"],
    7: ["семь часов", "восьмого", "восемь"], 
    8: ["восемь часов", "девятого", "девять"],
    9: ["девять часов", "десятого", "десять"], 
    10: ["десять часов", "одинадцатого", "одинадцать"], 
    11: ["одинадцать часов", "двенадцатого", "двенадцать"],
    12: ["двенадцать часов", "первого", "час"], 
    13: ["час", "второго", "два"], 
    14: ["два часа", "третьего", "три",], 
    15: ["три часа", "четверого", "четыре"],
    16: ["четыре часа", "пятого", "пять"], 
    17: ["пять часов", "шестого", "шесть"], 
    18: ["шесть часов", "седьмого", "семь"], 
    19: ["семь часов", "восьмого", "восемь"], 
    20: ["восемь часов", "девятого", "девять"],
    21: ["девять часов", "десятого", "десять"], 
    22: ["десять часов", "одинадцатого", "одинадцать"], 
    23: ["одинадцать часов", "двенадцатого", "двенадцать"],
    24: ["двенадцать часов", "первого", "час"]
    }

dic_min_p={0 : "Ровно", 1 : "Одна минута", 2 : "Две минуты", 3 : "Три минуты", 4 : "Четыре минуты",
5 : "Пять минут", 6 : "Шесть минут", 7 : "Семь минут", 8 : "Восемь минут", 9 : "Девять минут",
10 : "Десять минут", 11 : "Одиннадцать минут", 12 : "Двенадцать минут", 13 : "Тринадцать минут",
14 : "Четырнадцать минут", 15 : "Пятнадцать минут", 16 : "Шеснадцать минут", 17 : "Семнадцать минут",
18 : "Восемнадцать минут", 19 : "Девятнадцать минут", 20 : "Двадцать минут", 21 : "Двадцать одна минута",
22 : "Двадцать две минуты", 23 : "Двадцать три минуты", 24 : "Двадцать четыре минуты",
25 : "Двадцать пять минут", 26 : "Двадцать шесть минут", 27 : "Двадцать семь минут",
28 : "Двадцать восемь минут", 29 : "Двадцать девять минут", 30 : "Половина", 31 : "Тридцать одна минута",
32 : "Тридцать две минуты", 33 : "Тридцать трими нуты", 34 : "Тридцать четыре минуты",
35 : "Тридцать пять минут", 36 : "Тридцать шесть минут", 37 : "Тридцать семь минут",
38 : "Тридцать восемь минут", 39 : "Тридцать девять минут", 40 : "Без двадцати",
41 : "Без девятнадцати", 42 : "Без восемнадцати", 43 : "Без семнадцати", 44 : "Без шеснадцати",
45 : "Без пятнадцати", 46 : "Без четырнадцати", 47 : "Без тринадцати", 48 : "Без двенадцати",
49 : "Без одинадцати", 50 : "Без десяти", 51 : "Без девяти", 52 : "Без восьми", 53 : "Без семи",
54 : "Без шести", 55 : "Без пяти", 56 : "Без четырех", 57 : "Без трех", 58 : "Без двух", 59 : "Без одной"}




if (m==0 and h>=0 and h<=24):
    rezult=str(dic_min_p[m])+" "+str(dic_hour_r[h][0])

elif (m==30 and h>=0 and h<=24):
    rezult=str(dic_min_p[m])+" "+str(dic_hour_r[h][1])

elif (m>=1 and m<=29 and h>=0 and h<=24):
    rezult=str(dic_min_p[m])+" "+str(dic_hour_r[h][1])

elif (m>=31 and m<=39 and h>=0 and h<=24):
    rezult=str(dic_min_p[m])+" "+str(dic_hour_r[h][1])

elif (m>=40 and m<=59 and h>=0 and h<=24):
    rezult=str(dic_min_p[m])+" "+str(dic_hour_r[h][2])

else: 
    rezult="Неверный формат времени!"



print("Время введенное пользователям строчно :", rezult)


curr_sys= datetime.now().strftime("%H:%M")
print("Текущее время :", curr_sys)
curr_sys=curr_sys.split(':')
h_sys=int(curr_sys[0])
m_sys=int(curr_sys[1])



if (m_sys==0 and h_sys>=0 and h_sys<=24):
    rezult_sys=str(dic_min_p[m_sys])+" "+str(dic_hour_r[h_sys][0])

elif (m_sys==30 and h_sys>=0 and h_sys<=24):
    rezult_sys=str(dic_min_p[m_sys])+" "+str(dic_hour_r[h_sys][1])

elif (m_sys>1 and m_sys<=29 and h_sys>=0 and h_sys<=24):
    rezult_sys=str(dic_min_p[m_sys])+" "+str(dic_hour_r[h_sys][1])

elif (m_sys>31 and m_sys<=39 and h_sys>=0 and h_sys<=24):
    rezult_sys=str(dic_min_p[m_sys])+" "+str(dic_hour_r[h_sys][1])

elif (m_sys>40 and m_sys<=59 and h_sys>=0 and h_sys<=24):
    rezult_sys=str(dic_min_p[m_sys])+" "+str(dic_hour_r[h_sys][2])

else: 
    rezult_sys="Неверный формат времени!"



print("Текущее время строчно :", rezult_sys)
words = ["рыжая",
         "lisa",
         "prignyla",
         "cerez",
         "golovy"]
one = " ".join(words)
print(one)
print("*".join("abc")) #join - символы между символами в строке

s = "    Москва    "
print(s.strip()) #strip - удаление пробелов в начале и конце

print("hello {}".format("kolya")) #format - str вместо {}

equ = 'Все животные одинаковые'
print(equ.replace('о','&')) #replace - заменяет один символ на другой в строке

try:
    "Животные".index("з") # индекс первого вхождения символа
except:
    print("не обнаружено.")

print("kot" in "kot v meshke") # in проверяет содержится ли строка в другой строке
    
#срез str[i:j] - str с i-го до j-го
ivan = """Петр Иванович успокоился и с интересом стал
          расспрашивать подробности о кончине Ивана Ильича."""
print(ivan[0:24]) #~[:24]
print(ivan[24:93]) #~[24:]
print(ivan[:]) 

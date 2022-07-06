import os
#нужен для создания пути к файлу в разных операционых системах

s = os.path.join("users","remwyare","st.txt") #"/".join(...) ?
print(s)

st = open("st.txt", "w") # w - запись
st.write("Привет от Python!")
st.close()

with open("st.txt", "w") as f: # автоматическое закрытие файла
    f.write("1 Привет от Python!\n")
    f.write("2 Привет!")


with open("st.txt", "r") as f: # r - чтение
    print(f.read()) # read - возвращает итерируемый обект со всеми символами
                    # вызвать read можно только 1 раз

my_list = []
with open("st.txt", "r") as f:
    for s in f.read():
        my_list.append(s)
        

print(my_list)    

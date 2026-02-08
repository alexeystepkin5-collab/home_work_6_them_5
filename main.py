# Дедлайн Срок сдачи – 09.02.2026
#
# Задание
# Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
#
# The Moscow Times — Wednesday, October 2, 2002
# The Guardian — Friday, 11.10.13
# Daily News — Thursday, 18 August 1977
#
# Принципы работы программы:
#
# Программа должна выводить на экран объекты типа datetime, соответствующие датам в условии задачи.
# Также программа должна работать итерационно, а именно: принимать входные данные до момента ввода специального символа завершения программы.
# Если введённое значение не соответствует ни одному формату, то следует продолжать выполнение программы, переходя на следующую итерацию.
# Безопасный переход следует реализовать с помощью механизма исключений.

from datetime import datetime as dt

# print(dt.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y' ))
# print(dt.strptime('Friday, 11.10.13', '%A, %d.%m.%y' ))
# print(dt.strptime('Thursday, 18 August 1977', '%A, %d %B %Y' ))

print ('The Moscow Times — Wednesday, October 2, 2002')
print ('The Guardian — Friday, 11.10.13')
print ('Daily News — Thursday, 18 August 1977')

#date_string = ''
#magazine_is = ''
# трай эксепт надо засунуть в функцию и вызывать ее в случае эксепт, если это не ключ выхода.

try:
    date_string = input('Введите дату: ')
    formated_date = dt.strptime(date_string, '%A, %B %d, %Y')
    magazine_is = 'The Moscow Times'
except:
    #print('неизвестный формат даты')
    try:
        formated_date = dt.strptime(date_string, '%A, %d.%m.%y')
        magazine_is = 'The Guardian'
    except:
        #print('неизвестный формат даты')
        try:
            formated_date = dt.strptime(date_string, '%A, %d %B %Y')
            magazine_is = 'Daily News'
        except:
            print('неизвестный формат даты')
        else:
            print(magazine_is)
            print(formated_date)
    else:
        print(magazine_is)
        print(formated_date)
else:
    print (magazine_is)
    print (formated_date)
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

print ('The Moscow Times — Wednesday, October 2, 2002')
print ('The Guardian — Friday, 11.10.13')
print ('Daily News — Thursday, 18 August 1977')


date_format = ['%A, %B %d, %Y', '%A, %d.%m.%y', '%A, %d %B %Y']
global date_index

date_index = 0

def date_trial(date_string, date_format, date_index):
    try:
        formated_date = dt.strptime(date_string, date_format[date_index])
        magazine_is = 'Daily News'
    except:
        if date_index < 2:
            date_index += 1
            date_trial(date_string, date_format, date_index)
        else:
            print('неизвестный формат даты')
            return 0
    else:
        #print(magazine_is)
        print(formated_date)
        return 1
returned = 1
while (returned):
    date_string = input('Введите дату, для завершения введите exit: ')
    if date_string == 'exit':
        returned = 0
    else:
        date_trial(date_string, date_format, date_index)


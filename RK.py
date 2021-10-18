# используется для сортировки
from operator import itemgetter
 
#«Книга» и «Глава» связаны соотношением один-ко-многим. 
# Выведите список всех Книг, у которых название начинается 
# с буквы «А» и список глав.

#«Книга» и «Глава» связаны соотношением один-ко-многим. 
# Выведите список Книг с максимальным числом страниц несколько глав вместе взятых в каждой книге, 
# отсортированной по максимальной страниц



class Emp:
    """Сотрудник"""
    def __init__(self, id, name1, stra, number):
        self.id = id
        self.name1 = name1
        self.stra = stra
        self.number = number
        #self.dep_id = dep_id
 
class Dep:
    """Отдел"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class EmpDep:
    """
    'Сотрудники отдела' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, id, emp_id):
        self.id = id
        self.emp_id = emp_id
 
# Книги
deps = [
    Dep(1, 'Пхеньян'),
    Dep(2, 'Программирование с нуля'),
    Dep(3, 'Америка'),
    Dep(4, 'Автоматизация'),
    Dep(5, 'C#'),
    Dep(6, 'Навальный'),
]
 
# Главы
emps = [
    Emp(1, 'Начало', 2, 1),
    Emp(2, 'Начало', 2, 1),
    Emp(3, 'Начало', 2, 1),
    Emp(4, 'Начало', 2, 1),
    Emp(5, 'Начало', 2, 1),
    Emp(6, 'Начало', 2, 1),
    Emp(1, 'История', 11, 2),
    Emp(2, 'История', 9, 2),
    Emp(3, 'История', 13, 2),
    Emp(3, 'Местоположение', 18, 2),
    Emp(2, 'Заключение', 50, 6),
    Emp(5, 'Ведение', 1, 0),

]
 
emps_deps = [
    EmpDep(1,1),
    EmpDep(2,2),
    EmpDep(3,3),
    EmpDep(3,4),
    EmpDep(3,5),
 
    EmpDep(11,1),
    EmpDep(22,2),
    EmpDep(33,3),
    EmpDep(33,4),
    EmpDep(33,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(d.name, e.stra, e.name1) 
        for d in deps 
        for e in emps 
        if e.id==d.id
        ]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.id, ed.emp_id) 
        for d in deps 
        for ed in emps_deps 
        if d.id==ed.id]
    

    
    many_to_many = [(dep_name, e.stra, e.name1) 
        for dep_name, id, emp_id in many_to_many_temp
        for e in emps if e.id==emp_id]
 
    print('Задание Г1')
    res_11 = {}
    selected_emps = [one_traicour[0] for one_traicour in one_to_many if one_traicour[0].startswith('а') or one_traicour[0].startswith('А')]
    for emps_name in selected_emps:
        deps_for_traicour = [(one_deps[2],one_deps[1]) for one_deps in one_to_many if one_deps[0]==emps_name]
        res_11.update({emps_name:deps_for_traicour})
        print(res_11)

    print('\nЗадание Г2')
    res_12_unsorted = []
    for s in emps:
        s_deps = list(filter(lambda i: i[2]==s.name1, one_to_many))
        if len(s_deps) > 0:
            s_prices = [price for _,price,_ in s_deps]
            s_price_max = max(s_prices)
            res_12_unsorted.append((s.name1, s_price_max))
            res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
            print(res_12)
 
    print('\nЗадание Г3')
    res_13 = {}
    emps.sort(key=lambda one_emps: one_emps.name1)
    for s in emps:
        s_deps = list(filter(lambda i: i[2]==s.name1, many_to_many))
        s_deps_names = [x for x,_,_ in s_deps]
        res_13[s.name1] = s_deps_names
        print(res_13)
 
if __name__ == '__main__':
    main()

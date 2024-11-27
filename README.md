--------------------------------------------------------------------------------
Задание №3  
Разработать инструмент командной строки для учебного конфигурационного языка,  
синтаксис которого приведен далее. Этот инструмент преобразует текст из  
входного формата в выходной. Синтаксические ошибки выявляются с выдачей  
сообщений.  
Входной текст на языке json принимается из файла, путь к которому задан  
ключом командной строки. Выходной текст на учебном конфигурационном языке  
попадает в стандартный вывод. Однострочные комментарии:  
REM Это однострочный комментарий  
Словари:  
{  
 имя = значение  
 имя = значение  
 имя = значение  
 ...  
}  
Имена:  
[_a-zA-Z]+  
26  
Значения:  
• Числа.  
• Строки.  
• Словари.  
Строки:  
"Это строка"  
Объявление константы на этапе трансляции:  
var имя = значение  
Вычисление константы на этапе трансляции:  
$(имя)  
Результатом вычисления константного выражения является значение.  
Все конструкции учебного конфигурационного языка (с учетом их  
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3  
примера описания конфигураций из разных предметных областей.  
--------------------------------------------------------------------------------
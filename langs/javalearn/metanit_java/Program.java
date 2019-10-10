public class Program{

    public static void main (String args[]){

        System.out.println("Hello Java!");
    }
}

// Программа представляется в виде набора взаимодействующих классов.

// При определении класса вначале идет модификатор доступа public,
// который указывает, что данный класс будет доступен всем, то есть мы
// сможем его запустить из командной строки.  Далее идет ключевое слово
// class, а затем название класса. То есть класс называется Program.
// После названия в фигурных скобках расположено содержимое класса.

// Класс может содержать различные переменные и методы.  В данном случае
// у нас объявлен один метод main.  Это главный метод в любой программе
// на Java, он является входной точкой программы и с него начинается все
// управление.  Он обязательно должен присутствовать в программе.

// Метод main также имеет модификатор public.  Слово static указывает,
// что метод main - статический, а слово void - что он не возвращает
// никакого значения.

// Далее в скобках идут параметры метода - String args[] - это массив
// args, который хранит значения типа String, то есть строки.  В данном
// случае ни нам пока не нужны, но в реальной программе это те строковые
// параметры, передающиеся при запуске программы из командной строки.

// После списка параметров в фигурных скобках идет тело метода - это те
// инструкции, что будет выполнять метод.  В данном случае определена
// одна инструкция - вывод на консоль некоторой строки.  Для вывода на
// консоль используется встроенный метод System.out.println().  В этот
// метод передается выводимая строка.  Каждая инструкция завершается
// точкой с запятой.  Только один public class и имя должно совпадать с
// названием файла.
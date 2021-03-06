package tenums;

class Book{

    String name;
    Type bookType;
    String author;
    int year;

    Book(String name, String author, int year, Type type){

        bookType = type;
        this.name = name;
        this.author = author;
        this.year = year;
    }
}

// Кроме отдельных примитивных типов данных и классов в Java есть такой тип
// как enum или перечисление. Перечисления представляют набор логически
// связанных констант. Объявление перечисления происходит с помощью оператора
// enum, после которого идет название перечисления. Затем идет список
// элементов перечисления через запятую:

enum Type
{
    SCIENCE,
    BELLETRE,
    PHANTASY,
    SCIENCE_FICTION
}

// Само перечисление объявлено вне класса, оно содержит четыре жанра книг.
// Класс Book кроме обычных переменных содержит также переменную типа нашего
// перечисления. В конструкторе мы ее также можем присвоить, как и обычные
// поля класса.
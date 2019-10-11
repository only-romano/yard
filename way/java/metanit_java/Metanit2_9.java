import java.util.Scanner;

public class Metanit2_9{
    public static void main(String[] args){

    // Консольный ввод/вывод.

        // Для создания потока вывода в класс System определен объект out.
        // В этом объекте определен метод println, который позволяет
        // вывести на консоль некоторое значение с последующим переводом
        // консоли на следующую строку:

        System.out.println("Hello world");

        System.out.print("Without new line");


    // B Java есть также функция для форматированного вывода,
    // унаследованная от языка С: System.out.printf(). С ее помощью мы
    // можем переписать предыдущий пример следующим образом:

        int x=5;
        int y=6;
        System.out.printf("x=%d; y=%d \n", x, y);  // перевод с помощью \n.

    // В данном случае символы %d обозначают спецификатор, вместо которого
    // подставляет один из аргументов.  Спецификаторов и соответствующих им
    // аргументов может быть множество.  В данном случае у нас только два
    // аргумента, поэтому вместо первого %d подставляет значение переменной x,
    // а вместо второго - значение переменной y.  Сама буква d означает, что
    // данный спецификатор будет использоваться для вывода целочисленных
    // значений типа int.

    // Кроме спецификатора %d мы можем использовать еще ряд спецификаторов
    // для других типов данных:
        // .. %x: для вывода шестнадцатеричных чисел.
        // .. %f: для вывода чисел с плавающей точкой.
        // .. %e: для вывода чисел в экспоненциальной форме.
        // .. %c: для вывода одиночного символа.
        // .. %s: для вывода строковых значений.

        String name = "Nван";
        int age = 30;
        float height = 1.7f;

        System.out.printf("Nмя: %s   Возраст: %d лет   Рост: %.2f метров \n", name, age, height);


        // Класс Scanner имеет еще ряд методов, которые позволяют получить
        // введенные пользователем значения:
        // .. next(): считывает введенную строку до первого пробела.
        // .. nextLine(): считывает всю введенную строку.
        // .. nextInt(): считывает введенное число int.
        // .. nextDouble(): считывает введенное число double.
        // .. hasNext(): проверяет, было ли введено слово.
        // .. hasNextInt(): проверяет, было ли введено число int.
        // .. hasNextDouble(): проверяет, было ли введено double.

        // Кроме того, класс Scanner имеет еще ряд методов
        // nextByte/nextShort/nextFloat/nextBoolean, которые по аналогии с
        // nextInt считывают данные определенного типа данных.

        Scanner in2 = new Scanner(System.in);
        System.out.print("Введите имя: ");
        String name2 =  in2.nextLine();
        System.out.print("Введите возраст: ");
        int age2 = in2.nextInt();
        System.out.println("Ваше имя: " + name2 + "\tВаш возраст: " + age2);

        Scanner in = new Scanner(System.in);
        int[] nums = new int[5];
        for(int i=0;i < nums.length; i++){
            nums[i]=in.nextInt();
            // чтобы получить введенное число, используется метод in.nextInt();
            // который возвращает введенное с клавиатуры целочисленное значение.
        }

        for(int i=0;i < nums.length; i++){
            System.out.print(nums[i]);
        }

        System.out.println();
    }
}
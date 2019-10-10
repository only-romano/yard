package metanit;

// Если нам надо использовать классы из других пакетов, то нам надо
// подключить эти пакеты и классы.  Nсключение составляют классы из
// пакета java.lang (например, String), которые подключаются в
// программу автоматически.

import java.util.*;  // Nмпорт всех классов из пакета java.util.

// В java есть также особая форма импорта - статический импорт. Для
// этого вместе с директивой import используется модификатор static:

import static java.lang.Math.*;
import static java.lang.System.*;

// Здесь происходит статический импорт классов System и Math. Эти классы
// имеют статические методы.  Благодаря операции статического импорта мы
// можем использовать эти методы без названия класса.

public class Metanit3_2{

    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        // Альтернатива без импорта для автоматических пакетов:
        // java.util.Scanner in = new java.util.Scanner(System.in);

        // Возможна ситуация, когда мы используем два класса с одним
        // и тем же названием из двух разных пакетов, например, класс
        // Date имеется и в пакете java.util, и в пакете java.sql. N
        // если нам надо одновременно использовать два этих класса,
        // то необходимо указывать полный путь к этим классам в пакете:
        // java.util.Date utilDate = new java.util.Date();
        // java.sql.Date sqlDate = new java.sql.Date();

        // Например, писать не Math.sqrt(20), а sqrt(20), так как функция
        // sqrt(), которая возвращает квадратный корень числа, является
        // статической.  То же самое в отношении класса System: в нем
        // определен статический объект out, поэтому мы можем его
        // использовать без указания класса:
        double result = sqrt(20);
        out.println(result);

    }
}
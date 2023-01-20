# Домашнее задание к лекции «Python и БД. ORM»

## Задание 1

Составить модели классов SQLAlchemy по схеме:

![image](https://user-images.githubusercontent.com/47860117/213794823-c16a0592-5573-4d25-bdfb-1a677482fb4f.png)

Легенда: система хранит информацию об издателях (авторах), их книгах и фактах продажи. Книги могут продаваться в разных магазинах, поэтому требуется учитывать не только, что за книга была продана, но и в каком магазине это было сделано, а также когда.

Интуитивно необходимо выбрать подходящие типы и связи полей.

## Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

- Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
- Импортирует необходимые модели данных.
- Принимает имя или идентификатор издателя (publisher), например через `input()`. Выводит построчно факты покупки книг этого издателя:

```
название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки
```

Пример (было введено имя автора - `Пушкин`):

```
Капитанская дочка | Буквоед     | 600 | 09-11-2022
Руслан и Людмила  | Буквоед     | 500 | 08-11-2022
Капитанская дочка | Лабиринт    | 580 | 05-11-2022
Евгений Онегин    | Книжный дом | 490 | 02-11-2022
Капитанская дочка | Буквоед     | 600 | 26-10-2022
```

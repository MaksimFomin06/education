// console.log("Вывод в консоль")
// alert("Привет");
// prompt("Введите число")
// confirm("Вы согласны?")

let number = 5; // let - обычное создание переменной
let num = 5,
  str = "Hello";
num = 10;
str = prompt("Введите текст");
const num2 = 5; // const Нельзя изменять

const username = "Павел"; // flat
const userName = "Павел"; // camel case
const user_name = "Павел"; // snake case
const UserName = "Павел"; // Pascal case
// const user-name = "Павел" // kebab case

// Строгий режим: в начале  кода написать "use strict";

// Типы данных
// Неизменяемые (immutable) (примитивные)
// number - число
// string - строка
// boolean - булев тип
// bigInt - большое целое число
// symbol - символ
// undefined - undefined
// null - null
// Изменяемые
// object - составной

// Определение типа элемента
// typeof не использовать, устарел
const data = 1;
console.log(typeof data); // number

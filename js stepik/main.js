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

// Тип number
const million = 1_000_000;
const million2 = 1e6;
const million3 = 1e-6; // 0.000001
const million4 = 1e-7; // 1e-7 Так как в JS болште числа так сокращаются

// infinity
const num3 = 1e1000; // infinity

// Проверка что число конечное
console.log(Number.isFinite(num3));

// NaN
const num4 = 50 / "hello";
console.log(num4); // NaN

// Числа в строку
const num5 = 52;
console.log(num.toString()); // "52"
console.log(num.toString(2)); // 110100 двоичная система счисления
console.log(num + ""); // "52"

// Строки в числа
const str2 = "52.86";
console.log(+str); // 52.86
console.log(Number(str)); // 52.86
console.log(Number.parseInt(str)); // 52
const num6 = "54.2ru4b";
console.log(Number.parseInt(num6)); // 54
console.log(Number.parseFloat(num6)); // 54.2

// Округление
console.log(Math.round(24.43)); // 24
console.log(Math.round(24.88)); // 25
console.log(Math.floor(24.88)); // 24
console.log(Math.ceil(24.43)); // 25
console.log(Math.trunc(24.43)); // 24 - Просто отбрасывает дробную часть
console.log(Math.trunc(24.4367 * 100) / 100); // 24.44

// Max min
console.log(Math.max(2, 5, -4, 0));
console.log(Math.min(2, 5, -4, 0));

// Random
console.log(Math.random()); // Случайное число от нуля до единицы, ничего не принимает на вход
console.log(Math.floor(Math.random() * (max - min + 1) + min)); // Рандомное число в диапазоне от min до max включительно

// Строки
console.log("У меня есть " + count + " яблок");
console.log("У меня есть " + count + " яблок");
console.log(`У меня есть ${count} яблок`);
const str3 = `
1
2
3
`;

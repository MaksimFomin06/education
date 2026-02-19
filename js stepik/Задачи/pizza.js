const size = "большая";

let work_size;

if (size === null || size === undefined) {
  console.log("Вы не выбрали размер!");
} else {
  work_size = size.trim().toLowerCase();

  if (work_size === "маленькая") {
    console.log("Маленькая пицца стоит 800 руб.");
  } else if (work_size === "средняя") {
    console.log("Средняя пицца стоит 1200 руб.");
  } else if (work_size === "большая") {
    console.log("Большая пицца стоит 1500 руб.");
  } else {
    console.log("Такого размера у нас нет!");
  }
}

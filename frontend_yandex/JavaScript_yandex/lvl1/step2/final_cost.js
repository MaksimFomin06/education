const basePrice = "1000";
const discountPercent = "15";
const bonusPoints = "50";

const discount = (Number(basePrice) * Number(discountPercent)) / 100;
priceWithDiscount = Number(basePrice) - discount;
finalPrice = priceWithDiscount - Number(bonusPoints);

console.log(finalPrice);

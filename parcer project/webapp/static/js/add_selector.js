function addSelector() {
  const container = document.querySelector(".selector-container");
  const firstRow = container.querySelector(".selector-row");

  const newRow = firstRow.cloneNode(true);

  newRow.querySelectorAll("input").forEach((input) => {
    input.value = "";
  });
  container.appendChild(newRow);
}

function addRequirement() {
  const container = document.querySelector(".requirements-container");
  const firstRow = container.querySelector(".requirements-row");

  const newRow = firstRow.cloneNode(true);

  newRow.querySelectorAll("input").forEach((input) => {
    input.value = "";
  });

  container.appendChild(newRow);
}

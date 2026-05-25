let calculation = localStorage.getItem("calculation") || "";

displayCalculation();

function updateCalculation(value) {
  calculation += value;
  displayCalculation();

  localStorage.setItem("calculation", calculation);
}

function displayCalculation() {
  document.querySelector(".js-calculation").innerHTML = calculation;
}

/*
function setCalulation() {
    localStorage.setItem('calculation', calculation);
}
*/

// 2026.05.25 23:32

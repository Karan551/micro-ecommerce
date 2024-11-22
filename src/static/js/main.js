const currentYear = new Date().getFullYear();

const year = document.getElementById("year");
year.innerHTML = currentYear + " - " + (currentYear + 1);

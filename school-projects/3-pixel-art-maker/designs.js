// Select size input
const userInput = document.querySelector('#sizePicker'); //form
const grid = document.querySelector('#pixelCanvas'); //table
const gridRow = document.querySelector('#inputHeight'); //tr
const gridCell = document.querySelector('#inputWidth'); //td


// When size is submitted by the user, call makeGrid()
userInput.addEventListener('submit', function(changeGridSize) {
  changeGridSize.preventDefault(); //prevent grid from defaulting to value of 1 
  grid.textContent = ""; //reset grid
  makeGrid(); //create the number of rows and cells based on user input
});

function makeGrid() {
  for (let r = 0; r < gridRow.value; r++) {
    const row = document.createElement('tr');
    for (let c = 0; c < gridCell.value; c++) {
      const cell = document.createElement('td');
      row.appendChild(cell)
    }
    grid.appendChild(row)
  }
};


// Select color input
// When table cell is clicked, call changeColor()
const colorSelect = document.querySelector('#colorPicker');
grid.addEventListener('click', function(changeColor) {
  if (changeColor.target.nodeName === 'TD') { // when a cell is clicked, change cell color
    changeColor.target.style.backgroundColor = colorSelect.value;
  }
});
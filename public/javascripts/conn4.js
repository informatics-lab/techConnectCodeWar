
gametype = 'conn4' // declared in game.js
const X = 'X';
const Y = 'Y';
const COLS = 7;
const ROWS = 6;
const NONE = '-';
var state = (NONE.repeat(COLS) + '\n').repeat(ROWS);



function rowColToRef(row, col){
  let rowLetter = 'ABCDEFG'[row];
  return [col, rowLetter];
}

function checkAndMakeMove(e){
  e.preventDefault();
  try {
    let player = document.getElementById('player').value.toUpperCase();
    let move = parseInt(document.getElementById('move').value, 10);
    makeMove(move, player);
  } catch(e){
    alert('Bad move or something went wrong!');
  }
}

function getFirstAvaliableRow(col){
  for (let row=0; row < ROWS; row++){
    let value = state[cellToStateIndex(row, col)]
    if (value == NONE) {
      return row;
    }
  }
  throw "Illegal move col full.";
}

function cellToStateIndex(row, col){
  return col + (COLS + 1) * ( ROWS - 1 - row);
}

function updatedState(col, row, player){
  let index = cellToStateIndex(row, col);
  return state.substr(0, index) + player + state.substr(index + 1);
}

function makeMove(col, player){
  let row = getFirstAvaliableRow(col);
  state = updatedState(col, row, player);
  showState();
  update();
  sendState();
}

function update(){
  const ximg = "<img src='/images/x.svg' class='cell-mark' alt='X'>";
  const oimg = "<img src='/images/o.svg' class='cell-mark' alt='O'>";
  for (let row=0; row<ROWS; row++){
    for (let col=0; col<COLS; col++){
      let id = 'state-' + String(rowColToRef(row, col));
      let ele = document.getElementById(id);
      let index = cellToStateIndex(row, col);
      if (state[index] != NONE){
        ele.innerHTML = (state[index] == X)? ximg : oimg;
      }
    }
  }
}


function buildBoard(){

  function newRow(container){
    let row = document.createElement('div');
    row.className ='row';
    container.appendChild(row);
    return row;
  }

  let container = document.getElementById('game');

  for (let row=ROWS-1; row>=0; row--){
    rowContainer = newRow(container);
    for (let col=0; col<COLS; col++){
      let cell = document.createElement('div');
      cell.id = String(rowColToRef(row, col));
      cell.innerHTML = '<p class="ref">'+cell.id+'</p><div class="cell-state" id="state-'+cell.id+'"></div>';
      cell.className = 'cell col-xs-1';
      rowContainer.appendChild(cell);
    }
  }
  setInterval(scaleCellsVertically, 200);

}

function scaleCellsVertically(){
  let cells = document.getElementsByClassName('cell');
  for (var i = 0; i < cells.length; i++) {
    let cell = cells[i];
    cell.style.height = cell.clientWidth + 'px';
  }
}



buildBoard();
showState();
document.getElementById('controls').addEventListener('submit', checkAndMakeMove, false)

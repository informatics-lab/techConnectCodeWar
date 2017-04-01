/*
   0 1 2
A |_|_|_|
B |_|_|_|
C |_|_|_|
*/
gametype = 'xandos' // declared in game.js
const X = 'X';
const Y = 'Y';
const NONE = '-';
var state = NONE.repeat(9);


function cellNumToRef(i){
  let col = (i % 3)
  let row = 'ABC'[Math.floor(i/3)];
  return [col, row];
}

function checkAndMakeMove(e){
  e.preventDefault();
  try {
    let player = document.getElementById('player').value.toUpperCase();
    let move = document.getElementById('move').value.toUpperCase().replace(/[ )(]/g,'').split(',');
    move[0] = Number(move[0]);
    makeMove(move, player);
  } catch(e){
    alert('Bad move or something went wrong!');
  }
}

function makeMove(move, player){
  let index = moveToStateIndex(move);
  if(state[index] !== NONE){
    throw {msg:'Illegal Move', 'move':move};
  }
  state = state.substr(0, index) + player + state.substr(index + 1);
  showState();
  update();
  sendState();
}

function update(){
  const ximg = "<img src='/images/x.svg' class='cell-mark' alt='X'>";
    const oimg = "<img src='/images/o.svg' class='cell-mark' alt='O'>";
  for (let i=0; i<9; i++){
    let id = 'state-' + String(cellNumToRef(i));
    let ele = document.getElementById(id);
    if (state[i] != NONE){
      ele.innerHTML = (state[i] == X)? ximg : oimg;
    } else {
      ele.innerHTML = '';
    }

  }
}

function moveToStateIndex(move){
  col = move[0];
  row = {'A':0, 'B':1, 'C':2}[move[1]];
  return col + row * 3;
}


function buildBoard(){

  function newRow(container){
    let row = document.createElement('div');
    row.className ='row';
    container.appendChild(row);
    return row;
  }

  let container = document.getElementById('game');
  let row = newRow(container);
  for (let i=0; i<9; i++){
    if (i % 3 == 0){
      row = newRow(container);
    }
    let cell = document.createElement('div');
    cell.id = String(cellNumToRef(i));
    cell.innerHTML = '<p class="ref">'+cell.id+'</p><div class="cell-state" id="state-'+cell.id+'"></div>';
    cell.className = 'cell col-xs-4';
    row.appendChild(cell);
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

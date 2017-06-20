const X = 'X';
const O = 'O';
const COLS = 7;
const ROWS = 6;
const NONE = '-';
const EMPTY_STATE = (NONE.repeat(COLS) + '\n').repeat(ROWS);

var state = "";


var get = () => state;
var set = newState => state = newState;
var reset = () => set(EMPTY_STATE);


reset();
module.exports = {
    get: get,
    set: set,
    X: X,
    O: O,
    COLS: COLS,
    ROWS: ROWS,
    NONE: NONE,
    reset: reset
};
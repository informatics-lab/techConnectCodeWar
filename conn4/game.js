const state = require('./state');


function getFirstAvaliableRow(col) {
    for (let row = 0; row < state.ROWS; row++) {
        let value = state.get()[cellToStateIndex(row, col)]
        if (value == state.NONE) {
            return row;
        }
    }
    throw "Illegal move col full.";
}

function cellToStateIndex(row, col) {
    return col + (state.COLS + 1) * (state.ROWS - 1 - row);
}

function updatedState(col, row, player) {
    let index = cellToStateIndex(row, col);
    return state.get().substr(0, index) + player + state.get().substr(index + 1);
}

function play(player, col) {
    if (player.toUpperCase() == state.X) {
        player = state.X
    } else if (player.toUpperCase() == state.O) {
        player = state.O;
    }
    let row = getFirstAvaliableRow(col);
    var newState = updatedState(col, row, player);
    state.set(newState);
}

module.exports = {
    play: play,
    state: state,
    reset: state.reset
};
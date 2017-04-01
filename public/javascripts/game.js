

// socket
let gametype = 'game';

var socket = io.connect(location.protocol + '//' + location.host);
socket.on('state', function (data) {
  console.log('got state ', data);
  if(data[gametype] && data[gametype] != state){
    state = data[gametype];
    update();
    showState();
  }
});

function sendState(){
  console.log('send state ', state);
  let msg = {};
  msg[gametype] = state;
  socket.emit('stateUpdate', msg);
}


function showState(){
  document.getElementById('state-code').innerHTML = state;
}


function showControls(){
  document.getElementById('controls').style.display = 'block'
  document.getElementById('update').style.display = 'block'
}


document.getElementById('update').addEventListener('click', sendState, false)

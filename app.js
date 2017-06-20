var express = require('express');
var path = require('path');

var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var http = require('http');

var index = require('./routes/index');
var users = require('./routes/users');
var xandos = require('./routes/xandos');
var conn4 = require('./routes/conn4');
var c4State = require('./conn4/state');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index);
app.use('/users', users);
app.use('/xandos', xandos);
app.use('/conn4', conn4);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

var server = http.createServer(app);

// Web sockets for game
let stateInterval;
var io = require('socket.io')(server);

function updateState(data) {
    data = (data) ? data : {};
    data.conn4 = c4State.get();
    io.emit('state', data);
}
io.on('connection', function(socket) {
    socket.on('stateUpdate', function(data) {
        if (data['conn4']) {
            c4State.set(data['conn4']);
        }
        updateState(data)
    });
    if (!stateInterval) {
        stateInterval = setInterval(updateState, 300);
    }
});

/**
 * Listen on provided port, on all network interfaces.
 */

server.listen(3000);
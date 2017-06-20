var express = require('express');
var router = express.Router();
var c4State = require('../conn4/state');
var game = require('../conn4/game');



function sendState(res) {
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(game.state.get()));
}

router.get('/', function(req, res, next) {
    res.render('conn4', { title: 'Let\'s play' });
});


router.get('/api/state', function(req, res, next) {
    res.setHeader('Content-Type', 'application/json');
    sendState(res);
});


router.put('/api/play/:player/:col', function(req, res, next) {
    let player = req.params.player;
    let col = parseInt(req.params.col);

    console.log(req.params.player);
    console.log(req.params.col);

    game.play(player, col);


    res.setHeader('Content-Type', 'application/json');
    sendState(res);
});

router.put('/api/reset', function(req, res, next) {
    game.state.reset()
    sendState(res);
});



module.exports = router;
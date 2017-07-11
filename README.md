A server for playing connect 4 and X's and O's.

Created for a Tech Connect Meetup code battle.

run

```
npm install
npm run start
```

or

```
docker build -t war .
docker run -p 3000:30000 war
```

http://localhost:8000/conn4
http://localhost:8000/xandos


To see the controls open the developer tools on the above pages and type `showControls()`

All open instances of the pages should sync via web sockets.

## Conn 4 api

PUT /conn4/api/reset <- start a new game, clear state.
PUT /conn4/api/play/:player/:col <- Play :player (x or o) at col :col.
GET /conn4//api/state <- Get the game state.

#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (_, response, body) => !_ && JSON.parse(body).characters.forEach(character => request(character, (_, response, body) => !_ && console.log(JSON.parse(body).name))));

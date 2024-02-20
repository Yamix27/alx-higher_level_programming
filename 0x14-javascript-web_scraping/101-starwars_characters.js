#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, body) => {
	  if (!error) JSON.parse(body).characters.forEach(character => request(character, (_, response, body) => console.log(JSON.parse(body).name)));
});

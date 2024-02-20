#!/usr/bin/node
// print the title of a Star Wars movie where
// // the episode number matches a given integer.

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';
const episodeNbr = process.argv[2];

request(URL + episodeNbr, (err, response, body) => {
if (err) {
console.log(err);
} else if (response.statusCode === 200) {
const responseJSON = JSON.parse(body);
console.log(responseJSON.title);
} else {
console.log('Error code: ' + response.statusCode);
}
});

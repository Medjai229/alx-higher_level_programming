#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, async function (error, response, body) {
  if (error === null) printChar(JSON.parse(body).characters, 0);
});

function printChar (characters, i) {
  request(characters[i], function (error, response, body) {
    if (error === null) {
      console.log(JSON.parse(response.body).name);
      if (i + 1 < characters.length) printChar(characters, i + 1);
    }
  });
}

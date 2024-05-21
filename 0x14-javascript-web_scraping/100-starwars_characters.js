#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error === null) {
    const characters = JSON.parse(body).characters;
    for (const idx in characters) {
      request(characters[idx], function (error, response, body) {
        if (error === null) console.log(JSON.parse(response.body).name);
      });
    }
  }
});

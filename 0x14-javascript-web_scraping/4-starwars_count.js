#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err == null) {
    let count = 0;
    const jsonData = JSON.parse(body).results;
    for (const film in jsonData) {
      const characters = jsonData[film].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

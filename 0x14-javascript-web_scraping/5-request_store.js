#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error === null) {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) console.log(error);
    });
  }
});

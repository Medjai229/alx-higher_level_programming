#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error === null) {
    const jsonData = JSON.parse(body);
    const count = {};
    for (const idx in jsonData) {
      const task = jsonData[idx];
      if (task.completed && count[task.userId] === undefined) count[task.userId] = 1;
      else if (task.completed) count[task.userId] += 1;
    }
    console.log(count);
  }
});

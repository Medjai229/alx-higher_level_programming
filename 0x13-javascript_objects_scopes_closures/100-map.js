#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((value, index) => value * index);
console.log(newList);

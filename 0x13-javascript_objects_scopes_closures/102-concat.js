#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

const content1 = fs.readFileSync(argv[2], 'utf-8');
const content2 = fs.readFileSync(argv[3], 'utf-8');
fs.writeFileSync(argv[4], content1 + content2);

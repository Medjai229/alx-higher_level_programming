#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2]) || argv[2] === undefined) {
	console.log('Not a number');
} else {
	console.log('My number: ' + parseInt(argv[2]));
}

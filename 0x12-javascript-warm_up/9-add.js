#!/usr/bin/node

function add(a, b) {
	numAdd = a + b;
	console.log(numAdd);
}

const argv = process.argv;

add(parseInt(argv[2]), parseInt(argv[3]));

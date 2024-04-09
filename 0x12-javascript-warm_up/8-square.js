#!/usr/bin/node

const argv = process.argv;

if (isNaN(argv[2]) || argv[2] === undefined) {
  console.log('Missing size');
} else {
	const size = parseInt(argv[2]);
	for (let i = 0; i < size; i++) {
		console.log('X'.repeat(size));
	}
}

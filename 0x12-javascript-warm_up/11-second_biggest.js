#!/usr/bin/node

const argv = process.argv;
const numArr = argv.splice(2).map(Number);

if (numArr.length <= 1) {
	console.log('0');
} else {
	numArr.sort((a, b) => b - a);
	console.log(numArr[1]);
}

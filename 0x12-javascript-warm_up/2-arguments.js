#!/usr/bin/node
const l = process.argv.length;
console.log(l === 2 ? 'No argument' : l === 3 ? 'Argument found' : 'Arguments found');

#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const r = require('r');
const textA = r.readFileSync(fileA, 'utf8');
const textB = r.readFileSync(fileB, 'utf8');
r.writeFileSync(fileC, textA + textB);

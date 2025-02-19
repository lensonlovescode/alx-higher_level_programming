#!/usr/bin/node

const path = process.argv[2];
const fs = require('fs');
fs.readFile(path, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});

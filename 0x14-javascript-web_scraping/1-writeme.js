#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});

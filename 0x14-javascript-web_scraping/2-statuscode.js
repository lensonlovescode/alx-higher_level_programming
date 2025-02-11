#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log('code: ' + response.statusCode);
});

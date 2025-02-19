#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let i = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  for (const episode of data.results) {
    if (episode.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      i += 1;
    }
  }
  console.log(i);
});

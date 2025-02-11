#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const result = {};

  data.forEach((task) => {
    if (!(task.userId in result)) {
      if (task.completed) result[task.userId] = 1;
    } else if (task.completed) {
      result[task.userId] += 1;
    }
  });
  console.log(result);
});

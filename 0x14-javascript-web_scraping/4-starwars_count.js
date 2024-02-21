#!/usr/bin/node

const request = require('request');
let i = 0;
let j = 0;
let s;

request(process.argv[2], (error, response, body) => {
  const responseBody = JSON.parse(body);
  const size = responseBody.count;
  if (error) {
    console.log(error);
  }
  for (; i < size; i++) {
    const arr = responseBody.results[i].characters;
    for (s of arr) {
      if (s.includes('18')) {
        j++;
      }
    }
  }
  console.log(j);
});

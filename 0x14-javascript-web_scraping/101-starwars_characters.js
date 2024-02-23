#!/usr/bin/node

const request = require('request');
const url1 = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let s;

request(url1, (error, response, body) => {
  const responseBody = JSON.parse(body);
  if (error) {
    console.log(error);
  }
  for (s of responseBody.characters) {
    const url2 = s;
    request(url2, (error1, response1, body1) => {
      if (error1) {
        console.log(error1);
      }
      const characterBody = JSON.parse(body1);
      console.log(characterBody.name);
    });
  }
});

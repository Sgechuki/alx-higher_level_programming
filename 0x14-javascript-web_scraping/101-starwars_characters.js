#!/usr/bin/node

const request = require('request');
const url_1 = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2]

request(url_1, (error, response, body) => {
  const responseBody = JSON.parse(body);
  const size = responseBody.count;
  if (error) {
    console.log(error);
  }
  for (s of responseBody.characters) {
	  const url_2 = s;
	  request(url_2, (error1, response1, body1) => {
		  if (error1) {
		  console.log(error1);
		  }
		  characterBody = JSON.parse(body1);
		  console.log(characterBody);
	  });
  });
});

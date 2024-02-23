#!/usr/bin/node

let dict = {};
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
 const responseBody = JSON.parse(body);
 for (d of responseBody) {
   id = String(d.userId);
   console.log(id);
   if (d.completed) {
      if (id in dict) {
        console.log('yes');
        dict.id = dict.id + 1;
      } else {
	console.log('no');
        dict['id'] = 0;
      }
   } else {
       continue;
   }
 }
});
console.log(dict);

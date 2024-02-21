#!/usr/bin/node

const request = require('request');
let num = 0;

request(process.argv[2], (error, response, body) =>
	{
		responseBody = JSON.parse(body);
		for (f in responseBody["results"]) {
			for ( c in f["characters"]) {
			if c.includes("18") {
				num++;
			}
			}
		}
		console.log(num);
	}
);

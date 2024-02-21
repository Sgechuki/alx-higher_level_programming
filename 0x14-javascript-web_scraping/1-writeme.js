#!/usr/bin/node

const fs = require('node:fs');
const content = process.argv[3];

fs.writeFile(process.argv[2], content, err => {
  if (err) {
    console.error(err);
  }
});

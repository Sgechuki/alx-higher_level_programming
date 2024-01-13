#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  let i = 2;
  let j = 0;
  while (i < process.argv.length) {
    arr[j] = parseInt(process.argv[i]);
    i++;
    j++;
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}

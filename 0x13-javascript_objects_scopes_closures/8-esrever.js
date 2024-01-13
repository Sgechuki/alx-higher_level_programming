#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  let j = 0;
  const arr = [];
  while (i >= 0) {
    arr[j] = list[i];
    i--;
    j++;
  }
  return arr;
};

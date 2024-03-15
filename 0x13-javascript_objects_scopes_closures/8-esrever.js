#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  for (let i = 0; i < list.length; i++) {
    temp[i] = list[list.length - i - 1];
  }
  return temp;
};

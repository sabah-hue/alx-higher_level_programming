#!/usr/bin/node
exports.converter = function (base) {
  return function (e) {
    return e.toString(base);
  };
};

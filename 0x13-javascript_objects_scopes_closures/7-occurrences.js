#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const x = list.filter(e => e === searchElement);
  return x.length;
};

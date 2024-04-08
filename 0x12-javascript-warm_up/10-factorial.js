#!/usr/bin/node
const args = process.argv;
function factorial(n) {
    if (n === NaN) {
        return 1;
    }
    return n * factorial(n-1);
};
factorial(parseInt(args[2]));

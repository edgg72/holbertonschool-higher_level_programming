#!/usr/bin/node
let var1 = 0;
exports.logMe = function (item) {
  console.log(var1 + ': ' + item);
  var1++;
};

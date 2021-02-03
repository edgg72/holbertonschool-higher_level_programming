#!/usr/bin/node

exports.addMeMaybe = function (number, _function) {
  number = parseInt(number) + 1;
  _function(number);
};

#!/usr/bin/node

exports.callMeMoby = function (x, _function) {
  for (let i = 0; i < x; i++) {
    _function();
  }
};

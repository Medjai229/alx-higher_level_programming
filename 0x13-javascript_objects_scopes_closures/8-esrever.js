#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];

  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    revList[i] = list[j];
  }
  return (revList);
};

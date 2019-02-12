#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments
*/
let len = process.argv.length;
let first;
let second;
if (len < 3) {
  console.log(0);
} else {
  let arr = process.argv;
  first = second = arr[2];
  for (let i = 3; i < len; i++) {
    if (first < arr[i]) {
      second = first;
      first = arr[i];
    } else if (second === first || second < arr[i]) {
      second = arr[i];
    }
  }
  console.log(second);
}

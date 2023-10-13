// Define an array of numbers
const numbers = [4, 2, 9, 1, 5, 7];

// Use the sort() method to sort the array in ascending order
numbers.sort(function(a, b) {
  return a - b;
});

// The 'numbers' array is now sorted in ascending order
console.log(numbers);

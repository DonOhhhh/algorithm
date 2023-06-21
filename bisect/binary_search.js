function binarySearch(array, target) {
  // Initialize left and right pointers
  let left = 0;
  let right = array.length - 1;

  // Continue searching while left pointer is less than or equal to right pointer
  while (left <= right) {
    // Calculate middle index
    let mid = Math.floor((left + right) / 2);

    // If the target is less than the element at the middle index, search the left half of the array
    if (target < array[mid]) {
      right = mid - 1;
    }
    // If the target is greater than the element at the middle index, search the right half of the array
    else if (target > array[mid]) {
      left = mid + 1;
    }
    // If the target is equal to the element at the middle index, return the index
    else {
      return mid;
    }
  }

  // If the target is not found, return -1
  return -1;
}

let array = [1, 2, 3, 4, 5];
let target = 3;
let index = binarySearch(array, target); // index will be 2

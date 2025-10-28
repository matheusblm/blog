## Array
List of items, try to access item or remove or add O(1)


### Common array operations

Push - Add a item to the array length O(1)
Pop - Remove and return the last element of the array O(1)
Shift - removes and returns the first element of the array O(n)
unshitf - add item to the start of the array and return the array length O(n)
splice(start_index, count_to_remove, add_items1, ....) - O(n)

#### Iterations

const number = [1,2,4]

for(let i =0;i<numbers.length;i++){
	console.log(numbers[i])
}

numbers.forEach((item, index) => console.log(item))

for (const number of numbers) {
console.log(number)
}

### Linked list
```javascript
// create linked list with class constructor
class LinkedListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

// create linked list with function constructor
function LinkedListNode(val, next) {
  this.val = val;
  this.next = next;
}

// create linked list with object literal
const linkedListNode = { val: 1, next: { val: 2, next: null } };
```

- append to end is `O(1)`
- finding an element is `O(N)`

#### Stack

Array also doubles as a stack

#### has table

Objects

get using key = get(key)
set a key, value = set(key, value)
remove = delete(key)
check if a key exist = has(key)


#### Hash set

has(item)
add(item)
delete(item)


### Insertion Sort

```javascript
function sortList(unsortedList) {
    for (let i = 1; i < unsortedList.length; i++) {
        let current = i;
        // gets the smallest element and inserts at current index
        while (current > 0 && unsortedList[current] < unsortedList[current - 1]) {
            const temp = unsortedList[current];
            // swaps current smaller element with the element before it
            unsortedList[current] = unsortedList[current - 1];
            unsortedList[current - 1] = temp;
            current--;
        }
    }
    return unsortedList;
}
```

You verify the previous values than insert in the index
### Selection Sort


```javascript
function sortList(unsortedList) {
    const n = unsortedList.length;
    for (let i = 0; i < n; i++) {
        // Assume the current position as minimum
        let minIndex = i;

        // Find the minimum element's index from the rest of the list
        for (let j = i; j < n; j++) {
            if (unsortedList[j] < unsortedList[minIndex]) {
                minIndex = j;
            }
        }

        // Swap the minimum element with the first element
        [unsortedList[i], unsortedList[minIndex]] = [unsortedList[minIndex], unsortedList[i]];
    }
    return unsortedList;
}
```

You select whats are the lowest value and put on current index

### Bubble Sort

```javascript
function sortList(unsortedList) {
    const n = unsortedList.length;
    // Iterate through all list elements in reversed order
    for (let i = n - 1; i >= 0; i--) {
        // Track whether a swap occurred in this pass
        let swapped = false;
        for (let j = 0; j < i; j++) {
            // Swap if the element found is greater than the next element
            if (unsortedList[j] > unsortedList[j + 1]) {
                const temp = unsortedList[j];
                unsortedList[j] = unsortedList[j + 1];
                unsortedList[j + 1] = temp;
                swapped = true;
            }
        }

        // If no two elements were swapped, the list is sorted
        if (!swapped) return unsortedList;
    }
    return unsortedList;
}
```

Bubble sort you make a nested loop to validate if the next value smaller then the actual then swap them, putting the greater value at the end

###  Merge Sort



[[Algoritmos]]
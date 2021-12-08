# Singly Linked List
Create a singly linked list
## Challenge
Node
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
- Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
- insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
- includes
    - Arguments: value
    - Returns: Boolean
    - Indicates whether that value exists as a Node’s value somewhere within the list.
- to string
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:
    - "{ a } -> { b } -> { c } -> NULL"
- Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
- Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Review tests and description of linked list and build to what was described. Time:O(1) Space:O(1)

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list

https://github.com/3lueHippo/data-structures-and-algorithms/pull/20

# Extended Linked List
Extend a Linked List to allow various insertion methods.
## Challenge
Write the following methods for the Linked List class:

append
- arguments: new value
- adds a new node with the given value to the end of the list
insert before
- arguments: value, new value
- adds a new node with the given new value immediately before the first node that has the value specified
insert after
- arguments: value, new value
- adds a new node with the given new value immediately after the first node that has the value specified

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Review tests and description of linked list and build to what was described. Time:O(1) Space:O(1)

- [x] Can successfully add a node to the end of the linked list
- [x] Can successfully add multiple nodes to the end of a linked list
- [x] Can successfully insert a node before a node located i the middle of a linked list
- [x] Can successfully insert a node before the first node of a linked list
- [x] Can successfully insert after a node in the middle of the linked list
- [x] Can successfully insert a node after the last node of the linked list


https://github.com/3lueHippo/data-structures-and-algorithms/pull/21

# Extending an Implementation
k-th value from the end of a linked list.
## Challenge
Write the following methods for the Linked List class:

kth from end
- argument: a number, k, as a parameter.
- Return the node’s value that is k places from the tail of the linked list.
- You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Review tests and description of linked list and build to what was described. Time:O(1) Space:O(1)

- [x] Can successfully add a node to the end of the linked list
- [x] Can successfully add multiple nodes to the end of a linked list
- [x] Can successfully insert a node before a node located i the middle of a linked list
- [x] Can successfully insert a node before the first node of a linked list
- [x] Can successfully insert after a node in the middle of the linked list
- [x] Can successfully insert a node after the last node of the linked list
- [x] Where k is greater than the length of the linked list
- [x] Where k and the length of the list are the same
- [x] Where k is not a positive integer
- [x] Where the linked list is of a size 1
- [x] “Happy Path” where k is not at the end, but somewhere in the middle of the linked list

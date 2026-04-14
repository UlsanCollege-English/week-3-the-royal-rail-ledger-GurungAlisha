[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TeyGQAqr)
# Week 3: The Royal Rail Ledger

## Summary

This assignment focuses on linked-list operations set in a railway story context.
I implemented five functions across two linked-list types: a singly linked list (SLL)
for building, reading, and finding repeated cargo entries, and a doubly linked list (DLL)
for removing banned cargo and checking palindromic train sequences.
The functions implemented are `build_sll_from_list`, `sll_to_list`, `find_first_repeat_sll`,
`remove_all_from_dll`, and `is_train_palindrome`.
The hardest part was correctly updating all four pointers when removing nodes from the DLL,
especially for consecutive target values and nodes at the head or tail.

---

## Approach

### `build_sll_from_list(values)`
- I started with an empty `SinglyLinkedList` and handled the empty-input case immediately by returning it.
- I created a head node from `values[0]`, then iterated through the remaining values and attached each as a new node via `current.next`, advancing `current` at each step.
- Values stay in the correct left-to-right order because we walk forward through the input and append to the tail of the growing list.

### `sll_to_list(sll)`
- I started at `sll.head` with an empty Python list to collect results.
- I traversed the list by following `.next` pointers in a `while` loop until reaching `None`.
- I collected values by appending `current.value` at each step and returned the result list at the end.

### `find_first_repeat_sll(sll)`
- I tracked previously seen values using a Python `set` called `seen`, which gives O(1) average-case membership checks.
- When I found a value already in `seen`, I returned it immediately without scanning further.
- If I reached the end with no repeat, I returned `None`.

### `remove_all_from_dll(dll, target)`
- I traversed the list using a `current` pointer, saving `next_node = current.next` **before** any pointer rewiring so I could safely advance even after unlinking `current`.
- When I found the target value, I patched both sides of the gap: `current.prev.next` skips forward, and `current.next.prev` skips backward.
- I handled the head case (no `prev`) by updating `dll.head`, and the tail case (no `next`) by updating `dll.tail`. These two guards also correctly set both to `None` when all nodes are removed.

### `is_train_palindrome(dll)`
- I used a `left` pointer starting at `dll.head` and a `right` pointer starting at `dll.tail`, walking both inward simultaneously.
- I stopped early when `left is right` (odd-length middle node) or when `left` advanced to meet `right` (even-length centre crossed).
- I returned `False` on the first mismatched pair, and `True` if all pairs matched.

---

## Complexity

### `build_sll_from_list(values)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** We visit each value once to create n nodes, and store all n nodes in memory.

### `sll_to_list(sll)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** We traverse all n nodes once, and the output list holds n values.

### `find_first_repeat_sll(sll)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** In the worst case we scan all n nodes; the `seen` set stores up to n distinct values.

### `remove_all_from_dll(dll, target)`
- **Time complexity:** O(n)
- **Space complexity:** O(1)
- **Why:** We make one pass through all n nodes; pointer updates are done in-place with no extra storage.

### `is_train_palindrome(dll)` *(stretch)*
- **Time complexity:** O(n)
- **Space complexity:** O(1)
- **Why:** Two pointers walk inward from both ends — at most n/2 comparisons, no extra storage beyond the two pointer variables.

### Complexity notes

- Linked lists have no direct indexed access — you must traverse from the head to reach any node, costing O(k) to reach node k.
- Traversal is always linear O(n); there is no O(1) random access like Python lists.
- Pointer updates (insert/remove) are O(1) once you already hold a direct reference to the node.
- SLLs are simpler but only allow forward traversal; DLLs add backward traversal at the cost of a `prev` pointer on every node.

---

## Edge-Case Checklist

- [x] empty SLL
- [x] empty DLL
- [x] single-node SLL
- [x] single-node DLL
- [x] no repeated values in SLL
- [x] repeated value appears later in SLL
- [x] repeated value includes the head value
- [x] removing from DLL when target is at head
- [x] removing from DLL when target is at tail
- [x] removing consecutive target values in DLL
- [x] removing all nodes from DLL
- [x] palindrome with odd length
- [x] palindrome with even length
- [x] non-palindrome DLL

---

## Assistance & Sources

### AI use
- I used AI: Yes
- AI helped with: reviewing the implementation of all five functions, explaining pointer update logic for DLL removal, and filling out this README.

### Other sources
- Class notes: linked list lecture slides
- Python docs: built-in `set` for O(1) membership testing

---

## Debugging Notes

- I first got stuck on `remove_all_from_dll` — removing the head node crashed because `current.prev` was `None` and I tried to access `.next` on it without a guard check first.
- The failing test that helped me most was the one that removes all nodes; it forced me to ensure both `dll.head` and `dll.tail` become `None` after the loop.
- I fixed the issue by separating the prev-patch and next-patch into guarded `if/else` blocks: update `dll.head` when there is no `prev`, update `dll.tail` when there is no `next`.
- I also discovered I needed to save `next_node = current.next` **before** any rewiring; without it, consecutive target values would lose the traversal reference after unlinking `current`.
- One mistake I will avoid next time is assuming `head` or `tail` are always non-`None` — always check before dereferencing a pointer.

---

## Final Reflection

This assignment made it concrete why linked lists are taught separately from arrays: the lack of index access forces you to think in terms of pointer chains rather than positions, which is a genuinely different mental model. The DLL was harder than the SLL because every remove operation touches up to four pointers instead of one, and the head/tail edge cases multiply. The most surprising edge case was removing consecutive duplicate values — saving `next_node` before removal was essential, and this kind of discipline is simply not needed with a regular Python list. Before the next assignment I want to review how sentinel (dummy) nodes can eliminate head/tail edge cases entirely by ensuring `prev` and `next` are never `None`.
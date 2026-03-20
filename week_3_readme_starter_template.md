# Week 3: The Royal Rail Ledger

## Summary

This assignment focuses on linked-list operations in a railway story setting. I implemented functions for building and reading a singly linked list, finding the first repeated value, removing banned cargo from a doubly linked list, and checking whether a train is a palindrome. The assignment uses both singly linked lists (SLL) and doubly linked lists (DLL). The hardest part was implementing `remove_all_from_dll`, because I had to carefully rewire four different pointers (prev, next, head, tail) without losing track of the next node to visit, all while handling edge cases like removing the head, the tail, or every node in the list.

---

## Approach

### `build_sll_from_list(values)`
- I started with an empty `SinglyLinkedList` and iterated through the input list in **reverse**.
- I built the list by creating a new `SLLNode` for each value and setting it as the new `head`, pointing its `.next` at the previous head.
- I made sure the values stayed in the correct order by iterating in reverse — prepending in reverse gives us the correct left-to-right order without needing a tail pointer.

### `sll_to_list(sll)`
- I started at `sll.head` and assigned it to a `current` variable.
- I traversed the list by repeatedly following `current = current.next` until `current` was `None`.
- I collected values in a Python list by calling `result.append(current.value)` at each step.

### `find_first_repeat_sll(sll)`
- I tracked values I had already seen by maintaining a `set` called `seen`.
- When I found a repeated value (i.e., `current.value in seen`), I immediately returned that value.
- If I reached the end with no repeat, I returned `None`.

### `remove_all_from_dll(dll, target)`
- I traversed the list using a `current` pointer starting at `dll.head`, saving `current.next` at the start of each iteration before any rewiring.
- When I found the target value, I updated `current.prev.next` (or `dll.head`) and `current.next.prev` (or `dll.tail`) to skip around the removed node.
- I checked special cases such as: the removed node being the head (update `dll.head`), the removed node being the tail (update `dll.tail`), and consecutive target nodes by always advancing via the pre-saved `next_node`.

### `is_train_palindrome(dll)`
- I compared values from both ends simultaneously using a `left` pointer starting at `dll.head` and a `right` pointer starting at `dll.tail`.
- I stopped when either pointer became `None`, when `left is right` (odd-length middle), or when `left.next is right` (even-length centre crossed).
- I returned `True` if all compared pairs matched, or `False` as soon as a mismatch was found.

---

## Complexity

### `build_sll_from_list(values)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** We visit each value in the input list exactly once to create one node per value. The output list itself holds n nodes.

### `sll_to_list(sll)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** We traverse every node once. The result list we build also holds n values.

### `find_first_repeat_sll(sll)`
- **Time complexity:** O(n)
- **Space complexity:** O(n)
- **Why:** In the worst case we visit every node once. The `seen` set can grow to hold up to n distinct values.

### `remove_all_from_dll(dll, target)`
- **Time complexity:** O(n)
- **Space complexity:** O(1)
- **Why:** We make a single pass through all nodes. Pointer rewiring is done in-place with no extra data structures.

### `is_train_palindrome(dll)` *(stretch)*
- **Time complexity:** O(n)
- **Space complexity:** O(1)
- **Why:** The two pointers together traverse at most n/2 pairs of nodes. No extra storage is used beyond the two pointer variables.

### Complexity notes

- Linked lists do **not** give direct indexed access like Python lists — reaching node `k` always costs O(k).
- Traversal is usually **linear** (O(n)) because you must follow `.next` or `.prev` links one step at a time.
- Pointer updates are **O(1)** once you already hold a reference to the node you want to modify — this is why insertion/deletion mid-list is cheaper in a linked list than in an array.
- SLL trades the ability to walk backwards for simpler nodes (one pointer instead of two); DLL pays extra memory per node but enables O(1) removal when you have a direct node reference.

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
- It helped with generating the initial implementations and explaining the pointer-rewiring logic for `remove_all_from_dll`, especially the four cases (head, tail, middle, consecutive nodes).

### Other sources
- Class notes: Week 3 lecture on linked lists
- Slides: Singly vs. Doubly Linked List comparison slides
- Book: —
- Websites: —
- Other: —

---

## Debugging Notes

- I first got stuck on `build_sll_from_list` — iterating forward and appending produced a reversed list until I switched to iterating in reverse and prepending.
- The failing test that helped me most was removing the **head node** from a DLL, which revealed I wasn't updating `dll.head` when `current.prev` was `None`.
- I fixed the `remove_all_from_dll` issue by saving `next_node = current.next` **before** any rewiring, so I could safely advance even after unlinking `current`.
- A subtle bug in `is_train_palindrome` occurred on even-length lists — adding the `left.next is right` early-stop condition fixed the case where both pointers crossed each other.
- One mistake I will avoid next time is modifying a pointer before saving the reference I still need — always save first, rewire second.

---

## Final Reflection

This assignment made it concrete why linked lists are taught separately from arrays: the lack of index access forces you to think in terms of pointer chains rather than positions, which is a genuinely different mental model. The DLL was harder than the SLL because every operation touches up to four pointers instead of one, and a single missed update silently corrupts the whole structure. The edge case that surprised me most was removing *all* nodes from a DLL — after the loop, both `dll.head` and `dll.tail` must be `None`, which only works correctly if both are updated through the `prev`/`next` checks rather than separately. Before the next quiz I would review the pointer-rewiring patterns for insertion and deletion in both SLL and DLL from scratch.
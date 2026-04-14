[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/T6sJM4w6)
# Week 5 — Midnight Mail Train

## Summary

This assignment combines doubly linked list operations with string/list validation and recursive thinking. I implemented a `MidnightMailDLL` class that supports appending cars, detaching the last car, and traversing in reverse. I then wrote `is_valid_ticket_code` to validate a specific string format, and two recursive functions — `count_priority_labels` to count matching items in a list, and `clean_radio_message` to strip spaces from a string. The hardest part was the recursive functions, because each one needed a clear base case and a single-step reduction before the recursive call.

## Approach

- **Problem 1 (MidnightMailDLL):** `append_car` handles two cases — empty list (new node becomes both head and tail) and non-empty (wire the new node to the old tail and advance `tail`). `detach_last_car` handles three cases — empty list returns `None`, single node zeroes out both `head` and `tail`, and the general case rewinds `tail` one step and cuts the forward link. `to_reverse_list` starts at `tail` and follows `.prev` links until `None`, collecting IDs along the way.

- **Problem 2 (is_valid_ticket_code):** Check that the code starts with `"MM-"` using `str.startswith`, then slice off those first three characters and verify the suffix is exactly 4 characters long and passes `str.isdigit`. No regex needed.

- **Problem 3 (count_priority_labels — recursive):** Base case is an empty list returning 0. Each call checks only `labels[0]` (contributing 1 if it matches, 0 otherwise) and recurses on `labels[1:]`. The count accumulates on the way back up the call stack.

- **Problem 4 (clean_radio_message — recursive):** Base case is an empty string returning `""`. Each call either keeps or drops `message[0]` depending on whether it is a space, then concatenates the result of recursing on `message[1:]`.

## Complexity

### Problem 1 — `append_car`
- **Time:** O(1) — we hold a direct `tail` reference, so no traversal is needed.
- **Space:** O(1) — one new node allocated per call.

### Problem 1 — `detach_last_car`
- **Time:** O(1) — same reason; `tail` and `tail.prev` are direct references.
- **Space:** O(1) — no extra storage used.

### Problem 1 — `to_reverse_list`
- **Time:** O(n) — we visit every node exactly once following `.prev` links.
- **Space:** O(n) — the result list holds one entry per node.

### Problem 2 — `is_valid_ticket_code`
- **Time:** O(1) — the prefix and suffix lengths are fixed constants (3 and 4 characters), so all checks run in constant time regardless of input length.
- **Space:** O(1) — only a fixed-length slice is created.

### Problem 3 — `count_priority_labels`
- **Time:** O(n) — one recursive call per element in the list.
- **Space:** O(n) — the call stack grows one frame per element (no tail-call optimisation in Python).

### Problem 4 — `clean_radio_message`
- **Time:** O(n²) — each call creates a new string by concatenation, and string concatenation in Python copies all existing characters, so the total work is 1 + 2 + … + n = O(n²).
- **Space:** O(n) — the call stack is n frames deep; the final string is also O(n).

## Edge-case checklist
- [x] empty train
- [x] one train car
- [x] invalid ticket code
- [x] empty label list
- [x] empty message
- [x] one-character or all-space message

## Assistance & Sources
- **AI used?** Yes
- **What it helped with:** Generating the initial implementations, writing the additional test cases, and explaining the O(n²) cost of recursive string concatenation in Python.
- **Other sources used:** Week 5 lecture slides on recursion and DLL pointer wiring.
# Week 3 Assignment: The Royal Rail Ledger

**Due:** Fri, March 20, 2026 at 23:59 KST  
**Repo:** `ds26-wk03-royal-rail-ledger-<student>`  
**Files that count for grading:**
- `src/challenges.py`
- `tests/test_challenges.py`
- `README.md`

## Story
The Kingdom of Velora runs a railway system that tracks cargo using linked train cars.

Each train car stores one integer cargo code. Some trains use **singly linked lists** because cargo is checked in one direction. Other trains use **doubly linked lists** because inspectors need to move from either end.

The Royal Rail Office already practiced the basic linked-list operations in class. Now they need you to solve harder inspection and repair problems.

## Your mission
You will write functions that:
- build and inspect a **singly linked list**
- analyze repeated cargo codes
- repair a **doubly linked list** by removing banned cargo
- check whether a train reads the same from both ends

This assignment builds on ideas from:
- **Week 1:** functions, returns, pytest, debugging
- **Week 2:** Python lists, boundaries, iteration, and careful thinking about order
- **Week 3:** linked lists, traversal, constructors, and pointer updates

## What you need to do
Implement the required functions in `src/challenges.py` so that all tests in `tests/test_challenges.py` pass.

You must use the provided classes and function names.

## Tasks

### Task 1: Build the freight manifest
Implement:

```python
def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
```

Given a Python list of cargo codes, build and return a `SinglyLinkedList` with the same values in the same order.

Examples:
- `[]` becomes an empty linked list
- `[4, 7, 9]` becomes `4 -> 7 -> 9`

---

### Task 2: Produce a station report
Implement:

```python
def sll_to_list(sll: SinglyLinkedList) -> list[int]:
```

Return a regular Python list containing all values from the singly linked list in order.

Examples:
- empty list returns `[]`
- `4 -> 7 -> 9` returns `[4, 7, 9]`

---

### Task 3: Find the first repeated cargo code
Implement:

```python
def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
```

Return the **first value that repeats** when scanning from head to tail.

Examples:
- `3 -> 5 -> 7 -> 5 -> 9` returns `5`
- `8 -> 2 -> 8 -> 3` returns `8`
- `1 -> 2 -> 3 -> 4` returns `None`

Be careful: this is **not** asking for the most common value. It is asking for the **first repeated value encountered during traversal**.

---

### Task 4: Remove all banned cargo from an inspection train
Implement:

```python
def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
```

Remove **all** nodes whose value equals `target` from the doubly linked list.

You must update:
- `dll.head`
- `dll.tail`
- all necessary `prev` and `next` links

Examples:
- `4 <-> 2 <-> 2 <-> 5`, remove `2` becomes `4 <-> 5`
- `7 <-> 7 <-> 7`, remove `7` becomes an empty list
- removing a missing value changes nothing

---

### Stretch Task: Palindrome inspection
Implement:

```python
def is_train_palindrome(dll: DoublyLinkedList) -> bool:
```

Return `True` if the train reads the same from front to back and back to front.

Examples:
- `1 <-> 2 <-> 3 <-> 2 <-> 1` returns `True`
- `4 <-> 9 <-> 9 <-> 4` returns `True`
- `1 <-> 2 <-> 3 <-> 4` returns `False`

## Requirements
- Use **Python 3.11+**
- Use **stdlib only**
- Do not rename the provided classes or functions
- Do not submit notebooks for grading
- Your code should be in `.py` files and tested with `pytest`

## Edge cases you must handle
Your code should work correctly for:
- empty singly linked list
- empty doubly linked list
- single-node lists
- repeated values
- removing from the head
- removing from the tail
- removing consecutive matching values
- removing all nodes from a list
- palindrome cases with even and odd lengths

## README requirements
Your `README.md` must include:
- Summary
- Approach
- Complexity
- Edge-case checklist
- Assistance & Sources

A starter template is provided separately.

## Submission checklist
- [ ] I implemented all required functions
- [ ] `pytest -q` passes
- [ ] My code is in `src/challenges.py`
- [ ] My tests are in `tests/test_challenges.py`
- [ ] My `README.md` is complete
- [ ] I handled empty, single-node, head, and tail cases

## Hints
- Draw the list before and after each pointer change
- For linked lists, order matters
- For DLL repairs, forgetting one link update can break the whole structure
- If a test fails, read the error message carefully and debug one case at a time

## Revision policy
If revisions are allowed in your section, they must follow the course revision process:
- submit a Revision Request Issue
- link your PR or commits
- name the standards you want re-checked

Do not wait until the last minute. Pointer bugs love drama.


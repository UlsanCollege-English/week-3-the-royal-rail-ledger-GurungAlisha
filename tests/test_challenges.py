from src.challenges import (
    DLLNode,
    DoublyLinkedList,
    SinglyLinkedList,
    build_sll_from_list,
    find_first_repeat_sll,
    is_train_palindrome,
    remove_all_from_dll,
    sll_to_list,
)


def build_dll(values: list[int]) -> DoublyLinkedList:
    dll = DoublyLinkedList()
    previous = None

    for value in values:
        node = DLLNode(value, previous, None)
        if dll.head is None:
            dll.head = node
        else:
            previous.next = node
        previous = node

    dll.tail = previous
    return dll


def dll_to_list(dll: DoublyLinkedList) -> list[int]:
    result = []
    current = dll.head
    while current is not None:
        result.append(current.value)
        current = current.next
    return result


def dll_to_reverse_list(dll: DoublyLinkedList) -> list[int]:
    result = []
    current = dll.tail
    while current is not None:
        result.append(current.value)
        current = current.prev
    return result


def test_build_sll_from_empty_list() -> None:
    sll = build_sll_from_list([])
    assert isinstance(sll, SinglyLinkedList)
    assert sll_to_list(sll) == []


def test_build_sll_from_non_empty_list() -> None:
    sll = build_sll_from_list([4, 7, 9])
    assert sll_to_list(sll) == [4, 7, 9]


def test_sll_to_list_empty() -> None:
    sll = SinglyLinkedList()
    assert sll_to_list(sll) == []


def test_find_first_repeat_sll_found() -> None:
    sll = build_sll_from_list([3, 5, 7, 5, 9])
    assert find_first_repeat_sll(sll) == 5


def test_find_first_repeat_sll_none() -> None:
    sll = build_sll_from_list([1, 2, 3, 4])
    assert find_first_repeat_sll(sll) is None


def test_find_first_repeat_sll_repeat_at_head_value() -> None:
    sll = build_sll_from_list([8, 2, 8, 3])
    assert find_first_repeat_sll(sll) == 8


def test_remove_all_from_dll_middle_values() -> None:
    dll = build_dll([4, 2, 2, 5])
    remove_all_from_dll(dll, 2)
    assert dll_to_list(dll) == [4, 5]
    assert dll_to_reverse_list(dll) == [5, 4]


def test_remove_all_from_dll_all_values() -> None:
    dll = build_dll([7, 7, 7])
    remove_all_from_dll(dll, 7)
    assert dll_to_list(dll) == []
    assert dll.head is None
    assert dll.tail is None


def test_remove_all_from_dll_missing_value() -> None:
    dll = build_dll([1, 3, 5])
    remove_all_from_dll(dll, 9)
    assert dll_to_list(dll) == [1, 3, 5]
    assert dll_to_reverse_list(dll) == [5, 3, 1]


def test_remove_all_from_dll_head_and_tail_cases() -> None:
    dll = build_dll([6, 1, 2, 6])
    remove_all_from_dll(dll, 6)
    assert dll_to_list(dll) == [1, 2]
    assert dll_to_reverse_list(dll) == [2, 1]
    assert dll.head.value == 1
    assert dll.tail.value == 2


def test_palindrome_true_odd_length() -> None:
    dll = build_dll([1, 2, 3, 2, 1])
    assert is_train_palindrome(dll) is True


def test_palindrome_true_even_length() -> None:
    dll = build_dll([4, 9, 9, 4])
    assert is_train_palindrome(dll) is True


def test_palindrome_false() -> None:
    dll = build_dll([1, 2, 3, 4])
    assert is_train_palindrome(dll) is False


def test_palindrome_empty_is_true() -> None:
    dll = build_dll([])
    assert is_train_palindrome(dll) is True
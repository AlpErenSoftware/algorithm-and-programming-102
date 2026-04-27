import pytest
from weeks.week_01.src.stack import Stack

def test_push_and_peek():
    """The newly added item can be seen with a peek."""
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert s.size() == 2

def test_pop_logic():
    """The pop operation should remove and return the last added element."""
    s = Stack()
    s.push("A")
    s.push("B")
    assert s.pop() == "B"
    assert s.size() == 1
    assert s.peek() == "A"

def test_is_empty():
    """The null stack check should work correctly."""
    s = Stack()
    assert s.is_empty() is True
    s.push("A")
    assert s.is_empty() is False

def test_pop_empty_raise_error():
    """Removing an element from an empty stack should throw an error."""
    s = Stack()
    with pytest.raises(IndexError) as excinfo:
        s.pop()
    assert str(excinfo.value) == "Stack is empty"

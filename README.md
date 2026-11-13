# Library Manager

Run with `python3 main.py` (on Windows: `python main.py`). Requires Python 3.12 or later and no external packages. The output of my final run is in `output.txt`.

## Reflection

**1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?**
LibraryItem is abstract because a generic "library item" is not a real thing a member can borrow; it only exists to hold what Book, Magazine and DVD share and to force each of them to define its own `late_fee()`. If DVD forgets to write `late_fee()`, Python refuses to create a DVD object and raises a TypeError ("Can't instantiate abstract class DVD ..."). This catches the mistake immediately instead of letting a DVD silently charge the wrong fee later.

**2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?**
Reading `item.__available` from outside raises an AttributeError, because Python renames private attributes inside the class (name mangling), so the name `__available` does not exist outside it. We use `is_available()` so the value can be read without being changed directly. Only `mark_borrowed()` and `mark_returned()` can modify it, which keeps an item's availability consistent with who has borrowed it.

**3. What is the difference between LibraryItem.total_items and self.title?**
`total_items` is a class attribute: one value stored on the class and shared by every item, so it counts all items created (it goes up by 1 in each `__init__`). `self.title` is an instance attribute: each object has its own copy, so a Book and a DVD can have different titles. You read the class attribute through the class name (`LibraryItem.total_items`) and the instance attribute through the object (`book.title`).

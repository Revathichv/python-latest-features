from typing import Optional, List, Tuple

# Optional[str]: The get_user function can return either a string or None.

def get_user(id: int) -> Optional[str]:
    return None if id == 0 else "User"

def sum(num: List[int]) -> int:
    return sum(num)

def get_name_and_age() -> Tuple[str, int]:
    return ("Abc", 25)
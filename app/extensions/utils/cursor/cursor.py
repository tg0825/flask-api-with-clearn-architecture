from dataclasses import dataclass
from typing import List


@dataclass
class Paginate:
    total: int = None
    count: int = None
    per_page: int = None
    current_page: int = None
    total_pages: int = None
    links: List = None

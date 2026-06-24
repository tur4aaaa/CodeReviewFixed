from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Foo:
    name: str

alex = Foo("Alex")
mar = Foo("Mar")

counter: dict[Foo, int] = defaultdict(int)

counter[alex] += 1
counter[mar] += 1

print(counter)
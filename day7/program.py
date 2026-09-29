from dataclasses import dataclass, field

@dataclass()
class Program:
    name:str
    weight:int
    children:list[str]
    child_weights:list[int] = field(default_factory=list)

def parse_program(s:str):
    tokens = s.split()
    if len(tokens) < 2:
        return None

    name = tokens[0]
    weight = int(tokens[1][1:-1])
    children = []

    if len(tokens) > 2:
        for child in tokens[3:]:
            children.append(child.rstrip(','))

    program = Program(name, weight, children)
    return program

from logging import warning

from program import Program
from collections import Counter


class Graph:
    def __init__(self, program_list):
        self.nodes = dict()
        for program in program_list:
            self.nodes[program.name] = program

    def __repr__(self):
        s = ""
        for program in self.nodes.values():
            s += f"{program.name} ({program.weight})"
            children = ", ".join(program.children)
            s += f" -> {children}\n" if len(children) > 0 else "\n"
        return s

    """Returns a list of all the 'root' nodes (i.e. nodes with no incoming edges) in the graph."""
    def find_roots(self) -> list[Program]:
        indegree = dict()

        for program in self.nodes.values():
            for child in program.children:
                indegree[child] = indegree.setdefault(child, 0) + 1

        roots = []
        for program in self.nodes.values():
            if indegree.setdefault(program.name, 0) == 0:
                roots.append(program)

        return roots

    """Returns the corrected weight for the first unbalanced node to be found (if any)."""
    def find_balance(self):
        root = self.find_roots().pop()
        self.find_balance_recursive(root.name, 0)

        for node in self.nodes.values():
            counter = Counter(node.child_weights)
            if len(counter) > 1:
                bad_weight = min(counter, key=counter.get)
                good_weight = max(counter, key=counter.get)
                bad_idx = node.child_weights.index(bad_weight)
                faulty_node_name = node.children[bad_idx]
                faulty_node = self.nodes[faulty_node_name]

                corrected_weight = faulty_node.weight + good_weight - bad_weight

                # warning(f"Mismatched weight: {faulty_node_name} {corrected_weight}")
                return corrected_weight
        return None

    """Recursively calculates the child weights of all nodes. """
    def find_balance_recursive(self, name: str, level: int):
        node = self.nodes[name]
        node.child_weights = [self.find_balance_recursive(child, level + 1) for child in node.children]

        return node.weight + sum(node.child_weights)

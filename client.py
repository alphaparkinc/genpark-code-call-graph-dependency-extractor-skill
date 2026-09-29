"""Static Code Call Graph & Dependency Extractor.
100% Python Standard Library.
"""

import ast
import collections

class CallGraphExtractor(ast.NodeVisitor):
    """Extracts caller-to-callee directed graphs from Python code."""
    def __init__(self):
        self.current_func = None
        self.graph = collections.defaultdict(list)

    def visit_FunctionDef(self, node):
        old_func = self.current_func
        self.current_func = node.name
        self.generic_visit(node)
        self.current_func = old_func

    def visit_Call(self, node):
        if self.current_func and isinstance(node.func, ast.Name):
            self.graph[self.current_func].append(node.func.id)
        self.generic_visit(node)

    @classmethod
    def extract_graph(cls, source):
        tree = ast.parse(source)
        extractor = cls()
        extractor.visit(tree)
        return dict(extractor.graph)

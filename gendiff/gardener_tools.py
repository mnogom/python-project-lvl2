"""Module has predicates to explore nodes."""


def is_leaf(node):
    """Predicate to check if node is leaf."""

    return not is_branch(node)


def is_branch(node):
    """Predicate to check if node is branch."""

    return isinstance(node, dict)


def has_key(key, node):
    """Predicate to check if node has selected key."""

    return key in node.keys()


def get_value(key, node):
    """Return value from node by key."""

    return node.get(key)

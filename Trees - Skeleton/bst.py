"""Algorithms and Data Structures 1 AI - Binary Search Trees."""

import contextlib
from dataclasses import dataclass, field
from typing import Any, Iterable, Iterator, MutableMapping, overload, override


@dataclass
class TreeNode:
    """TreeNode helper class.

    Attributes:
        key (int): Key used for sorting the node into a BST.
        value (Any): Whatever data the node shall carry.
        right (TreeNode): Node to the right.
        left (TreeNode): Node to the left.
        parent (TreeNode): Parent node.
    """

    key: int
    value: Any
    _right: "TreeNode | None" = field(default=None, init=False, repr=False)
    _left: "TreeNode | None" = field(default=None, init=False, repr=False)
    _parent: "TreeNode | None" = field(default=None, init=False, repr=False, compare=False)

    @property
    def right(self) -> "TreeNode | None":
        """Return the right child of this node if existing."""
        return self._right

    @right.setter
    def right(self, value: "TreeNode | None"):
        """Set the right child of this node."""
        # NOTE: You may want to additionally update the parent field of the current child 
        # and future child accordingly and avoid ever setting 'parent' explicitly.
        self._right = value

    @property
    def left(self) -> "TreeNode | None":
        """Return the left child of this node if existing."""
        return self._left

    @left.setter
    def left(self, value: "TreeNode | None"):
        """Set the left child of this node."""
        # NOTE: You may want to additionally update the parent field of the current child 
        # and future child accordingly and avoid ever setting 'parent' explicitly.
        self._left = value

    @property
    def parent(self) -> "TreeNode | None":
        """Returns the parent of this node or 'None' if this is a root node."""
        return self._parent

    @parent.setter
    def parent(self, value: "TreeNode | None"):
        """Set the parent of this node."""
        # NOTE: *You may delete this setter* and automatically set '_parent' whenever this node
        # is being set as the left/right node of some other node.
        # This could make your life easier, ensuring that 'node.left.parent == node' all the time.
        self._parent = value

    def overwrite_parent(self, new_parent: "TreeNode | None"):
        """Force-set the parent of this node."""
        # This method is used in testing to ensure we can provide you a valid tree.
        self._parent = new_parent

    @property
    def depth(self) -> int:
        """Return depth of the node, i.e. the number of parents/grandparents etc.

        Returns:
            int: Depth of node
        """
        depth = 0
        node = self

        while node.parent is not None:
            depth += 1
            node = node.parent

        return depth

    @property
    def is_external(self) -> bool:
        """Return if node is an external node (= leaf)."""
        return self.left is None and self.right is None

    @property
    def is_internal(self) -> bool:
        """Return if node is an internal node."""
        return not self.is_external


class BinarySearchTree(MutableMapping[int, Any]):
    """Binary-Search-Tree implemented for didactic reasons."""

    @overload
    def __init__(self):
        """Initialize BinarySearchTree."""
        ...

    @overload
    def __init__(self, root: "TreeNode", size: int):
        """Initializes a BinarySearchTree already filled with data.

        Used for testing.

        Args:
            root (TreeNode): Root of the BST.
            size (int): Size of the BST.
        """
        ...

    def __init__(self, root: "TreeNode | None" = None, size: "int | None" = None):
        """Initializes a BinarySearchTree."""
        self._root = root
        self._size = size or 0

    def insert(self, key: int, value: Any) -> TreeNode:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is already present in the tree.
        
        Returns:
            TreeNode: The newly inserted node.
        """
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        new_node = TreeNode(key, value)

        if self._root is None:
            self._root = new_node
            self._size += 1
            return new_node

        current = self._root

        while True:
            if key == current.key:
                raise KeyError("Key already exists")
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    self._size += 1
                    return new_node
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    self._size += 1
                    return new_node
                current = current.right

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Raises:
            TypeError: If `key` is not an integer.
            KeyError: If `key` is not present in the tree.
        """
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")

        current = self._root

        while current is not None:
            if key == current.key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError("Key not found")

    def try_find(self, key: int) -> TreeNode | None:
        """Returns the node with the given key or None if that node doesn't exist.

        Raises:
            TypeError: If key is not an integer.
        """
        with contextlib.suppress(KeyError):
            return self.find(key)
        return None

    @property
    def size(self) -> int:
        """Return the number of nodes contained in the tree."""
        return self._size

    # This is what is called when you do `len(tree)`
    @override
    def __len__(self) -> int:
        """Returns the number of nodes contained in the tree."""
        return self.size

    # This is what gets called when you call e.g. `tree[5]`
    @override
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: The value of the node with the given key.
        """
        return self.find(key).value

    @override
    def __contains__(self, key: object) -> bool:
        """Return whether a node with the given key is in this tress."""
        if not isinstance(key, int):
            return False
        return self.try_find(key) is not None

    @override
    def __setitem__(self, key: int, value: Any) -> None:
        """Sets the value of the node with the given key or inserts a new node."""
        node = self.try_find(key)
        if node is None:
            self.insert(key, value)
        else:
            node.value = value

    @override
    def __delitem__(self, key: int) -> None:
        """Removes node with the given key, maintaining BST-properties."""
        self.remove(key)

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            TypeError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        # * HINT:
        # * find node
        # * node has 0 children? => remove node by detaching from parent
        # * node has 1 child?    => attach child to parent (instead of the node)
        # * node has 2 children?
        # * => find inorder-successor of node (how to do that?)
        # * => swap/replace node with inorder successor (maybe add a function for that)
        # * => after that our node has guaranteed at most one child (why that?)
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")

        node = self.find(key)

        if node.left is not None and node.right is not None:
            successor: TreeNode | None = node.right
            while successor.left is not None:
                successor = successor.left

            node.key = successor.key
            node.value = successor.value
            node = successor
        child = node.left if node.left is not None else node.right

        if child is not None:
            child.parent = node.parent

        if node.parent is None:
            self._root = child
        elif node.parent.left is node:
            node.parent.left = child
        else:
            node.parent.right = child

        self._size -= 1

    # NOTE: An Iterable is everything where you can write `for _ in <iterable>`
    # you may just return a list, but if you wanna be efficient you compute the order lazily
    # and return a generator instead.
    # Hint: Using a recursive generator with 'yield from' makes this function very easy to implement
    # Generator Tutorial: https://youtu.be/tmeKsb2Fras
    def inorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in inorder."""

        # if you're confused by `Iterable` just do
        # inorder_list: list[TreeNode] = []
        # <fill inorder_list with nodes in-order>
        # return inorder_list
        def traverse(node):
            if node is not None:
                yield from traverse(node.left)
                yield node
                yield from traverse(node.right)

        return traverse(self.root)

    def preorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in preorder."""

        def traverse(node):
            if node is not None:
                yield node
                yield from traverse(node.left)
                yield from traverse(node.right)

        return traverse(self._root)

    def postorder(self) -> Iterable[TreeNode]:
        """Returns an iterable yielding the nodes in postorder."""

        def traverse(node):
            if node is not None:
                yield from traverse(node.left)
                yield from traverse(node.right)
                yield node
        return traverse(self._root)

    # this allows for e.g. `for key in tree` and is required for a mutable mapping
    @override
    def __iter__(self) -> Iterator[int]:
        return iter(node.key for node in self.preorder())

    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""

        def check(node, min_key, max_key):
            if node is None:
                return True
            if min_key is not None and node.key <= min_key:
                return False
            if max_key is not None and node.key >= max_key:
                return False

            return check(node.left, min_key, node.key) and check(node.right, node.key, max_key)

        return check(self._root, None, None)

    def return_min_key(self) -> "TreeNode | None":
        """Return the node with the smallest key (None if tree is empty)."""
        current = self._root

        if current is None:
            return None

        while current.left is not None:
            current = current.left

        return current

    def return_max_key(self) -> "TreeNode | None":
        """Return the node with the largest key (None if tree is empty)."""
        current = self._root

        if current is None:
            return None
        while current.right is not None:
            current = current.right

        return current

    @staticmethod
    def count_comparisons(for_list: "list[int]", key: int) -> "tuple[int, int]":
        """Count how many comparisons are needed to find a specific key in a list vs bst.

        Creates a Binary Search tree, inserts all values from `for_list` and then checks
        how many comparisons are needed to find `key` vs how many comparisons are required when
        just going through the list one element after another. 

        `for_list` must not contain duplicates.

        Args:
            for_list (list[int]): The list to check against and build a BST from.
            key (int): The key to find.

        Returns:
            tuple[int, int]:
                0: The number of comparisons walking through the list.
                1: The number of comparisons used in the bst.
        """
        list_comparisons = 0

        for element in for_list:
            list_comparisons += 1
            if element == key:
                break

        tree = BinarySearchTree()

        for element in for_list:
            tree.insert(element, element)

        bst_comparisons = 0
        current = tree.root

        while current is not None:
            bst_comparisons += 1

            if key == current.key:
                break

            bst_comparisons += 1

            if key < current.key:
                current = current.left
            else:
                current = current.right
        return list_comparisons, bst_comparisons

    @property
    def root(self) -> "TreeNode | None":
        """Returns the root of the Binary Search Tree."""
        return self._root


    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self.inorder())})"

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

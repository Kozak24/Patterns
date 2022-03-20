from behavioral.iterator.data import Node
from behavioral.iterator.logic import DfsIterator, BfsIterator


def main() -> None:
    """
         1
       /  \
      2    3
     / \    \
    4   5    6
         \  /
           7
    """
    seventh_node = Node(7)
    sixth_node = Node(6, left=seventh_node)
    fifth_node = Node(5, right=seventh_node)
    fourth_node = Node(4)
    third_node = Node(3, right=sixth_node)
    second_node = Node(2, left=fourth_node, right=fifth_node)
    root = Node(1, left=second_node, right=third_node, iterator=DfsIterator)

    print("DFS Iterator")
    for node in root:
        print(node)

    root = Node(1, left=second_node, right=third_node, iterator=BfsIterator)
    print("\nBFS Iterator")
    for node in root:
        print(node)


if __name__ == "__main__":
    main()

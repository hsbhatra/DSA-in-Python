# If not trees what would we use?
# Arrays, linked-list, stack, queue.
# Which are basically a kind of an array with some different features.
# But one thing is common in them, the are linear in nature.
# We can store data in an array in a linear format.
#       ---------->  Linear traversal/access/search.
# arr = [1,2,3,4,5]
# Arrays are also of a fixed size. Fixed Memory Allocation.
# Well this is not a concept in linked list, queue, and stack. But in array.

# Trees:-
    # Searching is faster: (Better time complexity)
            # Even in an array if we apply binary search it will firstly need a sorted array, after that we need to find the mid index and then perform a lot of operations to find an element.
            # But in tree data structure we can store larger value on the right side and smaller values on the left side (no need to sort first), also in trees we use pointer concept (no need to traverse like we do in arrays), and less number of operation (such as no need to find the mid index and traversing through).
    # can form hierarchy.
    # Dynamic memory allocation, as tree works on the concept of pointers.

                                    # 40    (Root node) (Parent node of 30 and 50)
                                  # /   \
        # (Left child of 40)      30     50       (Right child node of 40)
                               # /  \   /  \
                             # 20   35 45   55      (Leaf nodes)

# Terminologies of tree data structure:-
    # Root node - Starting node.
    # Child node
    # Branches - ('/' or '\')
    # Siblings - Nodes having common Parent node. (Left child of 40 is sibling of right child of 40, and vice-versa)
    # Leaf node - The node which do not have any further child nodes. They are the "last or ending nodes" of the tree.

# Some extra terminologies:-
    # Degree - Max number of branches/edges/child nodes of any given node.
    # Depth - As we go down we increase the depth by 1. The depth of the "Root Node" is always 0.
    # Level - As we go down we increase the level by 1. The level of the "Root Node" is always 1.
    # Height - The longest path to the leaf node is the height of the given node. As we go down to each node, we increase the height by 1.

# Types of Tree:-
    # 1. Binary Tree - 
        # Each node has at most (maximum) 2 child nodes only.
        # Degree (of a binary tree) <= 2.

    # 2. Ternary Tree - 
        # Each node has at most (maximum) 3 child nodes only.
        # Degree <= 3.

    # 3. n-ary tree - 
        # Each node has at most (maximum) 'n' child nodes only.
        # Degree <= n.

# Some basic fourmulas:-
    # number of edges/branches = number of nodes - 1.
    # total number of leaf nodes in a binary tree = total number of nodes with two (2) child nodes + 1. 



















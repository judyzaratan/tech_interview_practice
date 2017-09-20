import random

# Question 1
# Given two strings s and t, determine whether some anagram of t is a
# substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a
# boolean True or False.


def question1(s, t):
    if len(s) < len(t):
        return False

    temp = t

    # Iterate through s
    for character in s:
        if character in t:
            # If character is in s and t, mark out that character
            temp = temp.replace(character, "", 1)
            # Anagram has been found, with all characters in t, marked out
            if len(temp) == 0:
                return True
        else:
            temp = t
    return False

print "Question 1 Test Cases"
print question1('hello', 'loh')
# False
print question1('udacity', 'ad')
# True
print question1('udacity', 'aduaca')
# False


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.


def longestPalindrome(str):
    # Return
    largestPal = ""
    for x in range(len(str)):
        workingStr = str[x:]
        end = len(workingStr)
        while end != 0:
            if workingStr == workingStr[-1:-len(workingStr)-1:-1]:
                if (len(workingStr)) > len(largestPal):
                    largestPal = workingStr
            end -= 1
            workingStr = workingStr[:end]
    if len(largestPal) == 0 or len(largestPal) == 1:
        return None
    else:
        return largestPal

print "Question 2 Test Case"

print longestPalindrome("bbbbbbbbbbbbbbrracecarxxxxxxxxxxxxxxxxxxxx")
# xxxxxxxxxxxxxxxxxxxx
print longestPalindrome("sdaasdfracecarbbb")
# racecar
print longestPalindrome("abracadabra")
# aca
print longestPalindrome("bbasdraceecarasdfa")
# racecar
print longestPalindrome("abcdefghijklmnopqrstuvwxyz")
# None

# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)


def question3(G):
    min_spanning_tree = {}
    visted_vertices = []
    # Initialize minimum spanning tree with vertices from G
    for i, vertex in enumerate(G):
        min_spanning_tree[vertex] = []
    print min_spanning_tree


    start_vertex = random.choice(G.keys())
    print 'start_vertex', start_vertex
    # Iterate through graph until all vertices are visted
    visted_vertices.append(start_vertex)
    print visted_vertices
    prev_e = None
    while len(visted_vertices) < len(G):
        for vertex in visted_vertices:
            for edge in G[vertex]:

                if not prev_e or edge[1] < prev_e[1]:
                    if edge[0] not in visted_vertices:
                        prev_e = edge
                        to_vertex = edge[0]
                        from_vertex = vertex
                        edge_weight = edge[1]

        if not prev_e:
            break
        visted_vertices.append(to_vertex)
        min_spanning_tree[from_vertex].append((to_vertex, edge_weight))
        min_spanning_tree[to_vertex].append((from_vertex, edge_weight))
        # if no edge is found, break the loop.
        # this is for cases where a node is detached from the graph.
        prev_e = None
        edge = None
        to_vertex = None
        from_vertex = None


    return min_spanning_tree




print "question3......"
print question3({'A': [('B', 2)],
                'B': [('A', 2), ('C', 5), ('D', 3)],
                'C': [('B', 5), ('E', 6)],
                'D': [('B', 3), ('E', 1)],
                'E': [('D', 1), ('C', 6)]
            })

# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
#For example, the root is a common ancestor of all nodes on the tree, but if both nodes are
# descendents of the root's left child, then that left child might be the lowest common ancestor.
# You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T is the tree represented
# as a matrix, where the index of the list is equal to the integer stored in that node and a 1
# represents a child node, r is a non-negative integer representing the root, and n1 and n2
# are non-negative integers representing the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def question4(T, r, n1, n2):
    def search(r, node):
        current_node = r
        path = []
        isFound = False
        path.append(r)
        prev_node = None
        while current_node != prev_node:
            if  node == current_node:
                isFound = True
                break
            if node < current_node:
                prev_node = current_node
                for child in range(0, current_node):
                    if T[current_node][child] == 1:
                        current_node = child
                        path.append(child)
                        break
            if node > current_node:
                prev_node = current_node
                for child in range(node, len(T)):
                    if T[current_node][child] == 1:
                        current_node = child
                        path.append(child)
                        break
        if isFound:
            return path
        else:
            return None

    print "search 1"
    path1 = search(r, n1)
    print path1
    print "search 2"
    path2 = search(r, n2)
    print path2
    foundAncestor = r
    for i1 in range(len(path1) - 1, 0, -1):
        for i2 in range(len(path2) - 1, 0, -1):
            if (path1[i1] == path2[i2]):
                foundAncestor = path1[i1]
                break
    return foundAncestor






print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4
            )



# Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
#
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def question5(ll, m):
    head_pointer = ll
    while m > 0:
        head_pointer = head_pointer.next
        m -= 1

    tail_pointer = ll
    while head_pointer != None:
        head_pointer = head_pointer.next
        tail_pointer = tail_pointer.next
    return tail_pointer.data


print "Question 5 Test Cases"

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six

print question5(one, 3)

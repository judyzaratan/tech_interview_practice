import random

# Question 1
# Given two strings s and t, determine whether some anagram of t is a
# substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a
# boolean True or False.

def compare_substrings(dict1, dict2):

    if len(dict1) != len(dict2):
        return False

    # Iterate through dict1 and compare each character with dict2
    # Break out of loop if character is not found or counts mismatch
    for i in dict1:
        if i in dict2:
            if dict1[i] != dict2[i]:
                return False
        else:
            return False
    return True


def question1(s, t):
    if len(s) < len(t):
        return False
    t_dict = {}
    s_dict = {}

    # Create two dictionaries that contains the first len(t) elements
    # for each string
    for i in range(len(t)):
        if i in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1

        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1

    # Compare first substring in the s substring sequence
    if compare_substrings(s_dict, t_dict):
        return True

    # Compare remaining substrings in s
    for i in xrange(len(t), len(s)):

        # Add last character in substring
        if s[i] in s_dict:
            s_dict[s[i]] +=1
        else:
            s_dict[s[i]] = 1

        # Remove last chacter from previous substring
        s_dict[s[i - len(t)]] -=1
        if s_dict[s[i-len(t)]] == 0:
            del s_dict[s[i-len(t)]]

       # Compare substring s with t
        if compare_substrings(s_dict, t_dict):
            return True


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

def processString(s):
    """ Provides a string that is 2N + 1 or odd-valued length """
    """
        Input: s, example: s="hello"
        Output: processedStr, example: processStr = "#h#e#l#l#o#"
    """
    processed_str = ""
    if len(s) == 0:
        return "##"
    for char in s:
        processed_str += "#" + char
    processed_str += "#"
    return processed_str


def longestPalindrome(str):
    largestPal = ""
    transformed_str = processString(str)
    center = 0
    radius = 0 # Edge index for the largest palindrome encountered
    pal_len = [0 for i in range(len(transformed_str))]

    for i in range(1, len(transformed_str)-1):
        # i: right edge index of current palindrome
        # i_mirr: left edge index of current palindrome
        # radius: right edge index of longest palindrome found so far
        i_mirr = 2 * center - i

        # Radius edge index greater than, i is within bounds
        # Set minimum palindrome length for right index
        # Use precomputated palindrome length if i is within bounds of
        # range from p[i_mirr] length
        if (radius > i):
            pal_len[i] = min(radius - i, pal_len[i_mirr])
        else:
            pal_len[i] = 0


        # Expand palindrome at index i, a(right) and b(left)
        # Ensure it is within bounds of transformed_str
        i_right = i + pal_len[i] + 1
        i_left = i - pal_len[i] - 1
        while (i_right < len(transformed_str) \
               and i_left >= 0 \
               and transformed_str[i_right] == transformed_str[i_left]):
            pal_len[i] += 1
            i_right = i + pal_len[i] + 1
            i_left = i - pal_len[i] - 1

        # Check if expanded palindrome from i is extended past radius
        # Update center to i and radius to extend length
        if (i + pal_len[i] > radius):
            center = i
            radius = i + pal_len[i]


    maxLen = 0
    centerIndex = 0

    # Iterate through palindrome lengths array to find one that has the maximum length
    for j in range(len(pal_len)):
        if (pal_len[j] > maxLen):
            maxLen = pal_len[j]
            centerIndex = j

    # Convert indexes to original input string to provide palindrome
    if maxLen == 1:
        return None
    else:
        return str[(centerIndex - maxLen )/2: (centerIndex + maxLen)/2]


print "Question 2 Test Case"
print longestPalindrome("racecar")

print longestPalindrome("bbbbbbbbbbbbbbrracecarxxxxxxxxxxxxxxxxxxxx")
#  xxxxxxxxxxxxxxxxxxxx
print longestPalindrome("sdaasdfracecarbbb")
#  racecar
print longestPalindrome("abracadabra")
# # aca
print longestPalindrome("bbasdraceecarasdfa")
# # racecar
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

    # Choose a random vertex to begin
    start_vertex = random.choice(G.keys())
    visted_vertices.append(start_vertex)

    # Iterate through graph until all vertices are visted
    prev_e = None
    while len(visted_vertices) < len(G):
        for vertex in visted_vertices:
            for edge in G[vertex]:
                # iterate through edge list for a vertex
                # selects edge that has the lowest weight
                if not prev_e or edge[1] < prev_e[1]:
                    if edge[0] not in visted_vertices:
                        prev_e = edge
                        to_vertex = edge[0]
                        from_vertex = vertex
                        edge_weight = edge[1]


        # store selected lowest weight edge visted list
        # store lowest weight edge into tree and visit node
        visted_vertices.append(to_vertex)
        min_spanning_tree[from_vertex].append((to_vertex, edge_weight))
        min_spanning_tree[to_vertex].append((from_vertex, edge_weight))

        # since next vertex is stored in visited list, reset variables
        prev_e = None
        edge = None
        to_vertex = None
        from_vertex = None


    return min_spanning_tree




print "Question 3 Test Cases"
print question3({'A': [('B', 2)],
                'B': [('A', 2), ('C', 5), ('D', 3)],
                'C': [('B', 5), ('E', 6)],
                'D': [('B', 3), ('E', 1)],
                'E': [('D', 1), ('C', 6)]
            })

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5), ('D', 3)],
#  'C': [('B', 5)],
#  'D': [('B', 3), ('E', 1)],
#  'E': [('D', 1)]
# }

print question3({'A': [('B', 6)],
                'B': [('A', 2), ('C', 1)],
                'C': [('B', 1), ('D', 1)],
                'D': [('A', 1), ('C', 1)]
            })

 # {'A': [('D',1)],
#   'B': [('C', 1)],
#   'C': [('B', 1), ('D', 1)],
#   'D': [('A', 1), ('C', 1)]
# }
print question3({'A': [('C', 6), ('D', 6), ('E', 1)],
                 'B': [('C', 6), ('D', 6), ('E', 1)],
                 'C': [('A', 6), ('B', 6), ('E', 1)],
                 'D': [('A', 6), ('B', 6), ('E', 1)],
                 'E': [('A', 1), ('B', 1), ('C', 1), ('D', 1)]
            })

 # {'A': [('E',1)],
#   'B': [('E', 1)],
#   'C': [('E', 1)],
#   'D': [('E', 1)],
#   'E': [('A', 1), ('B', 1), ('C', 1), ('D', 1)]
# }

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
        """ A subfunction to find a path from root to node"""

        # Initialize variables and pointers
        current_node = r
        path = []
        isFound = False
        path.append(r)
        prev_node = None

        while current_node != prev_node:
            if  node == current_node:
                isFound = True
                break

            # Check if node is to the left in BST
            # Find next child
            if node < current_node:
                prev_node = current_node
                for child in range(0, current_node):
                    if T[current_node][child] == 1:
                        current_node = child
                        path.append(child)
                        break

            # Check if node is to the right in BST
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

    path1 = search(r, n1)
    path2 = search(r, n2)


    # default ancestor as root
    foundAncestor = r

    for i1 in range(len(path1) - 1, 0, -1):
        for i2 in range(len(path2) - 1, 0, -1):

            # iterate through n1 path and compare against n2 path
            #  to find least common ancestor
            if (path1[i1] == path2[i2]):
                foundAncestor = path1[i1]
                break

    return foundAncestor

print "Question 4 Test Case"
print question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4
            )
# 3
print question4([[0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0]],
                4,
                0,
                3
            )
# 1

print question4( [[0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0]],
                4,
                0,
                3
            )
#2

# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end
# is the 3rd element. The function definition should look like
# question5(ll, m), where ll is the first node of a linked list and m is
# the "mth number from the end". You should copy/paste the Node class below
# to use as a representation of a node in the linked list. Return the value
# of the node at that position.
#

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


def question5(ll, m):
    head_pointer = ll
    while m > 0:
        if head_pointer == None:
            return None
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
# 4
print question5(one, 6)
# 1
print question5(one, 7)
# None

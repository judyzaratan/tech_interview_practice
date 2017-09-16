# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad", then the function returns True.
# Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(s , t):
  if len(s) < len(t):
      return False
  map = {}
  for item in s:
      if not map.has_key(item):
          map[item] = 0
      map[item] += 1
  for t_item in t:
      if map.has_key(t_item):
          if map[t_item] > 0:
              map[t_item] -= 1
          else:
              return False
      else:
          return False
  return True

print "Question 1 Test Case"
print question1('hello', 'lo')

# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def longestPalindrome(str):
    if len(str) == 1:
        return str
    if len(str) == 2:
        if str[0] == str[1]:
            return str
        else:
            return None

    # Pointers
    middle = 1
    start = 1
    end = 1
    largestPal = ""

    while middle < len(str) - 1:
        start -= 1
        end += 1
        if str[start] == str[end]:
            if len(str[start:end +1]) > len(largestPal):
                largestPal = str[start:end+1]
        if start == 0 or end == len(str) - 1:
            middle += 1
            start = middle
            end = middle
    return largestPal


print "Question 2 Test Case"
print longestPalindrome("racecarbbbbbbbbbb")
print len("bbbbbbbbbb")


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
    def search(n):
        path = []
        for node in T:
            print node
            for child in node:
                if node[child] != 0:
                    path.append(child)
        return path
    print search(T)

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)



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

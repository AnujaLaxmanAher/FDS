"""Q.PROBLEM STATEMENT : In a second year computer engineering class, group A students play cricket, 
group B students play badminton and group C students play football. Write a python program using 
functions to compute following:
a) List ofstudents who play both cricket and badminton.
b) List ofstudents who play either cricket or badminton but not both.
c) Number of students who play neither cricket nor badminton.
d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in 
functions)
Name: Anuja Aher
Class: SE Comp 2
Batch: R
Clg PRN: F24122006
Seat no: """

# Helper function to remove duplicates from a list
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Function to find intersection of two lists (students who play both games)
def intersection(lst1, lst2):
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result

# Function to find difference of two lists (students who play one game but not the other)
def difference(lst1, lst2):
    result = []
    for item in lst1:
        if item not in lst2 and item not in result:
            result.append(item)
    return result

# Function to find union of two lists (students who play either of the games)
def union(lst1, lst2):
    result = remove_duplicates(lst1 + lst2)
    return result

# Function to compute students who play both cricket and badminton
def cricket_and_badminton(cricket, badminton):
    return intersection(cricket, badminton)

# Function to compute students who play either cricket or badminton but not both
def cricket_or_badminton_not_both(cricket, badminton):
    only_cricket = difference(cricket, badminton)
    only_badminton = difference(badminton, cricket)
    return only_cricket + only_badminton

# Function to compute the number of students who play neither cricket nor badminton
def neither_cricket_nor_badminton(all_students, cricket, badminton):
    cricket_or_badminton = union(cricket, badminton)
    result = []
    for student in all_students:
        if student not in cricket_or_badminton:
            result.append(student)
    return len(result)

# Function to compute students who play cricket and football but not badminton
def cricket_and_football_not_badminton(cricket, football, badminton):
    cricket_and_football = intersection(cricket, football)
    result = difference(cricket_and_football, badminton)
    return result

# Sample data (example lists of students in each group)
all_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]
cricket_players = ["Alice", "Bob", "Charlie", "David"]
badminton_players = ["Charlie", "Eve", "Frank", "Alice"]
football_players = ["Bob", "Grace", "Hannah", "Alice"]

# Results
print("a) Students who play both cricket and badminton:", cricket_and_badminton(cricket_players, badminton_players))
print("b) Students who play either cricket or badminton but not both:", cricket_or_badminton_not_both(cricket_players, badminton_players))
print("c) Number of students who play neither cricket nor badminton:", neither_cricket_nor_badminton(all_students, cricket_players, badminton_players))
print("d) Students who play cricket and football but not badminton:", cricket_and_football_not_badminton(cricket_players, football_players, badminton_players))

# Bhavana Samudrala
# student number- 11258695
# NSID- bhs053
# Instructor- Arlin Schaffel
# CMPT-145-L14

import Statistics as S
stats = S.Statistics()


# test Statistics.create()
# We can't test the object's identity, and the attributes are private
# The only thing we can do is check to see if the initial values are correct
# This is indirect testing, and since we're using 2 methods in the test,
# it's a very limited form of integration testing.


test_item = 'Statistics.create()'
expected = 0
reason = "Initial count value"

# call the operation
stats = S.Statistics()
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


expected = 0
reason = "Initial average value"

# call the operation
stats = S.Statistics()
result = stats.mean()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))




#####################################################################
# test Statistics.add()
# We can't test add() directly, so check add() + count()
# these are integration tests

# Test Case - 1
test_item = 'add() + count()'

expected = 0
reason = "Check count after two value added"

# call the operation
stats = S.Statistics()

result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case - 2
test_item = 'add() + count()'
data_in = [0, 0, 0, 0, 0]
expected = 5
reason = "Check count after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case - 3
test_item = 'add() + count()'
data_in = [1, 2, 3, 4]
expected = 4
reason = "Check count after 4 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case - 4
test_item = 'add() + count()'
data_in = [1, 1, 1, 3, 3]
expected = 5
reason = "Check count after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


from test_statistics import close_enough

# test Statistics.mean()

# Test Case - 1
test_item = 'add() + mean()'
data_in = [2,4]
expected = 2
reason = "Check average after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

# We shouldn't test the floating point values for equality, because or roundoff error
# So use the close_enough() function.

if not S.close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


#####################################################################
# test Statistics.mean()
# Test Case - 2
test_item = 'add() + mean()'
data_in = [0, 0, 0, 0, 0]
expected = 0.0
reason = "Check average after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not S.close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))



print('*** Test script completed ***')
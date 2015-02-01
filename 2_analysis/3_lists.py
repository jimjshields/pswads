# Listing 3

from timeit import Timer

# Four ways of implementing a list of numbers
def test1():
	l = []
	for i in range(1000):
		l += [i]

def test2():
	l = []
	for i in range(1000):
		l.append(i)

def test3():
	l = [i for i in range(1000)]

def test4():
	l = list(range(1000))

# Timing each

# t1 = Timer('test1()', 'from __main__ import test1')
# print 'concat %s milliseconds' % (t1.timeit(number=1000))
# t2 = Timer('test2()', 'from __main__ import test2')
# print 'append %s milliseconds' % (t2.timeit(number=1000))
# t3 = Timer('test3()', 'from __main__ import test3')
# print 'comprehension %s milliseconds' % (t3.timeit(number=1000))
# t4 = Timer('test4()', 'from __main__ import test4')
# print 'list range %s milliseconds' % (t4.timeit(number=1000))

# Listing 4

popZero = Timer('x.pop(0)', 'from __main__ import x')
popEnd = Timer('x.pop()', 'from __main__ import x')

# x = list(range(20000000))
# print popZero.timeit(number=100)

# x = list(range(20000000))
# print popEnd.timeit(number=100)
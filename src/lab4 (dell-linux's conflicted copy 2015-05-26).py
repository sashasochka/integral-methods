f = [
	lambda x: 3   * x**5 + 3 * x**2 - 2 * x - 2,
	lambda x: 15  * x**4 + 6 * x - 2,
	lambda x: 60  * x**3 + 6,
	lambda x: 180 * x**2,
	lambda x: 360 * x,
	lambda x: 360,
]

inf = 10**10
eps = 0.1**6

def signs(t):
	q = [ff(t) for ff in f]
	for i in reversed(range(len(q))):
	if q[i] == 0 or i > 0 and q[i-1] != 0 and (q[i] / abs(q[i]) == q[i-1] / abs(q[i - 1])):
	  q.pop(i)
	return (len(q))//2

def bisect(a, b):
	print('Segment [{:.6f}; {:.6f}]'.format(a,b))
	c = (a + b) / 2
	value = f[0](c)
	if abs(value) < eps:
		return c
	elif (value > 0) ^ (f[0](a) > 0):
		return bisect(a, c)
	return bisect(c, b)


def chords(a, b):
	print('Segment [{:.6f}; {:.6f}]'.format(a,b))
	c = (a*f[0](b) - b*f[0](a)) / (f[0](b) - f[0](a))
	value = f[0](c)
	if abs(value) < eps:
		return c
	elif (value > 0) ^ (f[0](a) > 0):
		return bisect(a, c)
	return bisect(c, b)

def newton(a, b):
	def do(arg):
		print('Current value: {:.6f}'.format(arg))
		value = f[0](arg)
		if abs(value) < eps:
			return arg
		return do(arg - value / f[1](arg))
	return do((a+b)/2)


print('--- BISECTION ALGORITHM -----')
print('-- Searching for roots in range [-4; -0.75]')
print('x1 = {:.6f}'.format(bisect(-4, -0.75)))
print('-- Searching for roots in range [-0.75, -0.5]')
print('x1 = {:.6f}'.format(bisect(-0.75, -0.5)))
print('-- Searching for roots in range [0.25, 4]')
print('x1 = {:.6f}'.format(bisect(0.25, 4)))

print('--- CHORDS ALGORITHM -----')
print('-- Searching for roots in range [-4; -0.75]')
print('x1 = {:.6f}'.format(chords(-4, -0.75)))
print('-- Searching for roots in range [-0.75, -0.5]')
print('x1 = {:.6f}'.format(chords(-0.75, -0.5)))
print('-- Searching for roots in range [0.25, 4]')
print('x1 = {:.6f}'.format(chords(0.25, 4)))

print('--- NEWTON ALGORITHM -----')
print('-- Searching for roots in range [-4; -0.75]')
print('x1 = {:.6f}'.format(newton(-4, -0.75)))
print('-- Searching for roots in range [-0.75, -0.5]')
print('x1 = {:.6f}'.format(newton(-0.75, -0.5)))
print('-- Searching for roots in range [0.25, 4]')
print('x1 = {:.6f}'.format(newton(0.25, 4)))
import turtle

def draw_spiral(my_turtle, line_len):
	"""Recursively draws a spiral with a turtle object."""

	if line_len > 0:
		my_turtle.forward(line_len)
		my_turtle.right(30)
		draw_spiral(my_turtle, line_len - 1)

# draw_spiral(my_turtle, 100)

def tree(branch_len, turtle):
	"""Recursively draws a tree."""

	if branch_len > 5:
		turtle.forward(branch_len)
		turtle.right(20)
		tree(branch_len - 10, turtle)
		turtle.left(40)
		tree(branch_len - 10, turtle)
		turtle.right(20)
		turtle.backward(branch_len)

def main():
	t = turtle.Turtle()
	my_win = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color('green')
	tree(75, t)
	my_win.exitonclick

# tree(50, my_turtle)
# my_win.exitonclick()

main()
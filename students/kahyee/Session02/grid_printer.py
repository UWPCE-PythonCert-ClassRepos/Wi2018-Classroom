corner = "+"
hEdge = "-"
blank = " "
vEdge = "|"

def print_h_line(size, box):
	print((corner + (blank + hEdge) * (size) + blank) * box + corner)

def print_v_line(size, box):
	for i in range(size//2):
		print((vEdge + blank * size) * box + vEdge)

def print_grid(size):
	print_h_line(size // 2, 2)
	print_v_line(size, 2)
	print_h_line(size // 2, 2)
	print_v_line(size, 2)
	print_h_line(size // 2, 2)

print_grid(3)
print_grid(15)


def print_grid2(box, size):
	print_h_line(size, box)
	for i in range(box):
		print_v_line(size * 2 + 1, box)
		print_h_line(size, box)

print_grid2(3,4)
print_grid2(5,3)

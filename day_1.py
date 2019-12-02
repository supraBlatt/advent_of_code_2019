def list_file(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return lines

def part_1():
	masses = [int(x) for x in list_file('modules.txt')]
	overall = 0

	for mass in masses:
	  overall += int(mass/3) - 2

	print(overall)

def part_2():
	masses = [int(x) for x in list_file('modules.txt')]
	overall = 0
	for mass in masses:
	  curMass = mass

	  while True:
	    curMass = int(curMass/3) - 2
	    if (curMass <= 0):
	      break
	    overall += curMass

	print(overall)

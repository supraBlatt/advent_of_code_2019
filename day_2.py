def list_file(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return [int(x) for x in (",".join(lines)).split(",")]

init = list_file("modules.txt")

def part_1(noun, verb):
    commands = init[:] # tmp copy
    commands[1] = noun
    commands[2] = verb

    length = len(init)
    i = 0

    while i < length:
      if commands[i] == 99 or i >= length - 3:
        break
      if commands[i] == 1:
        commands[commands[i+3]] = commands[commands[i+1]] + commands[commands[i+2]]
      else:
        commands[commands[i+3]] = commands[commands[i+1]] * commands[commands[i+2]]
      i += 4

    return commands

def part_2():
    made_it = False
    values = []

    for noun in range(0,100):
    	for verb in range(0,100):
    	  commands = part_1(noun, verb)

    	  if commands[0] == 19690720:
    		made_it = True
    		values = [noun, verb]
    		break

    if made_it == True:
    	print(100*values[0] + values[1])

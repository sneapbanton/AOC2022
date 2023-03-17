

class NumObj():
    def __init__(self, val):
        self.val = val
        self.moved = False

def printorder(order):
    row = ""
    for o in order:
        row += str(o.val) + ", "
    print(row[:-1])



data = open("In1.txt")
ordering = []
original_ordering = []
for line in data:
    new_num_obj = NumObj(int(line))
    ordering.append(new_num_obj)
    original_ordering.append(new_num_obj)

decryption_key = 811589153
nec_factor = decryption_key%len(original_ordering)

for o in original_ordering:
    o.val = o.val*decryption_key

decryption_key = 1

limit = len(ordering)
for i in range(10):

    handler = 0
    while handler < limit:

        current = original_ordering[handler]
        if not current.moved and current.val != 0:
            #printorder(ordering)
            index = ordering.index(current)
            ordering.pop(index)
            steps = (current.val)%len(ordering)
            if current.val < 0:
                steps = -(abs(current.val)%len(ordering))
                new_pos = index + steps
                if index + steps < 0:
                    new_pos = len(ordering) + index + steps
                elif index + steps == 0:
                    new_pos = len(ordering)

            elif index + steps >= len(ordering):
                new_pos = (index+steps)%len(ordering)
            else:
                new_pos = index+steps

            ordering.insert(new_pos, current)
            current.moved = True

        else:
            handler += 1

    for o in original_ordering:
        o.moved = False
    
for i in range(len(ordering)):
    pass#print(ordering[i].val, original_ordering[i].val)

pos_zero = [x.val for x in ordering].index(0)
print("zero pos",pos_zero)
print(ordering[(pos_zero+1000)%limit].val*decryption_key)
print(ordering[(pos_zero+2000)%limit].val*decryption_key)
print(ordering[(pos_zero+3000)%limit].val*decryption_key)
print(sum([ordering[(pos_zero+1000)%limit].val*decryption_key, ordering[(pos_zero+2000)%limit].val*decryption_key, ordering[(pos_zero+3000)%limit].val*decryption_key]))
def tower_of_hanoi(num,first,middle,last):
    assert num>0
    if num==1:
        print('Move disk 1 from',first,"to",last)
        return
    tower_of_hanoi(num-1,first,last,middle)
    print('Move disk',num,'from',first,"to",last)
    tower_of_hanoi(num-1,middle,first,last)

print('Outputs:\nInputs:2')
tower_of_hanoi(2,"A","B","C")
print("\nInputs:3")
tower_of_hanoi(3,"A","B","C")
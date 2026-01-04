def tower_of_hanoi(num,first,middle,last):
    assert num>0
    if num==1:
        print('Move disk from',first,"to",last)
        return
    tower_of_hanoi(num-1,first,last,middle)
    tower_of_hanoi(1,first,middle,last)
    tower_of_hanoi(num-1,middle,first,last)

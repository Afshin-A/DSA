from collections import deque
import itertools
import sys
import time
import os

# Maximum number of disks supported by game
max_disks = 6
# Delay in seconds between each animation
time_delay = 0.2

class TowerOfHanoi() :
    '''
    Simulates a board for the game Tower of Hanoi

    Attributes:
        __rods: List of deque objects, each representing the rods on the board that hold the disks
        __num_disks: Number of disks in the game
        __shapes: list of characters that make up each disk
    '''


    def __init__(self, num_disks: int):
        '''
        Initializes the board object and its attributes

        Parameters:
            num_disks: number of disks in the game
        '''
        if num_disks < 3 or num_disks > max_disks:
            raise ValueError('Supported number of disks: 3-' + str(max_disks))
        self.__rods = [deque(), deque(), deque()]
        self.__num_disks = num_disks
        self.__shapes = ['c', '@', '#', '$', '%', '&', '+', '?', 'Ω', '€']
        # setup disks in rod 1
        for i in range(0, num_disks):
            self.__rods[0].appendleft(
                ' ' * i + self.__shapes[i] * ((max_disks*2)-1-2*i) + ' ' * i
            )
    

    #TODO: change this
    def PrintState(self):
        '''
        Prints the state of the game onto the console
        '''
        time.sleep(time_delay)
        for d in self.__rods:
            print(d)
        print('\n')
        
        lines = []
        for row in itertools.zip_longest(*self.__rods, fillvalue=(max_disks) * ' ' + '|' + (max_disks) * ' '):
            lines.append(''.join(row))
            lines.append('\n')
        output = ''.join(lines)
        print(output)
        
        # Clear the console
        # \033[H moves the cursor to the home position (top-left corner of the console).
        # \033[J clears the screen from the cursor to the end of the screen.
        # sys.stdout.write("\033[H\033[J") 
        
        # sys.stdout.write(output)
        # sys.stdout.flush()


    def __hanoi(self, num_disks: int, from_rod: int, to_rod: int) :
        '''
        Implements the recursive logic of solving the game
        '''
        # base case
        if num_disks == 0:
            return
        other_rod = 3 - (from_rod + to_rod)
        # move n-1 disks from current rod to buffer rod
        self.__hanoi(num_disks - 1, from_rod, other_rod)
        # add animation
        self.PrintState()
        # move largest disk to destination rod
        self.__rods[to_rod].appendleft(self.__rods[from_rod].popleft())
        # move n-1 disks to the destination rod
        self.__hanoi(num_disks - 1, other_rod, to_rod)


    def Solve(self):
        '''
        Public method that kickstarts the solution
        '''
        self.__hanoi(self.__num_disks, 0, 2)


    def GetMinMoves(self):
        '''
        Returns the minimum number of steps needed to solve the game
        '''
        return 2 ** self.num_disks - 1



t = TowerOfHanoi(6)
# t.PrintState()
t.Solve()
# t.PrintState()
# print(os.name)




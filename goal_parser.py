# https://leetcode.com/contest/weekly-contest-218/problems/goal-parser-interpretation/
class Solution:
    state = 0
    def fsm(self, i)->str:
        emit = None
        if i == 'G':
            self.state = 1
            emit = 'G'
        elif i == '(':
            self.state = 2
        elif i == ')':
            if self.state == 2:
                emit = 'o'
            elif self.state == 5:
                emit = 'al'
            self.state = 3
        elif i == 'a':
            self.state = 4
        elif i == 'l':
            self.state = 5
        else:
            print("kaput")
        return emit
            
            
    def interpret(self, command: str) -> str:
        rstr = ""
        for i in range(len(command)):
            # print(f"c:{command[i]}")
            r = self.fsm(command[i])               
            if r is not None:
                rstr = rstr + r
                # print(f"cmd{i}={command[i]} rstr={rstr}")
        return rstr
    

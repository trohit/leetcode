"""
L359. 
https://leetcode.com/problems/logger-rate-limiter/
"""
"""
T: O(1) where 
hash
k     v
msg last_seen

whenever a new msg comes its checked against this hash.
if new msg then we just record {msg,timestamp} and allow it.
else if old msg then
    compute time_diff
    if too soon: discard msg
    else: record new timestamp and allow msg
"""
class Logger:

    def __init__(self):
        self.dd = {} # hash that stores msg and last allowed timestamp
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # iterate thru all msgs
        if message not in self.dd.keys():
            # print(f"{timestamp} {message} : is allowed")
            self.dd[message] = timestamp
            return True

        diff = timestamp - self.dd[message]
        #check diff between last ts
        if diff >= 10:
            # print(f"d:{diff} ts:{timestamp} {message} : allowed")
            self.dd[message] = timestamp # record timestamp
            return True 

        # print(f"d:{diff} ts:{timestamp} {message} : not allowed")
        return False

"""
keep a dict that stores [msg1, last_ts] 
when new msg1 comes in, also checks against the ts for the same msg in the dict  

"""

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
""" 
Elegant impl.
Instead of logging print times, I store when it's ok for a message to be printed again. 
Should be slightly faster, because I don't always have to add or subtract (e.g., timestamp < log[message] + 10) 
but only do in the true case. 

class Logger(object):

    def __init__(self):
        self.ok = {}

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True
"""  
        

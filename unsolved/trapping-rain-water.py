'''
L42
https://leetcode.com/problems/trapping-rain-water/
TC:O(n*h)
SC:O(1)
TLE 318 / 320 test cases passed.

Examplify
  [0,1,0,2,1,0,1,3,2,1,2,1]
       1     1
>  0 0 0 1 0 0 0 2 1 0 1 0
           1 1 1     1
>  0 0 0 0 0 0 0 1 0 0 0 0

Observation
1. 

'''
def xprint(*args, **kwargs):
    return
    print("".join( map(str,args) ),**kwargs)
    
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        -             -
                      -
        -       -     -
        -  -    -  -  -
        -  -  _ -  -  -
        
        state input  next_state  action
        init     0      init        -
        init     1      wall        -
        wall     0      bet         water++
        wall     1      wall        -
        wet      0      bet         water++
        wet      1      wall        -
        
        10-init 20-wall 30-wet
        
        '''
        # curr_state i/p nxt_state
        fsm = {"init":{0:"init", 
                       1:"wall"}, 
               "wall":{0:"wet", 
                       1:"wall"}, 
               "wet":{0:"wet",
                      1:"wall"}}
        def do_fsm(fsm, curr_state, cell_val, lvl_wat, tmp_wat):
            new_st = fsm[curr_state][cell_val]
            if new_st == "wall" and curr_state == "wet":
                xprint(f"adding tw:{tmp_wat} to lw:{lvl_wat}")
                lvl_wat += tmp_wat
                tmp_wat = 0 # is this needed?
            if new_st == "wet":
                tmp_wat += 1
            else:
                tmp_wat = 0
            xprint(f"{curr_state}+{cell_val}=>{new_st} tw:{tmp_wat}")
            return new_st, lvl_wat, tmp_wat
            
        states = ["init", "wall", "wet"]
        water = 0
        lvl_water = 0
        lvl = 0
        while True:
            curr_state = states[0]
            lvl += 1
            tmp_wat = 0
            lvl_wat = 0
            xprint(f"h :{height} lvl:{lvl} w:{water}")
            # lvl process
            if sum(height) > 0:
                slice = [ 1 if x >= 1 else 0 for x in height ]
                xprint(f"sl:{slice}")
                for cell_val in slice:
                    new_st, lvl_wat, tmp_wat = do_fsm(fsm, curr_state, cell_val, lvl_wat, tmp_wat)
                    '''
                    elif curr_state == "wet":
                        tmp_wat += 1
                    '''
                    curr_state = new_st
                height = [ x-1 if x > 0 else 0 for x in height ]
            else:
                xprint("closing")
                break
            xprint(f"adding lw:{lvl_wat} to {water}")
            water += lvl_wat
        xprint(water)
        return water
        

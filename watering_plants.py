# https://leetcode.com/discuss/interview-question/356449

def fill_water(index:int, steps)->int:
    print("returning to fill water")
    capacity = 6    
    steps = steps + index*2
    print(f"steps:{steps} index:{index}")
    return steps, capacity

def water_plants(a:list, capacity:int)->int :
    steps = 0
    index = 0
    a.insert(0,0)
    print(a)
    
    while index != len(a):
        while capacity > 0:
            if index == len(a):
                print("done watering!")
                return steps
            if index < len(a) and capacity < a[index]:
                print(f"next plant at {index} needs {a[index]}")
                steps, capacity = fill_water(index, steps)
            print("moving >")
            steps += 1
            new_cap = capacity - a[index]
            print(f"after st:{steps} watered plant {index} :{capacity}-{a[index]}={new_cap}")
            capacity = new_cap
            index += 1
        steps, capacity = fill_water(index, steps)
    return steps
    
#driver code
if __name__ == "__main__":
    l = [2,4,5,1,2]
    steps = water_plants(l, 6)
    print(f"steps needed is {steps}") 

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num   #num = 4,9,2,1
    return total  # total = 4 -> 13 -> 15 -> 16
result = tally([4,9,2,1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])  #idx = 0, 1, 2, 3
    return new_list                 #new_list = [4] = [4, 9] = [4, 9, 2] = [4, 9, 2, 1]

result = copy([4, 9, 2, 1]) #this loop copies the list inputted, while the loop above tallys up all values of the list into a single sum

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1) #value = 4, 9, 2, 1
     #new_list = [5] = [5,10] = [5,10,3] = [5,10,3,2]
    return new_list

result = increment_all([4,9,2,1])
print()
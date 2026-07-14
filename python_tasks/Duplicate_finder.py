print("\nWelcome to the duplicate finder\n")
nums =list(x.strip() for x in input("Enter your numbers separated by a comma: ").split(','))

unique_nums = set(nums)

appear_once = set()
appear_more_than_once = set()
appear_more_than_twice = set()

for x in unique_nums:
    count = nums.count(x)

    if count == 1:
        appear_once.add(x)

    if count > 1:
        appear_more_than_once.add(x)
    
    if count > 2:
        appear_more_than_twice.add(x)

print(f"\nNumbers which appear exactly once are : {appear_once}")
print(f"\nNumbers which appear more than once are : {appear_more_than_once}")
print(f"\nNumbers which appear more than twice are : {appear_more_than_twice}")
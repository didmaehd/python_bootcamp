

heights = input("Enter all heihgt : ").split(" ")
for n in range(0,len(heights)):
    heights[n] = int(heights[n])

count = 0
height = 0
for i in heights: 
    height += i
    count += 1

# print(count)
average = height / len(heights)
print(f"Total Heights : {height} \nCount of people : {len(heights)} \nHeights Average : {average}")
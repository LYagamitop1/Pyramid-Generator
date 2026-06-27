
num = int(input("Enter number of rows in a pyramid: "))


      
      
print(f"""
      Type 1: Star style - right angled triangle
      
      """)

for i in range(num):
    j=0
    row_stars = []
    while j<=i:  
        row_stars.append("*")  
        j += 1
    x = " ".join(row_stars)
    print(x)




print(f"""
      Type 2: Column number style - right angle triangle
      
      """)

for i in range(num):
    j=0
    row_stars = []
    while j<=i:  
        row_stars.append(str(j+1))        
        j += 1
    x = " ".join(row_stars)
    print(x)
    
    
    
print(f"""
      Type 3: Proper pyramid - triangle
      
      """)



middle = 30  

no_of_stars = 1
for i in range(num):
    j=0
    row_stars = []
    
    while j<=middle - i:  
        row_stars.append(" ")        
        j += 1
    for k in range(no_of_stars):
        row_stars.append("*")
        
    x = " ".join(row_stars)
    
    no_of_stars += 2
    print(x)
    
 
print(f"""
      Type 4: Kite pattern
      
      """)
 
     
# num = 10

middle = 30  

no_of_stars = 1
for i in range(num):
    j=0
    row_stars = []
    
    while j<=middle - i:  
        row_stars.append(" ")        
        j += 1
    for k in range(no_of_stars):
        row_stars.append("*")
        
    x = " ".join(row_stars)
    
    no_of_stars += 2
    print(x)




no_of_stars = 2*num - 1
middle = 30 - no_of_stars//2
for i in range(num):
    j=0
    row_stars = []
    
    while j<=middle + i:  
        row_stars.append(" ")        
        j += 1
    for k in range(no_of_stars):
        row_stars.append("*")
        
    x = " ".join(row_stars)
    
    no_of_stars -= 2
    print(x)


print(f"""
      Type 5: Shadow style
      
      """)


middle = 30  

no_of_stars = 1
for i in range(num):
    j=0
    row_stars = []
    
    while j<=middle - i:  
        row_stars.append(" ")        
        j += 1
    for k in range(no_of_stars):
        row_stars.append("*")
        
    x = " ".join(row_stars)
    
    no_of_stars += 2
    print(x)

print("")

no_of_stars = 2*num - 1
middle = 30 - no_of_stars//2 -1
for i in range(num):
    j=0
    row_stars = []
    
    while j<=middle - i:  
        row_stars.append(" ")        
        j += 1
    for k in range(no_of_stars):
        row_stars.append("*")
        
    x = " ".join(row_stars)
    
    no_of_stars -= 2
    print(x)



print(f"""
      Type 6: 
      
      """)





width = len(str(num))      # 2 for 15, 3 for 100, etc.

for i in range(num):
    j = 0
    num_list = []

    while j <= i:
        num_list.append(f"{j+1:>{width}}")   # Right-align each number
        j += 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" " * width)         # Blank space of same width
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)


    
        
    

print(f"""
      Type 7: 
      
      """)
    
    



alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



spaces = 30

for i in range(num):
    pattern_list = []
    j=0
      
    while j<=spaces:
        pattern_list.append(" ")
        j += 1     
    
    spaces -= 1
    
    rev_list = []
    rev_list += alphabets[0:i]
    rev_list.reverse()
    
    
    letter_list = pattern_list + alphabets[0:i+1] + rev_list

    
    x = " ".join(letter_list)
    
    print(x)



print(f"""
      Type 8: 
      
      """)

for i in range(num):
    j = num - i
    num_list = []

    while j != 0:
        num_list.append("*") 
        j -= 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" ")
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)
    
    
for i in range(num):
    j = 0
    num_list = []

    while j <= i:
        num_list.append("*") 
        j += 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" ")
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)



print(f"""
      Type 9: 
      
      """)



for i in range(num):
    j = 0
    num_list = []

    while j <= i:
        num_list.append("*") 
        j += 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" ")
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)


for i in range(num):
    j = num - i -1
    num_list = []

    while j != 0:
        num_list.append("*") 
        j -= 1

    no_of_spaces = num - len(num_list)

    while no_of_spaces != 0:
        num_list.append(" ")
        no_of_spaces -= 1

    final_list = " ".join(num_list + num_list[::-1])

    print(final_list)
    
    

print(f"""
      Type 10: Concentric NUmber Pattern
      
      """)



pattern_list = []
number_track = num
width = len(str(num))

for i in range(num):
          
    k = num - len(pattern_list)
    while k!=0:
        pattern_list.append(number_track)
        k -= 1
        
    second_reversed_part = pattern_list[:len(pattern_list)-1]
    second_reversed_part.reverse()
    
    final_list = pattern_list + second_reversed_part
    
    
    number_track -= 1
    
    x = " ".join(f"{v:>{width}}" for v in final_list)
    print(x)
    
    j = num - i - 1
    while j!=0:
        pattern_list.pop()
        j -= 1
        
        


number_track = 2

for i in range(num-1):
    
    j = i+1
    while j!=0:
        pattern_list.pop()
        j -= 1
          
    k = num - len(pattern_list)
    while k!=0:
        pattern_list.append(str(number_track))
        k -= 1
        
    second_reversed_part = pattern_list[:len(pattern_list)-1]
    second_reversed_part.reverse()
    
    final_list = pattern_list + second_reversed_part
    
    
    number_track += 1
    
    x = " ".join(f"{int(v):>{width}}" for v in final_list)
    print(x)
    


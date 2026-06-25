
num = int(input("Enter number of rows in a pyramid: "))


      
      
print(f"""
      Type 1: Star number style
      
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
      Type 2: Column number style
      
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
      Type 3: Proper pyramid
      
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




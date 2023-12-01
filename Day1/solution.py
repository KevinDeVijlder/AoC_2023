#Challenge 1
with open('input.txt', 'r') as f:
    lines = f.readlines()

    
    SumOfAll = 0
    LineString = ""
    LineSum = 0
    placeholder = 0
    for line in lines:
        for character in line:
            if(character.isdigit()): 
                LineString += character
        print("Linestring: " + LineString)   
        LineStringFirst = LineString[0]
        LineStringLast = LineString[len(LineString) - 1]
        LineSum = int(LineStringFirst + LineStringLast)
        print("LineSum:" + str(LineSum))
        SumOfAll = SumOfAll + LineSum
        print("SumOfAll: " + str(SumOfAll))
        LineString = ""
        LineSum = 0
        print("-----------------------------------------")
    

# Challenge 2

    

print("The result for AoC day X part 1 is: " + str(SumOfAll))
print("The result for AoC day X part 2 is: " + str(placeholder)) 
print(r"""     
     *
    ***
   *****
  *******
 *********
     * 
Merry Xmas!""")
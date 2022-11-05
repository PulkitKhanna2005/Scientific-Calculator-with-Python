import math
import calendar
import datetime
import statistics
print("This is a program specially designed by Pulkit to work as an all-round calculator.")
print("The user may find below a list of the functions that can be implemented through this program:")
print("")
print(" -> 0. Quit/Exit/Close")
print(" -> 1. Addition")
print(" -> 2. Subtraction")
print(" -> 3. Multiplication")
print(" -> 4. Division")
print(" -> 5. Raising to the power of n")
print(" -> 6. Calculate nth root")
print(" -> 7. Floor Division")
print(" -> 8. Modulo")
print(" -> 9. Modulus(calculates absolute value for real numbers and")
print("       the distance from origin for imaginary numbers)")
print(" -> 10. Reciprocal")
print(" -> 11. Area of a Square")
print(" -> 12. Area of a Rectangle")
print(" -> 13. Area of a Triangle (for right-angled triangles)")
print(" -> 14. Area of a Triangle (with Heron's Formula)")
print(" -> 15. Area of a Circle")
print(" -> 16. Area of a Trapezium")
print(" -> 17. Total Surface Area, Lateral Surface Area and Volume of a Cube")
print(" -> 18. Total Surface Area, Lateral Surface Area and Volume of a Cuboid")
print(" -> 19. Total Surface Area, Curved Surface Area and Volume of a Cone")
print(" -> 20. Total Surface Area, Curved Surface Area and Volume of a Sphere")
print(" -> 21. Total Surface Area, Curved Surface Area and Volume of a Hemisphere")
print(" -> 22. Total Surface Area, Curved Surface Area and Volume of a Cylinder")
print(" -> 23. Body Mass Index")
print(" -> 24. Factorial")
print(" -> 25. Logarithm")
print(" -> 26. Statistics(Mean/Median/Mode)")
print(" -> 27. Length of a given string")
print(" -> 28. Interest(Simple/Compound)")
print(" -> 29. Angle Converter")
print(" -> 30. Sums of odd and even numbers between 0 and the given number")
print(" -> 31. Sum of digits of an integer")
print(" -> 32. Temperature in celsius to farenheit and kelvin")
print(" -> 33. Temperature in farenheit to celsius and kelvin")
print(" -> 34. Temperature in kelvin to farenheit and celsius")
print(" -> 35. Zeroes of a Quadratic Polynomial")
print(" -> 36. Sine of an angle(input in radians)")
print(" -> 37. Cosine of an angle(input in radians)")
print(" -> 38. Tangent of an angle(input in radians)")
print(" -> 39. Discount Calculator (with pre-defined discount rates in %)")
print(" -> 40. Discount Calculator (user inputs discount rate in %)")
print(" -> 41. Calculate maximum and minimum of n natural numbers")
print(" -> 42. Average of n numbers")
print(" -> 43. Calculate floor value")
print(" -> 44. Calculate ceiling value")
print(" -> 45. ASCII value calculator")
print(" -> 46. HCF & LCM calculator(for two numbers only)")
print(" -> 47. Count the number of occurrences of a character/s in a string")
print(" -> 48. Calculate calendar for a given month of a given year")
print(" -> 49. Decimal to Binary, Octal and Hexadecimal Converter")
print(" -> 50. M-L-T Converter")
print("")
print("PLEASE VIEW IN FULL SCREEN & SCROLL UP!")
print("")
num = ""
while num!=0:
    num=int(input("Enter your choice(select number from index): "))
    if num<0:
        print("Invalid Input! Please try again.")
        
    elif num==0:
        print("")
        print("Thank you for using this program!")
        print("")
        print("Rate this program? Yes/No")
        ans=input("")
        if ans=='Yes':
            i=int(input("Please give your feedback on a scale of 1 to 5: "))
            print("Thank you for your feedback.")
        else:
            print("Thank you for your time!")
        print("Last attempt took place on/at: ",datetime.datetime.now())
        print("")
            
    elif num==1:
        print("You have chosen Addition!")
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        Sum=a+b                                                                              #Addition
        print("The sum of",a,"and",b,"is: ",Sum)
        
    elif num==2:
        print("You have chosen Subtraction!")
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        diff=a-b                                                                            #Subtraction
        print("The difference of",a,"and",b,"is: ",diff)
        
    elif num==3:
        print("You have chosen Multiplication!")
        a=float(input("Enter the main number: "))
        b=float(input("Enter the number to be multiplied with: "))
        prod=a*b                                                                            #Multiplication
        print("The product of",a,"and",b,"is: ",prod)
        
    elif num==4:
        print("You have chosen Divison!")
        a=float(input("Enter the Dividend: "))
        b=float(input("Enter the Divisor: "))
        quo=a/b                                                                             #Division
        print("The quotient obtained after dividing",a,"and",b,"is: ",quo)
        
    elif num==5:
        print("You have chosen Raising to the power of n!")
        a=float(input("Enter the main number: "))
        b=float(input("Enter the power to be raised to: "))
        Pow=a**b                                                                            #To power n
        print("The result of raising",a,"to the power of",b,"is: ",Pow)
        
    elif num==6:
        print("You have chosen Calculate nth root!")
        a=float(input("Enter the main number: "))
        b=float(input("Enter the root value: "))
        root=(a**(1/b))                                                                     #nth root
        print("The final result of finding the",b,"st/nd/rd/th root of",a,"is: ",root)
        
    elif num==7:
        print("You have chosen Floor Division!")
        a=float(input("Enter the Dividend: "))
        b=float(input("Enter the Divisor: "))
        fquo=a//b                                                                           #Floor Division
        print("The quotient obtained after floor-dividing",a,"and",b,"is: ",fquo)
        
    elif num==8:
        print("You have chosen Modulo!")
        a=float(input("Enter the Dividend: "))
        b=float(input("Enter the Divisor: "))
        mod=a%b                                                                             #Modulo(gives remainder)
        print("The remainder left after dividing",a,"by",b,"is: ",mod)
        
    elif num==9:
        print("You have chosen Modulus!")
        print("Choose the type of input: ")
        print("->  i.Real Number")
        print("->  ii.Complex Number")
        z=(input("Enter your choice(select character from index): "))
        if z=='i':
            a=float(input("Enter the number: "))
            Abs=abs(a)                                                                      #Modulus of real number      
            print("The absolute value of the real number",a,"is: ",Abs)
        elif z=='ii':
            a=int(input("Enter the real part of the number: "))
            b=int(input("Enter the imaginary part of the number: "))
            d=(a*a)+(b*b)
            mds=math.sqrt(d)                                                                #Modulus of imaginary number
            print("The modulus of the imaginary number",a,"+(i*",b,")is: ",mds)
        else:
            print("Invalid Input! Please try again.")
            
    elif num==10:
        print("You have chosen Reciprocal!")
        a=float(input("Enter the number: "))
        rec=1/a                                                                                 #Reciprocal
        print("The reciprocal of",a,"is: ",rec)
        
    elif num==11:
        print("You have chosen Area of a Square!")
        a=float(input("Enter the side length in units: "))
        sqar=a**2                                                                               #Area of Square
        print("The area of a square of side",a,"is: ",sqar,"square units.")
        
    elif num==12:
        print("You have chosen Area of a Rectangle!")
        a=float(input("Enter the length in units: "))
        b=float(input("Enter the breadth in units: "))
        rcar=a*b                                                                                #Area of rectangle
        print("The area of a rectangle of length",a,"and breadth",b,"is: ",rcar,"square units.")
        
    elif num==13:
        print("You have chosen Area of a Right-angled Triangle!")
        a=float(input("Enter the height in units: "))
        b=float(input("Enter the base in units: "))
        trar=0.5*a*b                                                                            #Area of right triangle
        print("The area of a triangle of height",a,"and base",b,"is: ",trar,"square units.")
        
    elif num==14:
        print("You have chosen Area of a Triangle(with Heron's Formula)!")
        a=float(input("Enter the first side in units: "))
        b=float(input("Enter the second side in units: "))
        c=float(input("Enter the third side in units: "))
        s=(a+b+c)*0.5
        d=s*(s-a)*(s-b)*(s-c)
        trar=math.sqrt(d)                                                                       #Area of triangle(Heron)
        print("The area of a triangle of sides",a,",",b,",",c,"is: ",trar,"square units.")
        
    elif num==15:
        print("You have chosen Area of a Circle!")
        a=float(input("Enter the radius in units: "))
        crar=math.pi*(a**2)                                                                         #Area of circle
        print("The area of a circle of radius",a,"is: ",crar,"square units.")
        
    elif num==16:
        print("You have chosen Area of a Trapezium!")
        a=float(input("Enter the first parallel side in units: "))
        b=float(input("Enter the second parallel side in units: "))
        c=float(input("Enter the distance between the two parallel sides in units: "))
        tpar=0.5*(a+b)*c                                                                           #Area of trapezium
        print("The area of the trapezium is: ",tpar,"sqaure units.")
        
    elif num==17:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Cube!")
        a=float(input("Enter the side length in units: "))
        cbta=6*a*a                                                                                  #Cube operations
        cbla=4*a*a
        cbvl=a**3
        print("The Total Surface Area of a cube of side",a,"is: ",cbta,"square units.")
        print("The Lateral Surface Area of a cube of side",a,"is: ",cbla,"square units.")
        print("The Volume of a cube of side",a,"units is: ",cbvl,"cubic units.")
        
    elif num==18:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Cuboid!")
        a=float(input("Enter the length in units: "))
        b=float(input("Enter the breadth in units: "))
        c=float(input("Enter the height in units: "))
        cdta=2*((a*b)+(b*c)+(a*c))                                                                  #Cuboid operations
        cdla=2*c*(a+b)
        cdvl=a*b*c
        print("The Total Surface Area of the cuboid is: ",cdta,"square units.")
        print("The Lateral Surface Area of the cuboid is: ",cdla,"square units.")
        print("The Volume of the cuboid is: ",cdvl,"cubic units.")
        
    elif num==19:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Cone!")
        a=float(input("Enter the height in units: "))
        b=float(input("Enter the radius in units: "))
        l=math.sqrt((a*a)+(b*b))                                                                    #Cone operations
        cnta=math.pi*b*(l+b)
        cnla=math.pi*b*l
        cnvl=0.33*math.pi*(b*b)*a
        print("The Total Surface Area of the cone is: ",cnta,"square units.")
        print("The Lateral Surface Area of the cone is: ",cnla,"square units.")
        print("The Volume of the cone is: ",cnvl,"cubic units.")
        
    elif num==20:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Sphere!")
        a=float(input("Enter the radius in units: "))
        spta=4*math.pi*(a*a)                                                                        #Sphere operations
        spla=4*math.pi*(a*a)
        spvl=1.33*math.pi*(a**3)
        print("The Total Surface Area of the sphere is: ",spta,"square units.")
        print("The Lateral Surface Area of the sphere is: ",spla,"square units.")
        print("The Volume of the sphere is: ",spvl,"cubic units.")
        
    elif num==21:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Hemisphere!")
        a=float(input("Enter the radius in units: "))
        hsta=3*math.pi*(a*a)                                                                        #Hemisphere operations
        hsla=2*math.pi*(a*a)
        hsvl=0.67*math.pi*(a**3)
        print("The Total Surface Area of the hemisphere is: ",hsta,"square units.")
        print("The Lateral Surface Area of the hemisphere is: ",hsla,"square units.")
        print("The Volume of the hemisphere is: ",hsvl,"cubic units.")
        
    elif num==22:
        print("You have chosen Total Surface Area, Lateral Surface Area and Volume of a Cylinder!")
        a=float(input("Enter the radius in units: "))
        b=float(input("Enter the height in units: "))
        cyta=2*math.pi*a*(a+b)                                                                      #Cylinder operations
        cyla=2*math.pi*a*b
        cyvl=math.pi*a*a*b
        print("The Total Surface Area of the cylinder is: ",cyta,"square units.")
        print("The Lateral Surface Area of the cylinder is: ",cyla,"square units.")
        print("The Volume of the cylinder is: ",cyvl,"cubic units.")
        
    elif num==23:
        print("You have chosen Body Mass Index!")
        a=float(input("Enter the weight in kilograms: "))
        b=float(input("Enter the height in metres: "))
        bmi=a/(b*b)                                                                                 #Body Mass Index
        print("The BMI of a person weighing",a,"kgs and who is",b,"metres tall is: ",bmi)
        
    elif num==24:
        print("You have chosen Factorial!")
        a=int(input("Enter the number: "))
        fact = 1
        if a < 0:
           print("Sorry, factorial does not exist for negative numbers")
        elif a == 0:
           print("The factorial of 0 is 1")
        else:
           for i in range(1,a + 1):
               fact = fact*i                                                                          #Factorial
        print("The factorial of",a,"is: ",fact)
        
    elif num==25:
        print("You have chosen Logarithm!")
        print("Choose preferred type:")
        print("->  i.Natural Logarithm (base:e)")
        print("->  ii.Standard Logarithm (base: user-input)")
        q=(input("Enter your choice(select character from index): "))
        if q=='i':
            a=float(input("Enter the number: "))
            if a==0:
                print("Log of 0 to base e is not defined!")
            else:
                nlog=math.log(a)                                                                        #Logarithm
                print("The natural logarithm of",a,"is: ",nlog)
        elif q=='ii':
            a=float(input("Enter the number: "))
            if a==0:
                print("Log of 0 to any base is not defined!")
            else:
                b=float(input("Enter the base: "))
                log=math.log(a,b)                                                                       
                print("The logarithm of",a,"to the base of",b,"is: ",log)
        else:
            print("Invalid Input! Please try again.")
        
    elif num==26:
        print("You have chosen Statistics!")
        print("Choose required option:")
        print("->  i.Mean")                                                                             #Statistics
        print("->  ii.Median")
        print("->  iii.Mode")
        q=(input("Enter your choice(select character from index): "))
        lst=eval(input("Enter the list of values: "))
        if q=='i':
            print("Mean of the given list is: ",statistics.mean(lst))
        elif q=='ii':
            print("Median of the given list is: ",statistics.median(lst))
        elif q=='iii':
            print("Mode of the given list is: ",statistics.mode(lst))
        else:          
            print("Invalid Input! Please try again.")
            
    elif num==27:
        print("You have chosen Length of a given string!")
        a=input("Enter the string: ")
        b=len(a)                                                                                     #Length of string
        print("The length of string",a,"including blank spaces is: ",b)
        
    elif num==28:
        print("You have chosen Interest(Simple/Compound)!")
        print("Choose the type of interest to be calculated: ")
        print("->  i.Simple Interest")
        print("->  ii.Compound Interest")
        z=(input("Enter your choice(select character from index): "))
        if z=='i':
            a=float(input("Enter the principle amount: " ))                                         #Interest Calculator
            b=float(input("Enter the rate of interest: " ))
            c=float(input("Enter the time in years: " ))
            si=(a*b*c)/100
            amt=si+a
            print("The Simple Interest calculated per annum is: ",si)
            print("The amount payable is: ",amt)
        elif z=='ii':
            p = float(input("Enter the principal amount : ")) 
            t = float(input("Enter the number of years : "))
            r = float(input("Enter the rate of interest : "))
            amt=  p * (pow((1 + r / 100), t))
            ci=amt-p
            print("The value of the Compound Interest at the rate of",r,"% for",t,"years is: ",ci)
            print("The Amount payable after compounding at the rate of",r,"% for",t,"years is: ",amt)
        else:
            print("Invalid Input! Please try again.")
            
    elif num==29:
        print("You have chosen Angle Converter!")
        print("->  a.Degrees to Radians")                                                               #Angle converter
        print("->  b.Radians to Degrees")
        f=(input("Enter your choice(select character from index): "))
        if f=='a':
            a=float(input("Enter the angle in degrees: "))
            b=0.01745329*a
            print("The angle",a,"degrees is the same as",b,"radians.")
        elif f=='b':
            print("You have chosen Angle in radians to degrees!")
            a=float(input("Enter the angle in radians: "))
            b=57.2957795*a
            print("The angle",a,"radians is the same as",b,"degrees.")
        else:
            print("Invalid Input! Please try again.") 
            
    elif num==30:
        print("You have chosen Sums of odd and even numbers between 0 and the given number!")
        a=int(input("Enter the number: " ))
        i=1 
        sum1,sum2=0,0
        while i<=a:
            if i%2==0:
                sum1+=i                                                                             #Sum of odd and even numbers
            else:
                sum2+=i
            i+=1 
        print("The sum of even integers is: ",sum1)
        print("The sum of odd integers is: ",sum2)
        
    elif num==31:
        print("You have chosen Sum of digits of an integer!")
        a = int(input("Enter a number: " ))
        sum1 = 0
        for i in a :
            sum1 += int (i)                                                                         #Sum of digits of an integer
        print("Sum of digits: ", sum1)
        
    elif num==32:
        print("You have chosen Temperature in celsius to farenheit and kelvin!")
        a=float(input("Enter the temperature in celsius: "))
        b=((9*a)+160)/5                                                                                 #Celsius to others
        c=(a+(273.15))
        print("The temperature",a,"degrees celsius is the same as",b,"degrees farenheit and",c,"kelvin.")
        
    elif num==33:
        print("You have chosen Temperature in farenheit to celsius and kelvin!")
        a=float(input("Enter the temperature in farenheit: "))
        b=((5*a)-160)/9                                                                                 #Farenheit to others
        c=(b+(273.15))
        print("The temperature",a,"degrees farenheit is the same as",b,"degrees celsius and",c,"kelvin.")
        
    elif num==34:
        print("You have chosen Temperature in kelvin to celsius and farenheit!")
        a=float(input("Enter the temperature in kelvin: "))
        b=(a-(273.15))                                                                                  #Kelvin to others
        c=((9*b)+160)/5
        print("The temperature",a,"kelvin is the same as",b,"degrees celsius and",c,"degrees farenheit.")
        
    elif num==35:
        print("You have chosen Zeroes of a Quadratic Polynomial!")
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))   
        c=int(input("Enter the value of c:"))
        if a==0:
            print("Value of a can't be zero")
        else:
            d=b*b-4*a*c                                                                                 #Zeroes of quadratic
            if d>0:
                root1=(-b+math.sqrt(d))/(2*a)
                root2=(-b-math.sqrt(d))/(2*a)
                print("Roots are real and unequal")
                print("The zeroes of the Quadratic Polynomial",a,"x^2+",b,"x+",c,"are: ",root1,"and",root2)
            elif d==0:
                root1=-b/(2*a) 
                print("Roots are real and equal")
                print("The zeroes of the Quadratic Polynomial",a,"x^2+",b,"x+",c,"are: ",root1,"and",root2)
            else:
                print("Roots are complex and imaginary.")
                
    elif num==36:
        print("You have chosen Sine of an angle(input in radians)!")
        a=float(input("Enter the angle in radians: "))
        b=math.sin(a)                                                                                           #Sine
        print("The sine of",a,"radians is: ",b,".")
        
    elif num==37:
        print("You have chosen Cosine of an angle(input in radians)!")
        a=float(input("Enter the angle in radians: "))
        b=math.cos(a)                                                                                           #Cosine
        print("The cosine of",a,"radians is: ",b,".")
        
    elif num==38:
        print("You have chosen Tangent of an angle(input in radians)!")
        a=float(input("Enter the angle in radians: "))
        b=math.tan(a)                                                                                           #Tangent
        print("The tangent of",a,"radians is: ",b,".")

    elif num==39:
        print("You have chosen Discount Calculator (with predefined discount rates in %)!")
        print("For amounts less than or equal to ₹5000, discount% = 10%.")
        print("For amounts greater than ₹5000 but less than or equal to ₹15000, discount% = 15%.")
        print("For amounts greater than ₹15000 but less than or equal to ₹25000, discount% = 20%.")
        print("For amounts greater than ₹25000, discount% = 30%.")
        amt=float(input("Enter undiscounted amount: ₹"))
        if(amt>0):
            if amt<=5000:
               disc = amt*0.10
            elif amt<=15000:
                disc=amt*0.15
            elif amt<=25000:
                disc=0.20 * amt
            else:
                 disc=0.30 * amt                                                                            #Discount: predefined
            print("Discount value : ₹",disc)
            print("Final amount to be paid: ₹",amt-disc)
        else:
            print("Invalid amount entered.")

    elif num==40:
        print("You have chosen Discount Calculator (user inputs discount rate in %)!")
        amt=float(input("Enter undiscounted amount: ₹"))
        disc=float(input("Enter the discount rate in %: "))
        a=(disc*amt)/100                                                                                    #Discount: User-defined
        b=amt-a
        print("Discount value : ₹",a)
        print("Final amount to be paid: ₹",b)
        
    elif num==41:
        print("You have chosen Calculate maximum and minimum of n natural numbers!")
        lst = eval(input("Enter the list of natural numbers: "))
        print("Maximum element in the list is :", max(lst))                                                 #Max and Min in a list
        print("Minimum element in the list is :", min(lst))

    elif num==42:
        print("You have chosen Average of n numbers!")
        n = int(input('How many numbers to calculate from? '))
        sum1 = 0
        for i in range (n):
            print("Enter number",i+1,": ",end=" ")
            a = float(input())
            sum1 += a
        avg = sum1 / n                                                                                      #Average of list 
        print("The average value of the given",n,"numbers is: ",avg)

    elif num==43:
        print("You have chosen Calculate floor value!")
        a=float(input("Enter the number: "))
        print("The floor value of the given number is: ",math.floor(a))                                         #Floor

    elif num==44:
        print("You have chosen Calculate ceil value!")
        a=float(input("Enter the number: "))
        print("The ceiling value of the given number is: ",math.ceil(a))                                         #Ceil   

    elif num==45:
        print("You have chosen ASCII value calculator!")
        char=input("Please Enter Character :- ")
        convert=ord(char)                                                                                       #ASCII
        print("The ASCII value of '" + char + "' is", convert)

    elif num==46:
        print("You have chosen HCF & LCM calculator (for two numbers only)!")
        print("->  a.HCF")
        print("->  b.LCM")
        g=(input("Enter your choice(select character from index): "))                                           #HCF/LCM
        if g=='a':
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))
            print("The HCF of",a,"and",b,"is: ",math.gcd(a,b))
        elif g=='b':
            a=int(input("Enter the first number: "))
            b=int(input("Enter the second number: "))
            print("The LCM of",a,"and",b,"is: ",math.lcm(a,b))
        else:
            print("Invalid Input! Please try again.")

    elif num==47:
        print("You have chosen Count the number of occurrences of a character/s in a string")
        a=input("Enter the string: ")
        b=input("Enter the charater/s: ")
        c=a.count(b)                                                                                #Occurences of chars in string
        print("The total number of occurences of",b,"in",a,"are: ",c)

    elif num==48:
        print("You have chosen Calculate calendar for a given month of a given year!")
        yy=int(input("Enter the year: "))                                                                       #Calendar
        mm=int(input("Enter the month number (Eg -> August is 8): "))
        print(calendar.month(yy, mm))

    elif num==49:
        print("You have chosen Decimal to Binary, Octal and Hexadecimal Converter!")
        dec=int(input("Enter the number in the decimal system: "))
        print("->  a.To binary")
        print("->  b.To octal")
        print("->  c.To hexadecimal")
        e=(input("Enter your choice(select character from index): "))                                       #Decimal to others
        if e=='a':
            print("The binary value of the decimal number",dec,"is: ",(bin(dec))[2:])
        elif e=='b':
            print("The octal value of the decimal number",dec,"is: ",(oct(dec))[2:])
        elif e=='c':
            print("The hexadecimal value of the decimal number",dec,"is: ",(hex(dec))[2:])
        #[2:] added to code in order to remove the type-identifying alphanumeric characters from the result.
        else:
            print("Invalid Input! Please try again.")
       
    elif num==50:
        print("You have chosen M-L-T Converter!")
        print("->  a.Mass Converter")                                                               #Mass/Length/Time unit conversion 
        print("->  b.Length Converter")
        print("->  c.Time Converter")
        p=(input("Enter your choice(select character from index): "))
        if p=='a':
            print("You have chosen Mass Converter!")
            print("Choose the unit of the input:")
            print("->  i.Milligrams")
            print("->  ii.Grams")
            print("->  iii.Kilograms")
            q=(input("Enter your choice(select character from index): "))
            if q=='i':
                a=float(input("Input in milligrams:"))
                b=a/1000
                c=b/1000
                print(a,"mg is the same as",b,"g and",c,"kg.")
            elif q=='ii':
                a=float(input("Input in grams:"))
                b=a*1000
                c=a/1000
                print(a,"g is the same as",b,"mg and",c,"kg.")
            elif q=='iii':
                a=float(input("Input in kilograms:"))
                b=a*1000
                c=b*1000
                print(a,"kg is the same as",b,"g and",c,"mg.")
            else:
                print("Invalid Input! Please try again.")
        elif p=='b':
            print("You have chosen Length Converter!")
            print("Choose the unit of the input:")
            print("->  i.Millimetres")
            print("->  ii.Centimetres")
            print("->  iii.Metres")
            print("->  iv.Kilometres")
            q=(input("Enter your choice(select character from index): "))
            if q=='i':
                a=float(input("Input in millimetres:"))
                b=a/10
                c=b/100
                d=c/1000
                print(a,"mm is the same as",b,"cm,",c,"m and",d,"km.")
            elif q=='ii':
                a=float(input("Input in centimetres:"))
                b=a*10
                c=a/100
                d=c/1000
                print(a,"cm is the same as",b,"mm,",c,"m and",d,"km.")
            elif q=='iii':
                a=float(input("Input in metres:"))
                b=a*1000
                c=b/10
                d=a/1000
                print(a,"m is the same as",b,"mm,",c,"cm and",d,"km.")
            elif q=='iv':
                a=float(input("Input in kilometres:"))
                b=a*1000000
                c=a*100000
                d=a*1000
                print(a,"km is the same as",b,"mm,",c,"cm and",d,"m.")
            else:
                print("Invalid Input! Please try again.")
        elif p=='c':
            print("You have chosen Time Converter!")
            print("Choose the unit of the input:")
            print("->  i.Seconds")
            print("->  ii.Minutes")
            print("->  iii.Hours")
            print("->  iv.Days")
            q=(input("Enter your choice(select character from index): "))
            if q=='i':
                a=float(input("Input in seconds:"))
                b=a/60
                c=b/60
                d=c/24
                print(a,"sec/s is the same as",b,"min/s,",c,"hour/s and",d,"day/s.")
            elif q=='ii':
                a=float(input("Input in minutes:"))
                b=a*60
                c=a/60
                d=c/24
                print(a,"min/s is the same as",b,"sec/s,",c,"hour/s and",d,"day/s.")
            elif q=='iii':
                a=float(input("Input in hours:"))
                b=a*3600
                c=a*60
                d=a/24
                print(a,"hour/s is the same as",b,"sec/s,",c,"min/s and",d,"day/s.")
            elif q=='iv':
                a=float(input("Input in days:"))
                b=a*24*3600
                c=a*24*60
                d=a*24
                print(a,"day/s is the same as",b,"sec/s,",c,"min/s and",d,"hour/s.")
            else:
                print("Invalid Input! Please try again.")
        else:
            print("Invalid Input! Please try again.")
    else:
        print("Invalid Input! Please try again.")

    
    
    

          

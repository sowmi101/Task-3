Tamil = int(input("Enter your mark:"))
English = int(input("Enter your mark:"))
Maths = int(input("Enter your mark:"))
Science = int(input("Enter your mark:"))
Social = int(input("Enter your mark:"))
Total = Tamil + English + Maths + Science + Social
Grade ="None"
Max_mark = 500
Marginal_mark = 40
if(Max_mark > Marginal_mark and Total < Max_mark):
       Result = "Pass"
       if(Max_mark > Marginal_mark and Total > 450):
              Grade = "Your grade 'O'";
       elif(Max_mark > Marginal_mark and Total > 400 and Total < 450):
              Grade = "Your grade 'A'";
       elif(Max_mark > Marginal_mark and Total > 350 and Total < 400):
              Grade = "Your grade 'B'";
       elif(Max_mark > Marginal_mark and Total > 300 and Total < 350):
              Grade = "Your grade 'C'"
       else:
              Grade = "Your grade 'D'"
else:
  Result = "Fail"
  Grade = " Your failed"
 
 
print("Your Result:",Result)
print("Your Grade:",Grade)
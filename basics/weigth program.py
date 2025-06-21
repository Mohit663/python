weight=int(input('Enter weight : '))
w_type=str(input('Kgs or Lbs : '))

if w_type=="Kgs":
    print("weight in kgs : ", weight)
    print("weight in Lbs : ", weight*2.2)

elif w_type=="Lbs":
    print("weight in Kgs : ", weight/2.2)
    print("weight in Lbs : ", weight)

else :
    print("enter weight in correct input format!")



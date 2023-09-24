def rotate(nums,k):
    for i in range(k):
        s=nums.pop()
        nums.insert(0,s)

r =3
num =[3,5,2,3,6]
rotate(num,r)
print(num)

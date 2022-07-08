H = int (input("Enter Hour:"))
M = int (input("Enter Min:"))
S = int (input("Enter Sec:"))

H = H * 3600
H = H + (M*60)
H = H + S

print(H ,"seconds have passed since the beginning of the day.")
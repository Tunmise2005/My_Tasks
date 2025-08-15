voter_no1 = input("Enter your name: ")
voter_no2 = input("Enter your name: ")
voter_no3 = input("Enter your name: ")
voter_no4 = input("Enter your name: ")
voter_no5 = input("Enter your name: ")


voters = set()
for voter in [voter_no1, voter_no2, voter_no3, voter_no4, voter_no5]:
    if voter in voters:
        print(f"warming: {voter} has already resistered.")
    else:
        voters.add(voter)
print("\nTotal number of voters:",len(voters))
print("voters list:",",".join(voters))
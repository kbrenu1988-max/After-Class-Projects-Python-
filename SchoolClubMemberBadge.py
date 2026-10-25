name = input("Enter your name: ")
club_name = input("Enter your club: ")
member_number = input("Enter your number: ")
points = input("Enter your points: ")
active = True
badge_code = name[0:2] + name[7:9] + str(member_number)
status = str(active)


print("Name: ", name)
print("Club name: ", club_name)
print("Member number: ", member_number, "type: ", type(member_number))
print("Points: ", points, "type: ", type(points))
print("Active: ", active, "type: ", type(active))
print("Badge code: ", badge_code)

line_1 = "Member: " + name 
line_2 = "Club name: " + club_name
line_3 = "Code: " + badge_code
line_4 = "Points: " + points + " | Active: " + status

print()
print("====== CLUB BADGE ======")
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print("========================")

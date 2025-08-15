seat_number = {x for x in range(1, 51)}
# Seat bookings
seat1 = int(input("Book your seat number"))
seat2 = int(input("Book your seat number"))
seat3 = int(input("Book your seat number"))
seat4 = int(input("Book your seat number"))
seat5 = int(input("Book your seat number"))
user_seat = (seat1, seat2, seat3, seat4, seat5)
# Removing booked seats
seat_number.remove(seat1)
seat_number.remove(seat2)
seat_number.remove(seat3)
seat_number.remove(seat4)
seat_number.remove(seat5)
print(seat_number)
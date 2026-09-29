#1 for dirty and 0 for clean
import random
room_a_status=random.randint(0,1)
room_b_status=random.randint(0,1)
print(f"Initial states of Room A and B = {room_a_status} and {room_b_status} where 0 is clean and 1 is dirty")
score=0
#room_a_status=int(input("Enter the room status of room A (0 for clean and 1 for dirty): "))
#room_b_status=int(input("Enter the room status of room B (0 for clean and 1 for dirty): "))

room_start=input("Enter which room the vacuum cleaner starts in (A or B): ") #A or a for room A and B or b for room B
while room_a_status==1 or room_b_status==1:
    if (room_start not in ['A','a','b','B']):
        print(f"Room {room_start} does not exist")
        break
    if (room_start in ['A','a']):
        if (room_a_status == 1):
            room_a_status = 0 #became clean
            score+=1
            print("Room A is now clean. Moving to Room B")
            room_start = 'B'
        else:
            print(f"Room {room_start} is already clean. Moving to Room B")
            room_start ='B'
    else :
        if (room_b_status == 1):
            room_b_status = 0 #became clean
            score+=1
            print(f"Room {room_start} is now clean. Moving to Room A")
            room_start = 'A'
        else:
            print(f"Room {room_start} is already clean. Moving to Room A")
            room_start = 'A'

print(f"Room A status {room_a_status} and Room B status {room_b_status}")
print("Both Rooms A and B are now clean")
print(f"Score is {score}")
        


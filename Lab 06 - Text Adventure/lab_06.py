# Basic Text Adventure

class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    room = Room("You are standing in a spacious hall, decorated in red and gold, with glittering chandeliers overhead.",
                None, 1, None, 2)
    room_list.append(room)
    room = Room("This room is completely dark.",
                0, None, None, None)
    room_list.append(room)
    room = Room("The walls of this small room were clearly once lined with hooks, though now only one remains.",
                None, None, 0, None)
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_direction = input("What would you like to do? ")
        if user_direction == "North".lower() or user_direction == "N".lower():
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_direction == "South".lower() or user_direction == "S".lower():
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_direction == "East".lower() or user_direction == "E".lower():
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_direction == "West".lower() or user_direction == "W".lower():
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif user_direction == "Q".lower() or user_direction == "Quit".lower():
            print("Goodbye!")
            done = True
        else:
            print('I don\'t understand. Try a direction like "north" or "n"')


if __name__ == "__main__":
    main()
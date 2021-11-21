# Kayla Casper-Dixon
# establish dictionary
rooms = {
    "Old Mine Shaft": {
        "name": "Old Mine Shaft",
        "west": "Graveyard",
        "south": "Hall of Sacrifice",
        "text": "It’s dark and cold.",
        "visited": "TRUE",
        "direction_text": "To the West you can hear soft moans.\n"
                          "To the South you can smell a hint of iron.\n"},
    "Graveyard": {
        "name": "Graveyard",
        "east": "Old Mine Shaft",
        "south": "Witch’s Room",
        "item": "Magic Mirror",
        "visited": "FALSE",
        "text": "You see tombstones and wild weeds all around you.\n"
                "The smell of wet dirt fills your senses.\n"
                "Shadowy figures walk around the place, one turns to you.\n"
                "They point towards an older grave.\n"
                "Laying on the grave is an intricate mirror.",
        "direction_text": "To the East is a cold draft.\n"
                          "To the South is the smell of spices and herbs.\n"},
    "Witch’s Room": {
        "name": "Witch’s Room",
        "east": "Witch’s Hut",
        "south": "Garden of Memories",
        "item": "Talisman",
        "visited": "FALSE",
        "text": "You walk into a small room. In the center a pot boils with a bubbling green goo.\n"
                "Herbs and bones hang from the ceiling.\n"
                "Near the small stack of cloth in the corner you see a small talisman.",
        "direction_text": "To the South you can smell the strong scent of dirt and flowers.\n"
                          "To the North you can hear soft moans.\n"
                          "To the East you can feel a warm breeze and hear the sound of clicking.\n"},
    "Garden of Memories": {
        "name": "Garden of Memories",
        "east": "Stone Cavern",
        "north": "Witch’s Room",
        "item": "Hydrangea",
        "visited": "FALSE",
        "text": "You walk into an overrun garden surrounded by high jagged stone walls.\n"
                "Above you the full moon shines brightly.\n"
                "The smell of flowers surrounds you.\n"
                "You see a small brilliantly blue flower glowing in the moonlight.",
                "direction_text": "To the East you can hear the wind blowing.\n"
                "To the North is the smell of spices and herbs.\n"},
    "Stone Cavern": {
        "name": "Stone Cavern",
        "east": "Wishing Well",
        "north": "Witch’s Hut",
        "west": "Garden of Memories",
        "item": "Black Salt",
        "visited": "FALSE",
        "text": "The walls are made of stone and in the light you can see the shimmer of gems.\n"
                "Laying in a corner within a circle scratched into the ground sits a skeletal figure.\n"
                "In the decayed hand sits a small bowl of black salt.",
        "direction_text": "To the East you can hear running water.\n"
                          "To the North you can feel a warm breeze and hear the sound of clicking.\n"
                          "To the West you can smell the strong scent of dirt and flowers.\n"},
    "Wishing Well": {
        "name": "Wishing Well",
        "west": "Stone Cavern",
        "item": "Fairy Water",
        "visited": "FALSE",
        "text": "Water rushes through the room.\n"
                "Little lights shimmer and float by slowly.\n"
                "One light comes closer and dance slowly around a glass vile.",
        "direction_text": "To the West you can hear the wind blowing."},
    "Hall of Sacrifice": {
        "name": "Hall of Sacrifice",
        "west": "Witch’s Hut",
        "north": "Old Mine Shaft",
        "item": "Bone Knife",
        "visited": "FALSE",
        "text": "You find yourself inside of a dimly lite hall.\n"
                "In the center is a stone slab.\n"
                "As you get closer you can see the dark red stained into the stone.\n"
                "A sharpened bone lies on the edge.",
        "direction_text": "To the West you can feel a warm breeze and hear the sound of clicking.\n"
                          "To the North is a cold draft."},
    "Witch’s Hut": {
        "name": "Witch’s Hut",
        "east": "Witch’s Room",
        "south": "Stone Cavern",
        "west": "Hall of Sacrifice",
        "visited": "FALSE",
        "text":  "The heat hits you quickly.\n"
                 "There in the center of the room stands a black shadowy figure."}
        }


print("*****************************************************************************************\n"
      "**        *      *******        ********                   *            *              **\n"
      "**       * *        *           *       *                 * *           *              **\n"
      "**      *    *      *    *      ********     ********    *   *          *              **\n"
      "**        *         *   * *     *   *        *          *******   *     *              **\n"
      "**          *       *  *   *    *     *      *         *       *  *     ********       **\n"
      "**      *    *        *******   *       *    ******   *         * *                    **\n"
      "**        * *        *       *               *                    *                    **\n"
      "**         *        *         *              *                    *                    **\n"
      "**                                           *                    ********             **\n"
      "*****************************************************************************************")

# creating list for player items and directions.
player_items = []
direction = ["north", "south", "east", "west"]
current_room = rooms["Old Mine Shaft"]
print("Type the directions north, south, east, and west to navigate. Type exit to leave game.\n"
      "Type item's name to collect item.\n"
      "Find the items needed to protect yourself and defeat the witch.")

# function to move between rooms


def move():
    global current_room
    if user_direction in current_room:
        current_room = rooms[current_room[user_direction]]
        print("You are in the {}".format(current_room["name"]), "\n")
        return current_room

# function to update the player inventory


def get_item(player_inv):
    inventory = player_inv
    print(current_room["text"], "\n")
    current_room.update({"visited": "TRUE"})
    item_take = input("Would you like to take this {} ?\n".format(current_room["item"]))
    while item_take != current_room["item"]:
        if item_take != current_room["item"]:
            print("That item is not here.")
            item_take = input("\nWould you like to take this {} ?\n".format(current_room["item"]))
    inventory.append(current_room["item"])
    print("You place the {} in your bag.\n".format(current_room["item"]))
    return inventory


# print current room
print("You are in the", current_room["name"], "\n")
print(current_room["text"], "\n",
      current_room["direction_text"], "\n")

# start a loop that will only end when player inputs 'quit'
while True:
    # establishing if the room is the witch's hut
    if current_room["name"] == "Witch’s Hut":
        print(current_room["text"])
        # bad ending
        if len(player_items) < 6:
            print("The heat vanishes and the shadow rushes towards you.\n"
                  "The sound of laughter fill your ears as everything goes dark\n"
                  "YOU LOSE!")
            break
        # good ending
        elif len(player_items) == 6:
            print("The shadow creeps closer. The items in your pack begin to glow.\n"
                  "A shrek fills your ears as the shadows bursts into light.\n"
                  "On the other side of the room is a small doorway.\n"
                  "You open the door and find yourself outside your front door.\n"
                  "YOU WIN!")
            break
    # creating the game if else statements
    elif current_room["name"] != "Witch's Hut":
        user_direction = input("Which way would you like to go?\n")
        if user_direction == "exit":
            break
        elif user_direction in direction:
            # go to move function
            move()
            if "item" in current_room:
                # if elif statement to check if player has been in the room
                if current_room["visited"] == "FALSE":
                    # go to get item function
                    player_items = get_item(player_inv=player_items)
                    print("You have:", player_items)
                    print(current_room["direction_text"])
                elif current_room["visited"] == "TRUE":
                    print("You've been here before.\n",
                          current_room["direction_text"])
            # elif statement that takes care of items less rooms
            elif "item" not in current_room:
                if current_room["visited"] == "TRUE":
                    print("You've been here before.\n",
                          current_room["direction_text"])
        # statement for user input error for direction
        elif user_direction != current_room:
            print("Direction not found. Try again.")

print("Thanks for playing!")

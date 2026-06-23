def add_Mission():
    mission = input("Add a Mission: ")

    if mission.strip() == "":
        print("Empty mission cannot be added")
        return

    with open("missions.txt", "a", encoding="utf-8") as file:
        file.write(mission + " | STATUS: WAITING\n")

    print("Mission Added Successfully")


def list_Mission():
    try:
        with open("missions.txt", "r", encoding="utf-8") as file:
            print("\n===== MISSIONS =====")

            for line in file:
                print(f"Mission: {line.strip()}")

    except FileNotFoundError:
        print("File not found. No missions yet.")


def complete_mission():
    try:
        with open("missions.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("\n===== MISSION LIST =====")

        for i, line in enumerate(lines, 1):
            print(f"{i} - {line.strip()}")

        choice = int(input("\nWhich mission is completed? "))

        if 1 <= choice <= len(lines):
            lines[choice - 1] = lines[choice - 1].replace(
                "WAITING",
                "COMPLETED"
            )

            with open("missions.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)

            print("Mission marked as completed")

        else:
            print("Invalid selection")

    except FileNotFoundError:
        print("No missions found")


def exit_program():
    print("Exiting The Program")
    return


while True:

    print("\n" + "=" * 30)
    print("      TASK MANAGER")
    print("=" * 30)

    print("1 - Add Mission")
    print("2 - List Missions")
    print("3 - Complete Mission")
    print("4 - Exit")

    actions = {
        "1": add_Mission,
        "2": list_Mission,
        "3": complete_mission,
        "4": exit_program
    }

    choice = input("\nChoice Process: ")

    if choice in actions:
        actions[choice]()

        if choice == "4":
            break

    else:
        print("Invalid Choice")
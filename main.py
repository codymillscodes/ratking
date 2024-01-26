import sys
import commands as c


def main():
    print("ACCESSING MAINFRAME...")
    c.init_save()
    while True:
        command = input("> ")

        if command.startswith("qa"):
            cal = " ".join(command.split()[1:])
            print(c.quick_ammo(cal))
        elif command.startswith("a"):
            cal = " ".join(command.split()[1:])
            c.search_ammo(cal)
        elif command.startswith("u"):
            field = " ".join(command.split()[1:])
            c.update(field)
        elif command.startswith("quit"):
            sys.exit()
        elif command.startswith("i"):
            item = " ".join(command.split()[1:])
            c.search_items(item)
        elif command.startswith("help"):
            print("i - items\na - ammo\nqa - ammo cheatsheet\nu - update")
        elif command.startswith("tc"):
            task = " ".join(command.split()[1:])
            c.complete_task(task)
        elif command.startswith("cs"):
            command = command.split()[1:]
            level = int(command[-1:][0])
            command.pop()
            station = " ".join(command)
            c.complete_station(station, level)
        elif command.startswith("ta"):
            task = " ".join(command.split()[1:])
            c.add_task(task)
        elif command.startswith("ni"):
            c.needed_items()

        else:
            print("Unknown command.")


main()

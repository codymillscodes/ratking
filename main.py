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
            c.write_save()
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
            maps = None
            if len(command.split()) > 2:
                maps = command.split()[-1:][0]
                command.split()[1:].pop()
            q = " ".join(command.split()[1:])
            c.needed_items(q, maps)
        elif command.startswith("save"):
            c.write_save()
        elif command.startswith("fcat"):
            cat = " ".join(command.split()[1:])
            c.flea_cat(cat)
        else:
            print("Unknown command.")


main()

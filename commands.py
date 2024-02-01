import os
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json
import gquery
import misc

global active_save
active_save = {}


def update_ammo():
    print("updating ammo")
    with open("db/items.json") as f:
        items = json.load(f)

    ammo = {"ammo": []}
    for i in items["items"]:
        if i["category"]["name"] == "Ammo":
            ammo["ammo"].append(i)

    if ammo["ammo"]:
        with open("db/ammo.json", "w") as f:
            json.dump(ammo, f)


def update(field="all"):
    query = gquery.update(field)
    transport = AIOHTTPTransport(url="https://api.tarkov.dev/graphql")
    client = Client(transport=transport, fetch_schema_from_transport=True)
    if query:
        if field == "all":
            for q in query:
                result = client.execute(gql(query[q]))
                # boss_json = json.loads(result)
                print(f"updating {q}")
                with open(f"db/{q}.json", "w") as f:
                    json.dump(result, f)

                if q == "items":
                    update_ammo()

        else:
            result = client.execute(gql(query))
            print(f"updating {field}")
            with open(f"db/{field}.json", "w") as f:
                json.dump(result, f)

            if field == "items":
                update_ammo()

        return "update complete."
    return "Valid things to update are all, barters, bosses, crafts, flea, hideout, items, maps, tasks, traders."


def search_ammo(caliber):
    caliber = f"Caliber{caliber}"
    if caliber in misc.calibers:
        with open("db/ammo.json") as f:
            ammo = json.load(f)
        for a in ammo["ammo"]:
            if caliber in a["properties"]["caliber"]:
                print(
                    f"{a['name']}, {a['properties']['penetrationPower']} pen, {a['properties']['damage']} damage, {a['properties']['armorDamage']} a-dam, {a['properties']['fragmentationChance']} frag"
                )

    else:
        print(f"Wrong caliber: {misc.calibers}")


def quick_ammo(caliber):
    for a in misc.ammo_cheatsheet:
        if caliber in a["cal"]:
            return a["tiers"]

    return f"Couldn't find. Try: {misc.cs_cals}"


def search_items(item):
    with open("db/items.json") as f:
        items = json.load(f)

    for i in items["items"]:
        if item.lower() in i["name"].lower():
            print(f"Name: {i['name']} | Cat: {i['category']['name']}")
            sell_for = {}
            for s in i["sellFor"]:
                sell_for[s["vendor"]["name"]] = s["price"]
            print(f"Sell for: {sell_for}")
            if i["craftsFor"] or i["craftsUsing"]:
                craft_str = f"Crafts: {len(i['craftsFor']) + len(i['craftsUsing'])}"
            else:
                craft_str = "Crafts: 0"

            if i["bartersFor"] or i["bartersUsing"]:
                barter_str = f"Barters: {len(i['bartersFor']) + len(i['bartersUsing'])}"
            else:
                barter_str = "Barters: 0"

            print(f"{craft_str} | {barter_str}")
            print(f"t.dev Link: {i['link']}")


def complete_task(task):
    global active_save
    with open("db/tasks.json") as f:
        tasks = json.load(f)
    for t in tasks["tasks"]:
        if t["name"].lower() == task:
            task_id = t["id"]
            print("Found task.")
            break
    if task_id:
        active_save["tasks_complete"].append(task_id)
        print(f"Added {task} with id: {task_id}")
        active_save["tasks_active"].remove(task_id)
        write_save(active_save)
    else:
        print("Couldnt find task. Typo?")


def complete_station(station, level):
    global active_save
    active_save["hideout"][station] = level
    print(f"{station} set to level {active_save['hideout'][station]}")
    write_save(active_save)


def add_task(task):
    global active_save
    with open("db/tasks.json") as f:
        tasks = json.load(f)
    for t in tasks["tasks"]:
        if t["name"].lower() == task:
            task_id = t["id"]
            print("Found task.")
            break
    if task_id:
        active_save["tasks_active"].append(task_id)
        print(f"Added {task} with id: {task_id}")
        write_save(active_save)
    else:
        print("Couldnt find task. Typo?")


def needed_items(q, maps=None):
    global active_save
    with open("db/tasks.json") as f:
        tasks = json.load(f)
    with open("db/hideout.json") as f:
        hideout = json.load(f)
    if q == "t" or q == "":
        for a in active_save["tasks_active"]:
            for t in tasks["tasks"]:
                if t["id"] == a:
                    task_map = "Any"
                    if t["map"]:
                        task_map = t["map"]["name"]
                    if maps and maps in task_map.lower():
                        print(
                            f"\n{t['name'].upper()}\nGiver: {t['trader']['name']} | Map: {task_map}\n"
                        )
                        for ob in t["objectives"]:
                            print(ob["description"])
                    else:
                        print(
                            f"\n{t['name'].upper()}\nGiver: {t['trader']['name']} | Map: {task_map}\n"
                        )
                        for ob in t["objectives"]:
                            print(ob["description"])

                        print("---")

    if q == "h" or q == "":
        for h in active_save["hideout"]:
            for o in hideout["hideoutStations"]:
                if h == o["name"].lower():
                    for l in o["levels"]:
                        if l["level"] == active_save["hideout"][h] + 1:
                            print(f'\n[{h.upper()}] {l["level"]}')
                            for i in l["itemRequirements"]:
                                print(i["count"], i["item"]["name"])

                            print("---")


def flea_cat(c):
    cats = [
        "gun",
        "wearable",
        "ammobox",
        "keys",
        "ammo",
        "grenade",
        "mods",
        "provisions",
        "armor",
        "rig",
        "backpack",
        "meds",
        "injectors",
        "barter",
        "glasses",
        "helmet",
        "container",
        "armorplate",
        "preset",
    ]
    if c.lower() not in cats:
        print("Not a correct category. Try: ", cats)
    else:
        with open("db/items.json") as f:
            items = json.load(f)

        # Create an empty dictionary to store the items and their prices
        item_dict = {}
        for i in items["items"]:
            if c in i["types"] and "noFlea" not in i["types"]:
                for t in i["sellFor"]:
                    if t["vendor"]["name"] == "Flea Market":
                        # Add the item name and priceRUB to the dictionary
                        item_dict[i["name"]] = t["priceRUB"]

        # Sort the dictionary by value in descending order and store the result in a list of tuples
        sorted_items = sorted(item_dict.items(), key=lambda x: x[1], reverse=False)
        # Loop over the sorted_items list and print the item name and priceRUB from each tuple
        for item, price in sorted_items:
            print(f"{item} [{price}]")


def init_save():
    global active_save
    if not os.path.isfile("save.json"):
        print("CREATING ROOT USER.")
        save = {
            "level": 1,
            "traders": {
                "prapor": 1,
                "therapist": 1,
                "fence": 1,
                "skier": 1,
                "peacekeeper": 1,
                "mechanic": 1,
                "ragman": 1,
                "jaeger": 1,
            },
            "tasks_complete": [],
            "tasks_active": [],
            "hideout": {
                "air filtering unit": 0,
                "bitcoin farm": 0,
                "booze generator": 0,
                "defective wall": 0,
                "generator": 0,
                "gym": 0,
                "hall of fame": 0,
                "heating": 0,
                "illumination": 0,
                "intelligence center": 0,
                "lavatory": 0,
                "library": 0,
                "medstation": 0,
                "nutrition unit": 0,
                "rest space": 0,
                "scav case": 0,
                "security": 0,
                "shooting range": 0,
                "solar power": 0,
                "stash": 0,
                "vents": 0,
                "water collector": 0,
                "weapon rack": 0,
                "workbench": 0,
                "christmas tree": 0,
            },
        }
        with open("save.json", "w") as f:
            json.dump(save, f)
        print("SUPERUSER CREATED.")
        active_save = save
    else:
        print("LOGGED IN.")
        with open("save.json") as f:
            save = json.load(f)
        active_save = save


def write_save(save=None):
    if not save:
        global active_save
        save = active_save
    with open("save.json", "w") as f:
        json.dump(save, f)

    print("Home dir backed up.")

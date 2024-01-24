import sys
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import json
import gquery

_calibers = [
    "Caliber556x45NATO",
    "Caliber12g",
    "Caliber762x54R",
    "Caliber762x39",
    "Caliber40mmRU",
    "Caliber9x19PARA",
    "Caliber545x39",
    "Caliber762x25TT",
    "Caliber9x18PM",
    "Caliber9x39",
    "Caliber762x51",
    "Caliber366TKM",
    "Caliber9x21",
    "Caliber20g",
    "Caliber46x30",
    "Caliber127x55",
    "Caliber57x28",
    "Caliber1143x23ACP",
    "Caliber23x75",
    "Caliber40x46",
    "Caliber762x35",
    "Caliber86x70",
    "Caliber9x33R",
    "Caliber26x75",
    "Caliber68x51",
]

ammo_cheatsheet = [
    {
        "cal": "12x70",
        "tiers": {"budget": "Magnum Buckshot", "mid": "Flechette", "best": "AP-20"},
    },
    {
        "cal": "20x70",
        "tiers": {"budget": "7.5mm Buckshot", "mid": "Poleva-6u", "best": "Star"},
    },
    {
        "cal": "23x75",
        "tiers": {"budget": "Sharpnel-10", "mid": None, "best": "Barrikada"},
    },
    {
        "cal": "9x18",
        "tiers": {"budget": "PSO gzh", "mid": "PST gzh", "best": "PBM gzh"},
    },
    {"cal": "762x25", "tiers": {"budget": "AKBS", "mid": "PT gzh", "best": "PST gzh"}},
    {
        "cal": "9x19",
        "tiers": {"budget": "PST gzh", "mid": "AP 6.3", "best": "PBP gzh (73N1)"},
    },
    {"cal": "9x33R", "tiers": {"budget": None, "mid": None, "best": "Magnum FMJ"}},
    {
        "cal": "1143x23ACP",
        "tiers": {"budget": "Match FMJ", "mid": None, "best": "ACP (AP)"},
    },
    {"cal": "9x21", "tiers": {"budget": "P gzh", "mid": "PS gzh", "best": "BT gzh"}},
    {"cal": "57x28", "tiers": {"budget": "SS197SR", "mid": None, "best": "190SS190"}},
    {"cal": "46x30", "tiers": {"budget": "JSP SX", "mid": None, "best": "AP SX"}},
    {"cal": "9x39", "tiers": {"budget": "5SP5", "mid": "SPP", "best": "6SP6"}},
    {"cal": "366TKM", "tiers": {"budget": "EKO", "mid": None, "best": "AP"}},
    {"cal": "545x39", "tiers": {"budget": "PP", "mid": "BT", "best": "BP"}},
    {"cal": "556x45", "tiers": {"budget": "M855", "mid": "M855A1", "best": "M995"}},
    {"cal": "68x51", "tiers": {"budget": "SIG FMJ", "mid": None, "best": "SIG Hybrid"}},
    {"cal": "762x35", "tiers": {"budget": "BCP FMJ", "mid": "M62", "best": "AP"}},
    {"cal": "762x39", "tiers": {"budget": "PS", "mid": "PP", "best": "BP"}},
    {"cal": "762x51", "tiers": {"budget": "M80", "mid": "M62", "best": "M61"}},
    {"cal": "762x54R", "tiers": {"budget": "LPS", "mid": "PS", "best": "SNB"}},
    {"cal": "86x70", "tiers": {"budget": "FMJ", "mid": None, "best": "AP"}},
    {"cal": "127x55", "tiers": {"budget": "PS12", "mid": None, "best": "PS12B"}},
]


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


def update_all():
    with open("items.json") as f:
        items = json.load(f)

    ammo = {"ammo": []}
    print("updating ammo")
    for i in items["items"]:
        if i["category"]["name"] == "Ammo":
            ammo["ammo"].append(i)

    if ammo["ammo"]:
        with open("ammo.json", "w") as f:
            json.dump(ammo, f)

    else:
        print("uhhhh")


def search_ammo(caliber):
    caliber = f"Caliber{caliber}"
    if caliber in _calibers:
        with open("ammo.json") as f:
            ammo = json.load(f)
        for a in ammo["ammo"]:
            if caliber in a["properties"]["caliber"]:
                print(
                    f"{a['name']}, {a['properties']['penetrationPower']} pen, {a['properties']['damage']} damage, {a['properties']['armorDamage']} a-dam, {a['properties']['fragmentationChance']} frag"
                )

    else:
        print(f"Wrong caliber: {_calibers}")


def quick_ammo(caliber):
    for a in ammo_cheatsheet:
        if caliber in a["cal"]:
            return a["tiers"]

    cs_cals = [
        "12x70",
        "20x70",
        "23x75",
        "9x18",
        "762x25",
        "9x19",
        "9x33R",
        "1143x23ACP",
        "9x21",
        "57x28",
        "46x30",
        "9x39",
        "366TKM",
        "545x39",
        "556x45",
        "68x51",
        "762x35",
        "762x39",
        "762x51",
        "762x54R",
        "86x70",
        "127x55",
    ]

    return f"Couldn't find. Try: {cs_cals}"


def search_items(item):
    with open("items.json") as f:
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


# search_items("soap")
# quick_ammo("poop")
# search_ammo("12g")
# update_all()


def main():
    print("ACCESSING MAINFRAME...")
    print("LOGGED IN.")
    while True:
        command = input("> ")

        if command.startswith("aq"):
            cal = " ".join(command.split()[1:])
            print(quick_ammo(cal))
        elif command.startswith("a"):
            cal = " ".join(command.split()[1:])
            search_ammo(cal)
        elif command.startswith("u"):
            field = " ".join(command.split()[1:])
            update(field)
        elif command.startswith("quit"):
            sys.exit()
        elif command.startswith("i"):
            item = " ".join(command.split()[1:])
            search_items(item)
        elif command.startswith("help"):
            print("i - items\na - ammo\naq - ammo cheatsheet\nu - update")
        else:
            print("Unknown command.")


main()

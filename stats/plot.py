import matplotlib.pyplot as plt
import json


pokemon = 'Slurpuff'
attrib = 'Items'

# Ignore attrib, just plot usage
usage = True
file = "output/" + pokemon + attrib + '.json'
keys = ['choicescarf', 'choicespecs', 'leftovers']
colors = ['k', 'r', 'b', 'g', 'y', 'm', 'c']

with open(file) as f:
    data = json.load(f)

    # print(json.dumps(data, indent=2))

    # Remove null values. This is a problem for pokemons released after the
    # release of the game.
    data = [x for x in data if x]
    if not usage:
        for key in keys:
            data = [x for x in data if key in x['top']]
    for i in data:
        i['date'] = i['date'].split(',')[0]
    # Plot the data
    if usage:
        plt.plot([x['date'] for x in data], [x['usage'] for x in data], colors.pop())
        keys = [pokemon]
    else:
        for i, key in enumerate(keys):
            plt.plot([x['date'] for x in data], [x['top'][key] for x in data], colors[i], label=key)
    # Show only every 8th label
    plt.xticks([x['date'] for x in data][::4], rotation=90)
    # Show legend
    plt.legend(keys)
    plt.grid(zorder=0)
    plt.show()

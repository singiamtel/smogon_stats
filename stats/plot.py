import matplotlib.pyplot as plt
import json


pokemon = 'Yveltal'
file = "output/" + pokemon + 'Moves.json'
moves = ['roost', 'darkpulse']
colors = ['k', 'r', 'b', 'g', 'y', 'm', 'c']

# The data looks like this:
# {
#   "date": "11/1/2016, 1:00:00 AM",
#   "top": {
#     "lastresort": 100,
#     "batonpass": 100,
#     "protect": 73.9304011969732,
#     "quickattack": 73.93039009995931,
#     "": 40.323845945704434
#   },
#   "rawCount": 764
# },
# {
#   "date": "2/1/2017, 1:00:00 AM",
#   "top": {
#     "lastresort": 99.08065125329215,
#     "batonpass": 96.61787000786981,
#     "protect": 34.427422967270566,
#     "substitute": 27.599990369659587,
#     "": 24.89576712629149
#   },
#   "rawCount": 46333
# },

with open(file) as f:
    data = json.load(f)

    # Drop the entries with no data
    # for x in data:
    #     print(x['top'])
    for move in moves:
        data = [x for x in data if move in x['top']]
    # print(data)
    for i in data:
        i['date'] = i['date'].split(',')[0]
    # Plot the data
    for i, move in enumerate(moves):
        plt.plot([x['date'] for x in data], [x['top'][move] for x in data], colors[i], label=move)
    # plt.plot([x['date'] for x in data], [x['top'][move] for x in data], color="g")
    # plt.plot([x['date'] for x in data], [x['top'][move2] for x in data], color="k")
    # Show only every 8th label
    plt.xticks([x['date'] for x in data][::6], rotation=90)
    # Show legend
    plt.legend(moves)
    plt.grid(zorder=0)
    plt.show()

const fs = require('fs').promises;

const dir = "1760/"
const pokemon = process.argv[2] || "Zygarde";
const outdir = "output/"
const key = "Items"

function getTopValues(obj, topN)
{
    const sortedEntries = Object.entries(obj).sort(function(a,b){return b[1]-a[1]});
	if (sortedEntries.length < topN) {
		return Object.fromEntries(sortedEntries)
	}
    const last = sortedEntries[topN-1][1];
    const result = sortedEntries.filter(function(entry){
        return entry[1] >= last;
    });
    return Object.fromEntries(result)
}

const getDataPoint = async function(pokemon, topN, key, file) {
	const rawdata = await fs.readFile(file);
	const json = JSON.parse(rawdata);
	dict = json.data[pokemon]?.[key];
	if(!dict) {
		console.log("File " + file + " does not contain data for " + pokemon + " or " + key + " is not a valid key.");
		return;
	}
	const abilitiesSum = Object.values(json.data[pokemon].Abilities).reduce((a, b) => a + b, 0);
	for(let i in dict){
		dict[i] = dict[i]/abilitiesSum * 100
	}
	console.log("<" + pokemon + "> Finished processing " + file);
	return {
		"date": new Date(file.split("/")[1].split(":")[0].substring(0,7)).toLocaleString(),
		"top": getTopValues(dict, topN),
		"usage": json.data[pokemon]["usage"] * 100
	}
}

const main = async () => {
	// console.log(await getDataPoint("Zygarde", 5, "Moves", dir + "/2022-09:gen7anythinggoes-" + dir + ".json"));
	const dirs = await fs.readdir(dir)
	const promises = dirs.map(async (file) => {
		return getDataPoint(pokemon, 10, key, dir + file).then(function(result) {
			return result;
		});
	});
	const results = await Promise.all(promises);
	fs.writeFile(outdir + pokemon + key + ".json", JSON.stringify(results));
}

main()

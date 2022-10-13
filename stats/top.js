const fs = require("fs")

const top = process.argv[2] || 10
const rawdata = fs.readFileSync("1760/2022-09:gen8anythinggoes-1760.json");
const json = JSON.parse(rawdata);

const arr = []
for (let i in json.data){
	arr.push([i, json.data[i]["usage"]])
}
arr.sort(function(a,b){return b[1]-a[1]});
const res = arr.slice(0, top).map(e => e[0])
// const res = arr.slice(0, top)
for(let i of res){
	console.log(i)
}

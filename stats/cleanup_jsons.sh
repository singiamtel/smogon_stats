for i in $(ls output/ -1 | grep -E ".json$"); do
	jq . output/$i | sponge output/$i && echo output/$i
done

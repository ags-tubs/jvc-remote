rm -f tmp_list_convert
IFS=$'\n'
cat README.md | while read -r line; do
    if [[ $line == "|cmd type|setting|value|bitfield|cam response|topic|value-representation|" && $line != 0 ]]
    then
        break
    else
        echo "$line"
    fi
done > tmp_list_convert

echo "|cmd type|setting|value|bitfield|cam response|topic|value-representation|">> tmp_list_convert
echo "|--------|-------|-----|--------|------------|-----|--------------------|">> tmp_list_convert
cat cmds.csv | sed -r 's/,/\|/g' | sed -r 's/^/\|/g' | sed -r 's/$/\|/g' >> tmp_list_convert
cat tmp_list_convert

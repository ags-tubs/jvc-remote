IFS=$'\n'
cat README.md | while read -r line; do
    if [[ $line == "|cmd type|setting|value|bitfield|cam response|topic|value-representation|" ]]; then
        break
    else
        echo "$line"
    fi
done
cat << EOF
|cmd type|setting|value|bitfield|cam response|topic|value-representation|
|--------|-------|-----|--------|------------|-----|--------------------|
EOF
cat cmds.csv | sed -r 's/,/\|/g' | sed -r 's/^/\|/g' | sed -r 's/$/\|/g'

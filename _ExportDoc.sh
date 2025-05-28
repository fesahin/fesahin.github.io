 #!/bin/bash
inpDir="/Users/fsahin/Desktop/test3/"

python3 preprocessMD.py "$inpDir"

inpDir+="/_output"

# pandoc -s $(cat includes.txt) -o index1.pdf 
pandoc "--from=markdown+rebase_relative_paths" --number-sections -F pandoc-crossref -s "$inpDir"/*.md -o index1.pdf 
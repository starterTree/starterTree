[[ $1 == "" ]] && { echo need version as '$1' ; exit 1 ; }
sed -i "s/version is.*hash/version is $(git rev-parse HEAD) hash/g" starterTree.py
sed -i "s/version is version/$1/g" starterTree.py
version is version
rm -rf ~/build/*
cxfreeze -c starterTree.py --target-dir ~/build/starterTree
cd ~/build/ && tar -zcvf starterTree.tar.gz starterTree && cd -
sed -i "s/version is.*hash/version is git rev-parse HEAD hash/g" starterTree.py
sed -i "s/$1/version is version/g" starterTree.py

sed -i "s/version is.*hash/version is $(git rev-parse HEAD) hash/g" starterTree.py
rm -rf ~/build/*
cxfreeze -c starterTree.py --target-dir ~/build/starterTree
cd ~/build/ && tar -zcvf starterTree.tar.gz starterTree && cd -
sed -i "s/version is.*hash/version is git rev-parse HEAD hash/g" starterTree.py

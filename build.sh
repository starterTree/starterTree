[[ $1 == "" ]] && { echo need version as '$1' ; exit 1 ; }
sed -i "s/version is.*hash/version is $(git rev-parse HEAD) hash/g" starterTree.py
sed -i "s/version is version/$1/g" starterTree.py
rm -rf ~/build/*
cxfreeze -c starterTree.py --target-dir ~/build/starterTree
cd ~/build/ && tar -zcvf starterTree.tar.gz starterTree && cd -
ln -sf ~/build/starterTree/starterTree ~/.local/bin/st-build
sed -i "s/version is.*hash/version is git rev-parse HEAD hash/g" starterTree.py
sed -i "s/$1/version is version/g" starterTree.py



# 4,5M	/home/throc/build/starterTree/lib/libpython3.6m.so
# 4,5M	/home/throc/build/starterTree/lib/libpython3.6m.so.1.0
# 1,1M	/home/throc/build/starterTree/lib/library.zip
# 1,4M	/home/throc/build/starterTree/lib/prompt_toolkit
# 3,1M	/home/throc/build/starterTree/lib/pygments


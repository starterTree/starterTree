nameScript=starterTree.py
nameBinary=st
[[ $1 == "" ]] && { echo need version as '$1' ; exit 1 ; }
sed -i "s/version is.*hash/version is $(git rev-parse HEAD) hash/g" $nameScript
sed -i "s/version is version/$1/g" $nameScript
mkdir -p ./build
rm -rf ./build/*
cxfreeze -c $nameScript --target-dir ./build/$nameBinary
cd ./build/ && tar -zcvf $nameBinary.tar.gz $nameBinary && cd -
ln -sf ./build/$nameBinary/$nameBinary ~/.local/bin/$nameBinary
sed -i "s/version is.*hash/version is git rev-parse HEAD hash/g" $nameScript
sed -i "s/$1/version is version/g" $nameScript





# 4,5M	/home/throc/build/starterTree/lib/libpython3.6m.so
# 4,5M	/home/throc/build/starterTree/lib/libpython3.6m.so.1.0
# 1,1M	/home/throc/build/starterTree/lib/library.zip
# 1,4M	/home/throc/build/starterTree/lib/prompt_toolkit
# 3,1M	/home/throc/build/starterTree/lib/pygments


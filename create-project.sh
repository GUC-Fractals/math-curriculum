#!/usr/bin/bash 

echo "Enter Project name: "
read file_name

mkdir -p $file_name/{src,out}
cp ./temp/build ./$file_name/
cp ./temp/temp.tex ./$file_name/src/
cd $file_name/src
mv temp.tex $file_name.tex
#!/bin/sh
cd myJavaBase
git pull origin master
git add .
git commit -m "update"
git push origin master

cd ..
cd myPythonBase
git pull origin master
git add .
git commit -m "update"
git push origin master

cd ..
cd myShellBase
git pull origin master
git add .
git commit -m "update"
git push origin master

exit 0

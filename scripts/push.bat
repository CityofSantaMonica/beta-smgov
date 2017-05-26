@echo off
ECHO GIT CHECKOUT MASTER
git checkout master
ECHO GIT FETCH
git fetch
ECHO GIT PULL
git pull
ECHO GIT SUBMODULE UPDATE
git submodule update
ECHO GIT ADD
git add --all .
ECHO COMMIT -M "Deploy content"
git commit -m "Deploy content"
ECHO GIT PUSH
git push origin master
exit

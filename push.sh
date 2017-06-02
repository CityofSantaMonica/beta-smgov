git config --local user.name "deploy"
git config --local user.email deploy@smgov.net
git checkout master
git fetch
git pull
git add --all .
git commit -m "Deploy content"
git push origin master

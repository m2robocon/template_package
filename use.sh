#!/bin/bash

set -euxo pipefail

if [[ -z $1 ]]; then
	echo "Usage: ./use.sh <repo name>"
	exit 1
fi

: Using name $1

git init
git add -A

git ls-files | xargs sed -i "s/template_package/$1/"

git remote add origin git@github.com:m2robocon/$1
git commit -am "Initial commit"
git push -u origin master

rm use.sh

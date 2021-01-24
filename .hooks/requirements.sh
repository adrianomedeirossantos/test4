#! /bin/sh
pipenv lock -r | sort > src/requirements.txt
pipenv lock --dev -r | sort > tests/requirements.txt
git add src/requirements.txt tests/requirements.txt

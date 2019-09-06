find /Volumes/CARD10/apps/berlin_uhr/ -name "*.py" -exec rm -v {} \;
find ./ -name '*.py' ! -name '*test.py' -exec cp -prv {} /Volumes/CARD10/apps/berlin_uhr/ \;

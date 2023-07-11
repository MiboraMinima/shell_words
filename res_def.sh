#!/bin/bash

password="112358"

if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
    echo "$password" | sudo -S date -s "$(wget --method=HEAD -qSO- --max-redirect=0 google.com 2>&1 | sed -n 's/^ *Date: *//p')" > /dev/null
else
    echo "No internet connection."
fi

dt=$(date)

echo -e "----- $dt\n" >> './result/res_def.txt'
cat './result/def.txt' >> './result/res_def.txt'


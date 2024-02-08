#!/bin/bash

dt=$(date)

echo -e "----- $dt\n" >> './result/res_def.txt'
cat './result/def.txt' >> './result/res_def.txt'

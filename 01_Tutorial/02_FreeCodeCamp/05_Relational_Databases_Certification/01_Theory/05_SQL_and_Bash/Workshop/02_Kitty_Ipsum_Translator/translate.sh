#!/bin/bash
cat $1 | sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'

# 2026.11.02 20:14
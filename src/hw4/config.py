global the, Help, Seed
the = {
    'dump': False,
     'go': 'data',
    'help': False,
    'seed': 937162211,
    'file' : '../../etc/data/repgrid1.csv',
    'p' : '2',
    }

help=""""   
grid.lua : a rep grid processor
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE: grid.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../etc/data/repgrid1.csv
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
ACTIONS:
"""
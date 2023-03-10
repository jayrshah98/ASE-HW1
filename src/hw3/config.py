global the, Help, Seed

the = {
    'dump': False,
    'file' : '../../etc/data/auto93.csv',
    'far' : .95,
    'go' : 'data',
    'help' : 'false',
    'min' : .5,
    'p' : 2,
    'seed': 937162211,
    'Sample' : 512

}
help = """"
cluster.lua : an example csv reader script
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE: cluster.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = ../../etc/data/auto93.csv
  -F  --Far     distance to "faraway"  = 0.95
  -g  --go      start-up action        = data
  -h  --help    show help              = false
  -m  --min     stop clusters at N^min = 0.5
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
  -S  --Sample  sampling data size     = 512
ACTIONS:
"""
    
Seed = 927162211
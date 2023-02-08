class main:
    the = {
    'dump': False,
    # 'go': data,
    'help': False,
    'seed': 937162211,
    'file' : '../../etc/data/auto93.csv',
    'Far' : '.95',
    'min' : '.5',
    'p' : '2',
    'Sample' : '512'
    }

    help="""[[   
    cluster.lua : an example csv reader script
    (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
    USAGE: cluster.lua  [OPTIONS] [-g ACTION]
    OPTIONS:
    -d  --dump    on crash, dump stack   = false
    -f  --file    name of file           = ../../etc/data/repgrid.csv
    -F  --Far     distance to "faraway"  = .95
    -g  --go      start-up action        = data
    -h  --help    show help              = false
    -p  --p       distance coefficient   = 2
    -s  --seed    random number seed     = 937162211
    ACTIONS:
    ]]"""
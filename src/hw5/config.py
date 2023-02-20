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
    'Sample' : 512,
    'bins': 16,
    'cliffs': 0.147,
    'Halves' : 512,
    'Max': 512,
    'rest' : 4,
    'Reuse' : True
}
help = """"
bins: multi-objective semi-supervised discetization
(c) 2023 Tim Menzies <timm@ieee.org> BSD-2
  
USAGE: lua bins.lua [OPTIONS] [-g ACTIONS]
  
OPTIONS:
  -b  --bins    initial number of bins       = 16
  -c  --cliffs  cliff's delta threshold      = .147
  -f  --file    data file                    = ../../etc/data/auto93.csv
  -F  --Far     distance to distant          = .95
  -g  --go      start-up action              = nothing
  -h  --help    show help                    = false
  -H  --Halves  search space for clustering  = 512
  -m  --min     size of smallest cluster     = .5
  -M  --Max     numbers                      = 512
  -p  --p       dist coefficient             = 2
  -r  --rest    how many of rest to sample   = 4
  -R  --Reuse   child splits reuse a parent pole = true
  -s  --seed    random number seed           = 937162211
ACTIONS:
"""
    
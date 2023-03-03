global the, Help, Seed

the = {
    'bins' : 16,
    'cliffs' : .147,
    'd' : .35,
    'file' : '../../etc/data/auto93.csv',
    'far' : .95,
    'go' : 'nothing',
    'help' : 'false',
    'Halves' : 512,
    'min' : .5,
    'Max': 512,
    'p' : 2,
    'rest' : 4,
    'Reuse' : True,
    'seed': 937162211
}
help = """
xpln: multi-goal semi-supervised explanation
(c) Group 9
  
USAGE: python3 main.py [OPTIONS] [-g ACTIONS]
  
OPTIONS:
  -b  --bins    initial number of bins       = 16
  -c  --cliffs  cliff's delta threshold      = .147
  -d  --d       different is over sd*d       = .35
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
"""
import config 
from tests import *
from LIB import LIB
import sys
lib = LIB()
sys.stdin.reconfigure(encoding='utf-8') 
sys.stdout.reconfigure(encoding='utf-8')
def main(options, help, funs, saved = {}, fails = 0):
    for k, v in lib.cli(lib.settings(help)).items():
        options[k] = v
        saved[k] = v
    if options["help"]:
        print(help)
    else:
        for what in funs:
            if options["go"] == "all" or what == options["go"]:
                for k,v in saved.items():
                    options[k] = v
                if funs[what]() == False:
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
    exit(fails)

egs = {}
def eg(key,str,func):
    egs[key] = func
    config.help = config.help + ("  -g  %s\t%s\n" % (key,str))



eg("rand", "demo random number generation", test_rand)
eg("some", "demo of reservoir sampling", test_some)
eg("sym","check syms", sym_test)
eg("num","check nums", num_test)
eg("csv","read from csv",csv_test)
eg("data","read DATA csv",data_test)
eg("clone","duplicate structure", test_clone)
eg("cliff","sstats test", test_cliffs)
# eg("dist","distance test",test_dist)
# eg("half","divide data in half",test_half)
# eg("tree","make snd show tree of clusters",test_tree)
# eg("sway","optimizing", test_sway)
# eg("bins","find deltas between best and rest", test_bins)
main(config.the, config.help, egs)
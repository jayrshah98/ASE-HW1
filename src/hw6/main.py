import config 
from tests import *
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

eg("the","show settings", the_test)
eg("num","demo of NUM",num_test)
eg("sym","demo SYMS", sym_test)
eg("some","demo of reservoir sampling", some_test)
eg("check_csv","reading csv files", csv_test)
eg("data","showing data sets", data_test)
eg("clone","replicate structure of a DATA", clone_test)
eg("cliffs","stats tests", cliffs_test)
eg("dist","check distance", dist_test)
eg("half","divide data in half", half_test)
eg("tree","make and show tree of clusters", tree_test)
eg("Sway","optimizing", sway_test)
eg("bins","find deltas between best and rest", bins_test)
eg("xpln","explore explanation sets", xpln_test)
main(config.the, config.help, egs)
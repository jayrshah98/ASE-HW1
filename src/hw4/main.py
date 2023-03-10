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

eg("sym","check syms",sym_test)
eg("num","check nums",num_test)
eg("the","show settings", the_test)
eg("copy","check copy", copy_test)
eg("reprows","check reprows", reprows_test)
eg("repcols","check repcols", repcols_test)
eg("synonyms","check synonyms", synonyms_test)
eg("prototype","check prototype", prototype_test)
eg("position","check position", position_test)
eg("every","check every", every_test)



main(config.the, config.help, egs)
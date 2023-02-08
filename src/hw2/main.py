import config 
from tests import *
from lib import LIB
lib = LIB()

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
eg("sym","check syms",sym_test)
eg("num","check nums",num_test)
eg("csv","read from csv",csv_test)
eg("data","read DATA csv",data_test)
# eg("stats","stats from DATA",stats_test)
main(config.the, config.help, egs)
import config 
from tests import *
import sys

sys.stdin.reconfigure(encoding='utf-8') 
sys.stdout.reconfigure(encoding='utf-8')
def main(funs, saved = {}, fails = 0):
        for what in funs:
                if funs[what]() == False:
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
        exit(fails)
        
    
egs = {}
def eg(key,str,func):
    egs[key] = func
    #config.help = config.help + ("  -g  %s\t%s\n" % (key,str))

eg("ok", "seed generation", ok_test)
eg("sample", "samples", sample_test)
eg("nums","NUM", num_test)
eg("gauss", "gaussian", gauss_test)
eg("boot", "boot", boot_test)
eg("basic", "basic", basic_test)
eg("pre", "pre", pre_test)
eg("five", "five", five_test)
eg("six", "six", six_test)
eg("tiles", "tiles", tiles_test)
eg("sk", "sk", sk_test)

if __name__ == "__main__":
    main(egs)
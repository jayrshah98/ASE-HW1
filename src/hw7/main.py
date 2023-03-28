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
eg("sample", "demo of samples", sample_test)
eg("nums","demo of NUM", num_test)
eg("gauss", "demo of gaussian", gauss_test)
eg("boot", "demo of boot", boot_test)
eg("basic", "demo of basic", basic_test)
eg("pre", "demo of pre", pre_test)
eg("five", "demo for five", five_test)
eg("six", "demo for six", six_test)
eg("tiles", "demo for tiles", tiles_test)
eg("sk", "demo for sk", sk_test)

if __name__ == "__main__":
    main(egs)
import os
import shutil
from configparser import ConfigParser

_config = ConfigParser()
_config.read("config.ini",encoding="utf-8")

li=os.listdir(r'C:\\Users\\leixiaodan\Downloads')

for i in li:
    ke=['wj','hgdl','hl','ts','hs','wt','xfc','lhyx','pacf','kl','yflp_s1','gjhr1','gjhr2','hf']

    for k in ke:
        w= _config.get(k, 'user')
        fo=_config.get(k,'folder')#后期加的
        if w in i:
            # shutil.move('C:\\Users\\leixiaodan\Downloads\%s'%i,'C:\\Users\\leixiaodan\Desktop\\futuremonitor\%s'%k)

            shutil.move(r'C:\\Users\\leixiaodan\Downloads\%s' % i, r'\\192.168.53.50\product\期货对账单\\%s\保证金监控中心' % fo) #后期加的
        else:
            print('nothing')
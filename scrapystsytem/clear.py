# -*- coding: utf-8 -*-
import os

if __name__ =="__main__":
    for fpathe,dirs,fs in os.walk(os.path.abspath('.')):
        for f in fs:
            if f.endswith('.pyc') or f.endswith('.csv'):
                os.remove(os.path.join(fpathe,f));
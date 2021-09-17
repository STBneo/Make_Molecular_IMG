import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys,os,glob

def histogram_each(values_list,value_name):
    for i in ["Values","Values_Cumulative"]:
        plt.figure(figsize=(15,15))
        if i == "Values":
            ptitle = "%s"%value_name
            plt.hist(values_list,bins=20)
        elif i == "Values_Cumulative":
            ptitle = "%s Cumulative"%value_name
            plt.hist(values_list,bins=20,cumulative=True)
        else:
            sys.exit(1)
        plt.grid(True)
        plt.xticks(fontsize=45)
        plt.yticks(fontsize=45)
        plt.tight_layout()
        plt.savefig("%s.%s.png"%(value_name,i),tranparent=True)
        plt.close()

def Make_tiled_picture(output_path,a,b,f_list,fn):
    rows = int(a)
    cols = int(b)

    fig = plt.figure(figsize=(rows*6,cols*6))
    i = 1
    for f in f_list:
        img = plt.imread(f)
        ax = fig.add_subplot(rows,cols,i)
        ax.imshow(img)
        ax.set_xticks([]),ax.set_yticks([]),ax.axis("off")
        i += 1

    plt.tight_layout()
    plt.subplots_adjust(wspace=.0,hspace=-.5)
    plt.savefig(output_path + "/" + fn + ".tiled.png",transparent=True)

    plt.close()
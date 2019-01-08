#!/usr/bin/python

# python imports
from __future__ import print_function, absolute_import, division
import os, glob, sys

# The main method
def main():
    # Where to look for Cityscapes
    if 'CITYSCAPES_DATASET' in os.environ:
        cityscapesPath = os.environ['CITYSCAPES_DATASET']
    else:
        cityscapesPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..')
    cityscapesPath_img = cityscapesPath + '/leftImg8bit'

    # how to search for all ground truth
    searchFine   = os.path.join( cityscapesPath_img , "*" , "*" , "*_leftImg8bit.png" )
    print ("searchFine: ", searchFine)
    # search files
    filesFine = glob.glob( searchFine )
    filesFine.sort()
    
    # concatenate fine and coarse
    files = filesFine

    # quit if we did not find anything
    if not files:
        print ( "Did not find any files. Please consult the README." )

    # a bit verbose
    print("Processing {} train&val&test files".format(len(files)))

    train_list = 'train.txt'
    val_list = 'val.txt'
    test_list = 'testing.txt'
    # iterate through files
    progress = 0
    print("Progress: {:>3} %".format( progress * 100 / len(files) ), end=' ')
    # open files
    fw1 = open(train_list, 'w')
    fw2 = open(val_list, 'w') 
    fw3 = open(test_list, 'w')
    for f in files:
        if f.find('train') != -1:
            train_img = f.split('leftImg8bit/')[1] # get 'train/bremen/bremen_000174_000019_leftImg8bit.png'
            # 'leftImg8bit/train/bremen/bremen_000174_000019_leftImg8bit.png'
            train_img_list = 'leftImg8bit/' + train_img
            # label
            # train_label_pre = train_img.split('_leftImg8bit')[0] # get 'train/bremen/bremen_000174_000019'
            # train_label_pre += '_gtFine_labelTrainIds.png' # get 'train/bremen/bremen_000174_000019_gtFine_labelTrainIds.png'
            train_label_pre = train_img.replace("_leftImg8bit.png", "_gtFine_labelTrainIds.png")
            # 'gtFine/train/bremen/bremen_000174_000019_leftImg8bit.png'
            train_label_list = 'gtFine/' + train_label_pre
            fw1.write(train_img_list + ' ' + train_label_list + '\n')
        elif f.find('val') != -1:
            val_img = f.split('leftImg8bit/')[1] # get 'val/munster/munster_000173_000019_leftImg8bit.png'
            # 'leftImg8bit/munster/munster_000173_000019_leftImg8bit.png'
            val_img_list = 'leftImg8bit/' + val_img
            # label
            # val_label_pre = val_img.split('_leftImg8bit')[0] # get 'val/munster/munster_000173_000019'
            # val_label_pre += '_gtFine_labelTrainIds.png' # get 'val/munster/munster_000173_000019_gtFine_labelTrainIds.png'
            val_label_pre = val_img.replace("_leftImg8bit.png", "_gtFine_labelTrainIds.png")
            # 'gtFine/val/munster/munster_000173_000019_gtFine_labelTrainIds.png'
            val_label_list = 'gtFine/' + val_label_pre
            fw2.write(val_img_list + ' ' + val_label_list + '\n')

        else:
            test_img = f.split('leftImg8bit/')[1] # get 'test/berlin/berlin_000000_000019_leftImg8bit.png'
            # 'leftImg8bit/test/berlin/berlin_000000_000019_leftImg8bit.png'
            test_img_list = 'leftImg8bit/' + test_img
            fw3.write(test_img_list + '\n')

        # status
        progress += 1
        print("\rProgress: {:>3} %".format( progress * 100 / len(files) ), end=' ')
    print ('\n')

# call the main
if __name__ == "__main__":
    main()

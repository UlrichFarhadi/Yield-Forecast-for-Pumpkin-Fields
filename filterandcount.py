#import os
#import sys
from ast import If
from xml.etree.ElementTree import tostring
import cv2
from cv2 import imshow
from cv2 import waitKey
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread("Orthomosaic.jpg")
    print("Shape of Orthomosaic", img.shape)
    
    tile_h = 500
    tile_w = 500

    img_h, img_w, channels = img.shape
    print("img_h: ", img_h)
    print("img_w: ", img_w)
    h_times = int(np.floor(img_h/tile_h))
    w_times = int(np.floor(img_w/tile_w))
    tiles = []
    for i in range(h_times):
        for j in range (w_times):
            tiles.append(img[tile_h * i:tile_h * (i+1), tile_w * j: tile_w * (j+1)])
    
    print("Tiles Shape: ", np.array(tiles).shape)

    print("tilecolor", tiles[0][1,1])
    #print("TEST: ", tiles[0][1,1][0])
    white_checker = 5
    tiles_sorted = []
    for tile in tiles:
        white_counter = 0
        for pix in range(white_checker):
            if tile[pix, pix][0] == 255 and tile[pix, pix][1] == 255 and tile[pix, pix][2] == 255:
                white_counter = white_counter + 1
        if white_checker != white_counter:
            tiles_sorted.append(tile)
    tiles_sorted = np.array(tiles_sorted)
    print("tiles_sorted.shape: ", tiles_sorted.shape)


    # Print a couple of tiles
    #imshow("win1", tiles_sorted[1])
    #imshow("win2", tiles_sorted[10])
    #imshow("win3", tiles_sorted[240])
    #imshow("win4", tiles_sorted[300])
    #imshow("win5", tiles_sorted[410])
    #cv2.imwrite("dataset/TEST.jpg", tiles_sorted[300])

    #waitKey(0)

    dataset_size = 100 # First trying if 100 is enough. Phew
    # Generate random integer array
    tiles_sorted_length = tiles_sorted.shape[0]
    random_tile_ints = np.random.randint(tiles_sorted_length, size=dataset_size)
    #print("Tile_ints: ", random_tile_ints)
    counter = 0
    for i in random_tile_ints:
        #cv2.imwrite("dataset/" + str(counter) + ".jpg", tiles_sorted[i])
        counter = counter + 1
    
    counter = 0
    for i in range(np.array(tiles).shape[0]):
        #cv2.imwrite("all_tiles/" + str(counter) + ".jpg", tiles[i])
        counter = counter + 1


    counter = 0
    # Restitch the tiles with bounding boxes back together
    combmosaic = []
    for i in range(h_times):
        firstimg = cv2.imread("images_with_bounding_boxes_500px/" + str(counter) + ".jpg")
        counter = counter + 1
        for j in range (1, w_times):
            newimg = cv2.imread("images_with_bounding_boxes_500px/" + str(counter) + ".jpg")
            firstimg = np.concatenate((firstimg, newimg), axis=1)
            counter = counter + 1
        combmosaic.append(firstimg)

    #imshow("test", combmosaic[0])
    #waitKey(0)

    firstimg = combmosaic[0]
    for i in range(1, len(combmosaic)):
        firstimg = np.concatenate((firstimg, combmosaic[i]), axis=0)
    
    cv2.imwrite("mosaic_pumpkins_detected_500px.jpg", firstimg)
    #imshow("test", firstimg)
    #waitKey(0)


main()

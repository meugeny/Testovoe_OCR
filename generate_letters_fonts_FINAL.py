import os
import pygame
import numpy as np
import cv2
from PIL import Image

Colors = {'white': (255, 255, 255), 'black': (0,0,0)}
Sizes = {'medium': 100, 'large': 150}

Letters = list(range(1040, 1072))
Integers = list(range(48, 58))
single_set = Letters + Integers
words = []
img_size = 128
# generate words using a depth-first-search, max_w_len is the maximum length of the words, for now is one(single characters)
max_w_len = 1

def dfs(w, L):
    if len(w)==max_w_len:
        return
    for l in L:
        words.append(w+chr(l))
        dfs(w+chr(l), L)

dfs('', single_set)

font_dir = './fonts'
if not os.path.exists(font_dir):
    os.makedirs(font_dir)

pygame.init()
screen = pygame.display.set_mode((img_size, img_size)) # image size Fix(128 * 128)
#cnt = 0

# Get the list of all files and directories
# in the root directory
path = "fonts2"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# print the list
print(dir_list)
i = 0
for word in words: # 1st round for words

    print(word)
    for size in Sizes.keys():
        for font in dir_list:  # 5th round for fonts
            i += 1
            # 1 set back_color
            screen.fill(Colors['white']) # background color
            # 2 set letter/word
            # selected_letter = chr(letter)
            selected_letter = word
            # 3,4 set font and size
            selected_font = pygame.font.Font(f'{path}/{font}', Sizes[size]) #pygame.font.SysFont(font, Sizes[size]) # size and bold or not
            font_size = selected_font.size(selected_letter);
            # 5 set font_color

            rtext = selected_font.render(selected_letter, True, Colors['black'], Colors['white'])
            # 6 render
            drawX = img_size / 2 - (font_size[0] / 2.0)
            drawY = img_size / 2 - (font_size[1] / 2.0)
            # screen.blit(rtext, (img_size/2, img_size/2))
            # screen.blit(rtext, (img_size / 4, 0))
            screen.blit(rtext, (drawX, drawY)) # because
            # Save images in a specific path E.g. A / 64/ red / blue / arial

            img_name = selected_letter + size + '_' + font + ".png"
            img_path = os.path.join(font_dir, selected_letter)
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            # pygame.image.save(screen, os.path.join(img_path, img_name))

            view = pygame.surfarray.array3d(screen)
            view = view.transpose([1, 0, 2])
            # img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)
            image_gray = cv2.cvtColor(view, cv2.COLOR_BGR2GRAY)
            image = cv2.blur(image_gray,(10,10))
            # is_success, im_buf_arr = cv2.imencode(".png", image_gray)
            # im_buf_arr.tofile(f'{img_path}/{img_name}')

            im = Image.fromarray(image, mode='L')
            im.save(f'{img_path}/{img_name}')

print('finished')


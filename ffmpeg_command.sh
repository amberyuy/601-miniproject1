#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:20:38 2018

@author: wangyuying
"""

# ffmpeg command line
ffmpeg -r 1/2 -i %d.jpg -c:v libx264 -vf "fps=24,format=yuv420p" out.mp4
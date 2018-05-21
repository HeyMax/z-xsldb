#!/bin/bash
#download
rm -f /root/*.xlsx && wget --execute robots=off -nc -nd -r -l1  -A 'QQ*.xlsx' -P /root/  http://192.168.200.100/mirror/carl/QQ%E7%BE%A4%E9%97%AE%E9%A2%98%E8%AE%B0%E5%BD%95/
#import
python3 z-import.py /root/QQ*.xlsx

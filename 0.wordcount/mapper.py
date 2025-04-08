#!/usr/bin/env python3
import sys

for line in sys.stdin: # 스탠다드인:파일 전체
    line = line.strip()
    words = line.split()

    for word in words:
        print(f'{word}\t1')
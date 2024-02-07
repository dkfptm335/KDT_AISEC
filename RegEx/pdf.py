import re
import zlib
import json

def save_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

keyword_counts = {}

with open('pdf1.bin', 'rb') as f:
    fbuf = f.read()
    
    for t in re.finditer(rb"(\d+) 0 obj <<(.*)>>\s*(stream\s*([\d\D]*?)\s*endstream)?\s*endobj", fbuf):
        s = t.group(2).decode()
        print(s)
        
    #     for keyword in re.findall(r'/[a-zA-Z]+', s):
    #         if keyword in keyword_counts:
    #             keyword_counts[keyword] += 1
    #         else:
    #             keyword_counts[keyword] = 1
    
    # print(json.dumps(keyword_counts, indent=2))
        
    
    # for t in re.finditer(rb"(\d+) 0 obj <<(.*)>>\s*(stream\s*([\d\D]*?)\s*endstream)?\s*endobj", fbuf):
    #     if t.group(4): # stream 정보 존재 여부
    #         if b'/FlateDecode' in t.group(2): # 압축 여부
    #             data = zlib.decompress(t.group(4))
    #             filename = f'{t.group(1).decode()}.bin'
    #             save_file(filename, data)
    #             print(f'{filename} saved')
            
import urllib2
import requests
import json

BASE_DIR = "http://chartapi.finance.yahoo.com/instrument/1.0/"
SUFFIX_DIR = "/chartdata;type=quote;range=1d/csv"


def parseline(string_line):
    st = string_line.split(':')
    if len(st)>1:
        return (st[0], st[1].split(','))
    return None


def process_data(shortcut):
    url = BASE_DIR+shortcut+SUFFIX_DIR
    response = requests.get(url)
    raw_json_unit = {}
    content = response.content
    content = content.split('\n')
    if len(content)<10:
        return None
    else:
        for i in range(18):
            line_tuple = parseline(content[i])
            if line_tuple!=None:
                raw_json_unit[line_tuple[0]] = line_tuple[1]
    
    return raw_json_unit

def get_data(filename):
    with open(filename,"rb") as f:
        json_data = json.loads(f.read())
        f.close()
    return json_data


if __name__ == '__main__':
    short_list = get_data("symbols.json")
    valid_set = []
    for lst in short_list:
        for e in lst:
            chk = process_data(e)
            if chk != None:
                valid_set.append(chk);
    with open("tickers.json","wb") as f:
        f.write(json.dumps(valid_set))
        f.close()
    
    # print valid_set


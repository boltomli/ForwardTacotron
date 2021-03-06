import re
from utils.files import get_files
from pathlib import Path
from typing import Union


def ljspeech(path: Union[str, Path]):
    csv_file = get_files(path, extension='.csv')

    assert len(csv_file) == 1

    text_dict = {}

    with open(csv_file[0], encoding='utf-8') as f :
        for line in f :
            split = line.split('|')
            text_dict[split[0]] = split[-1]

    return text_dict


def databaker(path: Union[str, Path]):
    label_file = get_files(path, extension='.txt')
    assert len(label_file) == 1
    text_dict = {}
    prosody_pattern = re.compile(r'#\d')
    with open(label_file[0], encoding='utf-8') as f:
        for line in f:
            if not line.startswith('\t'):
                split = line.split('\t')
                text_dict[split[0]] = ''.join(re.split(prosody_pattern, split[1]))
    return text_dict

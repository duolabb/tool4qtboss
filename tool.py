import os
import json
import re

CONSTANT_RSC_STR = 'resources'
CONSTANT_BOMB_STR = 'bomb'
CONSTANT_MAP_STR = 'map'
CONSTANT_PLAYER_STR = 'player'

CONSTANT_MAP_KEY = 'map'
CONSTANT_BOMB_KEY = 'pp_id'
CONSTANT_PLAYER_KEY = 'id'
CONSTANT_ITEMS_KEY = 'have_items'
CONSTANT_MAX_KEY = 'max'
CONSTANT_BOSS_KEY = 'name'
CONSTANT_HP_KEY = 'hp'
CONSTANT_MUSIC_KEY = 'music'
CONSTANT_SOUND_KEY = 'sound'
CONSTANT_KEYS_KEY = 'keys'

CONSTANT_ITEMS_DICT = {'1': '泡泡', '2':'威力', '3':'鞋子', '9':'慢慢胶水', '21':'电网' ,'23':'香蕉皮', '24':'叉子'}
CONSTANT_MAX_DICT = {'pp':'泡泡', 'weili':'威力', 'xiezi':'鞋子'}
CONSTANT_KEYS_DICT = {"up":'上', "down":'下', "left":'左', "right":'右', "space":'放泡', "key1":'道具1', "key2":'道具2', "key3":'道具3', "key4":'道具4', "key5":'道具5', "key6":'道具6', "key7":'道具7', "ctrl":'使用当前道具', "T":'表情1', "Y":'表情2', "U":'表情3', "I":'表情4', "O":'表情5', "P":'表情6'}

CONSTANT_BOSS_LIST = ['圣诞格里芬', '大盗格里芬', '鬼仆格里芬', '大年兽', '小年兽', '水手', '大副', '虎克']

def get_path(* args):
    return '/'.join(args)
def get_num(str):
    return int(''.join(re.findall(r'\d+', str)))

json_file_path = 'config.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 获取目录下的所有文件和子目录名
bomb_list = os.listdir(get_path(CONSTANT_RSC_STR, CONSTANT_BOMB_STR))
map_list = os.listdir(get_path(CONSTANT_RSC_STR, CONSTANT_MAP_STR))
player_list = os.listdir(get_path(CONSTANT_RSC_STR, CONSTANT_PLAYER_STR))

# 修改数据
json_data[CONSTANT_BOMB_KEY] = get_num(bomb_list[0])
json_data[CONSTANT_MAP_KEY] = map_list[0]
json_data[CONSTANT_PLAYER_KEY] = get_num(player_list[0])

# 将修改后的数据写回文件
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print(f"Data in \'{json_file_path}\' updated.")
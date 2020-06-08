# region [Imports]

import os
import self_created.gid_land as gil

# endregion [Imports]




arma_mods_folder = 'C:/Program Files (x86)/Steam/steamapps/common/Arma 3/!Workshop'

dict_of_pbo_lists = {}



def get_folder_list(in_dir):
    _list = os.listdir(in_dir)
    _list.remove('!DO_NOT_CHANGE_FILES_IN_THESE_FOLDERS')
    return _list

def dict_of_clean_name_and_path(in_list, in_dir, out_dir):
    n_mod_dict = {}
    for names in in_list:
        _name = names.replace('@', '')
        _opath_create = f'{out_dir}/{_name}'
        _ipath_create = f'{in_dir}/{names}/addons'
        n_mod_dict[_opath_create] = _ipath_create
    return n_mod_dict

def make_dict_of_pbo_lists(in_dict):
    for key, value in in_dict.items():
        _pbo_list = []
        _temp_pbo_list = os.listdir(value)
        for titems in _temp_pbo_list:
            if '.pbo' in titems and '.bisign' not in titems:
                _n_item = f'{value}/{titems}'
                _pbo_list.append(_n_item)
        dict_of_pbo_lists[key] = _pbo_list
    return dict_of_pbo_lists

def make_folders(in_dict):
    for key in in_dict:
        os.makedirs(key)


def run_the_shit(in_dict):
    for key, value in in_dict.items():
        if '3cb' not in value.lower():
            _phrase = f'extractPboDos -P -N "{value}" "{key}"'
            os.system(f'cmd /c {_phrase}')

print('----------------------------------------\nWarning: 3cb mods will not be extracted as extracting them or any other obfuscated mod is not possible!\n----------------------------------------\n\n')
print('\n###########################################\n')
print("Mikeros tools is a prerequisite for this script, if you don't have it installed, please visit \n[https://mikero.bytex.digital/Downloads]\nand download it\n\nabsolutely need is:")
print("\t - ExtractPbo (it also needs to be on your path, but this should happen automatically when you install it")
print('\n###########################################\n\n')
print('Please enter your Arma mod directory (without Quotes)\nExample: C:\Program Files (x86)\Steam\steamapps\common\Arma 3\!Workshop\n\ninput: ', end='')
arma_mods_folder = gil.pathmaker(input())
print('''Please enter the folder you want to extract the mods to (without Quotes, without trailing backslash)\n
      make sure it is empty, as this script will create a new folder for each mod\n
      and because I am lazy it will fail if the folder already exists\n
      Example: D:\Archives\ArmA\Mods_reference\n\ninput: ''', end='')
output_folder = gil.pathmaker(input())
print('preparing inputs for use in script')
first_list = get_folder_list(arma_mods_folder)
second_dict = dict_of_clean_name_and_path(first_list, arma_mods_folder, output_folder)
final_dict = make_dict_of_pbo_lists(second_dict)
print('starting folder creation')
make_folders(final_dict)
print('starting extraction, this can take a while')
run_the_shit(second_dict)

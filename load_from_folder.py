from os import listdir, mkdir, remove, rmdir
from os.path import isfile, join, isdir
import json


class LoadAndSaveData:
    def __init__(self, dir):
        self.dir = dir
        if not isdir(dir):
            mkdir(dir)

    def __read_json(self, file_path):
        with open(file_path, 'r') as target:
            return json.load(target)

    def __save_json(self, file_path, data):
        with open(file_path, 'w') as target:
            return json.dump(data, target)

    def __get_dir_files(self):
        only_files = [join(self.dir, f) for f in listdir(self.dir)
                      if isfile(join(self.dir, f)) and f[-5:].lower() == '.json']

        return only_files

    def load_data_set(self):
        result = []
        for item in self.__get_dir_files():
            try:
                result.append(self.__read_json(item))
            except:
                pass

        return result

    def save_data_set(self, data_set):
        for i in range(len(data_set)):
            self.__save_json(join(self.dir, str(i) + '.json'), data_set[i])

    def clear_data_set(self):
        try:
            for path in self.__get_dir_files():
                remove(path)

            rmdir(self.dir)
        except:
            pass


if __name__ == "__main__":
    test_data_set = [
        {'inputs': [1, 1], 'result': 1},
        {'inputs': [1, 0], 'result': -1},
        {'inputs': [0, 1], 'result': -1},
        {'inputs': [0, 0], 'result': -1},
    ]
    x = LoadAndSaveData('./test')
    x.save_data_set(test_data_set)
    print(x.load_data_set())
    x.clear_data_set()

class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for f in self.file_names:
            with open(f, 'r',encoding='utf-8') as file:
                str_file = file.read()
                str_file = str_file.lower()
                for p in ".,=!?:;-":
                    str_file = str_file.replace(p, '')
                all_words[f] = str_file.split()
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word.lower()) + 1
        return result
    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = 0
            for i in words:
                if word.lower() == i:
                    result[name] += 1

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
import glob, os, polib

def parser(list):
    """
    Convert comma separated items
    to list
    """
    split = list.split(',')
    out = [x.strip() for x in split]

    return out

def vbool(val):
    return True if val == 'true' else False


class DocsPro(object):
    """docstring for DocsPro"""
    def __init__(self, path, multilang=False, ignore_langs=''):
        super(DocsPro, self).__init__()
        self.multilang = vbool(multilang)
        self.ignore_langs = ignore_langs
        self.path = path
        # self.PoFiles = []
        # self.warnings = []


    def __get_PoFiles(self, dir):
        """
        Get all .po files and absolute paths
        """
        pofiles = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".po"):
                    file_path = os.path.join(root, file)
                    pofiles.append(file_path)

        return pofiles


    def __msgs_data(self, po, obsoletes):
        """
        Get translated and total strings
        """
        translatedStrings = len(po.translated_entries())
        totalStrings = len(po) - obsoletes # Substrate obsoletes from total entries

        return (translatedStrings, totalStrings)


    def __list_langs(self):
        return os.listdir(self.path)


    def __remove_ignored_files(self, pofiles, ignored_langs):
        """
        Remove files with ignored langs in path
        """
        for_remove = []
        for lang in ignored_langs:
            lang_match = [file for file in pofiles if f"/{lang}/" in file]
            for_remove.extend(lang_match)

        return list(set(pofiles) - set(for_remove))

    def __total(self, pofiles):
        """
        Calculate final lang total progress
        """
        translatedStrings = 0
        totalStrings = 0

        for file in pofiles:
            po = polib.pofile(file)
            obsoletes = len(po.obsolete_entries())
            msgs_data = self.__msgs_data(po, obsoletes)
            translatedStrings += msgs_data[0]
            totalStrings += msgs_data[1]

        total = (translatedStrings / totalStrings) * 100

        return "%.2f" % (total)


    def translated(self):
        ignored_langs = self.ignore_langs
        print(bool(self.multilang))
        if self.multilang:
            target_langs = self.__list_langs()
            target_langs = [x for x in target_langs if x not in ignored_langs]
            langs_data = {}

            for lang in target_langs:
                lang_dir = os.path.join(self.path, lang)
                lang_files = self.__get_PoFiles(lang_dir)
                lang_progress = self.__total(lang_files)
                langs_data[lang] = lang_progress

            return langs_data

        else:
            pofiles = self.__get_PoFiles(self.path)
            pofiles = self.__remove_ignored_files(pofiles, ignored_langs)
            total = self.__total(pofiles)
            return total
"""
def main():
    path = 'docs/locales'
    dp = DocsPro(path)
    d = dp.translated()
    pprint(d)

if __name__ == '__main__':
    main()
"""

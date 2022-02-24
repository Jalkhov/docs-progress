import glob
import os
import polib
from pprint import pprint


class DocsPro(object):
    """docstring for DocsPro"""
    def __init__(self, path):
        super(DocsPro, self).__init__()
        self.path = path
        self.PoFiles = []
        self.translatedStrings = 0
        self.totalStrings = 0
        # self.warnings = []


    def __get_PoFiles(self):
        """
        Get all .po files and absolute paths
        """
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".po"):
                    file_path = os.path.join(root, file)
                    self.PoFiles.append(file_path)


    def __msgs_data(self, po, obsoletes):
        """
        Get translated and total strings
        """
        translatedStrings = len(po.translated_entries())
        totalStrings = len(po) - obsoletes # Substrate obsoletes from total entries

        return (translatedStrings, totalStrings)


    def __walk_files(self):
        """
        Walk all .po files and store global total
        translated and total strings
        """
        files = self.PoFiles
        for file in files:
            po = polib.pofile(file)
            obsoletes = len(po.obsolete_entries())
            msgs_data = self.__msgs_data(po, obsoletes)
            self.translatedStrings += msgs_data[0]
            self.totalStrings += msgs_data[1]


    def __total(self):
        """
        Calculate final total progress
        """
        return (self.translatedStrings / self.totalStrings) * 100


    def translated(self, fix=True):
        self.__get_PoFiles()
        self.__walk_files()

        total = self.__total()

        return "%.2f" % (total) if fix else str(total)


path = 'docs/locales'
dp = DocsPro(path)
d = dp.translated()

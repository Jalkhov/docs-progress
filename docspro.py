import glob
import os
import polib

# path = 'docs/locales/es/LC_MESSAGES'

class DocsPro(object):
    """docstring for DocsPro"""
    def __init__(self, path):
        super(DocsPro, self).__init__()
        self.path = path
        self.po_files = []
        self.translatedMessageCount = 0
        self.totalMessages = 0


    def __get_po_files(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".po"):
                    file_path = os.path.join(root, file)
                    self.po_files.append(file_path)


    def __msgs_data(self, po, obsoletes):
        translatedMessageCount = len(po.translated_entries())
        totalMessages = len(po) - obsoletes # Substrate obsoletes from total entries

        return (translatedMessageCount, totalMessages)


    def __walk_files(self):
        files = self.po_files
        for file in files:
            po = polib.pofile(file)
            obsoletes = len(po.obsolete_entries())
            msgs_data = self.__msgs_data(po, obsoletes)
            self.translatedMessageCount += msgs_data[0]
            self.totalMessages += msgs_data[1]


    def __total(self) -> float:
        return (self.translatedMessageCount / self.totalMessages) * 100


    def translated(self, fix=True):
        self.__get_po_files()
        self.__walk_files()
        total = self.__total()

        return "%.2f" % (total) if fix else str(total)


# dp = DocsPro(path)
# d = dp.translated()
# print(d)


import re
from doccodes import Doccode

from doc_codes import DoccodeManagerInstance
from base import Doccode

class ProjectGutenbergEbookDoccode(Doccode):
    active = True
    name = 'Project Gutenberg eBooks'
    description = '[0-9]{1,6}'
    doccode_id = 3

    def validate(self, document_name):
        if re.match('^[0-9]{1,6}$', document_name):
            return True
        else:
            return False

    # Split document_name as per Project Gutenberg method for 'eBook number' not, eText
    # http://www.gutenberg.org/dirs/00README.TXT
    def split(self, document_name):
        d = []
        for i in range(len(document_name)):
            d.append(document_name[i-1:i])
        return d

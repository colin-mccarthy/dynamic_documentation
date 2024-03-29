#
# list_compress filter
#
from jinja2 import TemplateError
from itertools import count, groupby
from ansible.errors import AnsibleFilterError

import re

class FilterModule(object):

   def list_compress(self,list_to_compress):
      if not isinstance(list_to_compress, list):
         raise AnsibleFilterError('value must be of type list, got %s' % type(list_to_compress))

      G=(list(x) for _,x in groupby(sorted(list_to_compress), lambda x,c=count(): next(c)-x))
      return (",".join("-".join(map(str,(g[0],g[-1])[:len(g)])) for g in G))


   def filters(self):
      return {
         'list_compress' : self.list_compress,
    }


from yaml import safe_load
from glob import glob
from os.path import basename, abspath, dirname, join
from collections import defaultdict

from permm.core.Mechanism import Mechanism
_mechanisms_dir = abspath(dirname(__file__))

atoms = safe_load(open(join(_mechanisms_dir, 'atoms.yaml')))

class _mech_fromkey(defaultdict):
    def __init__(self):
        self._paths = dict([(basename(path)[:-5], path) for path in glob(join(_mechanisms_dir, '*.yaml'))])

    def keys(self):
        return [k for k in list(self._paths.keys())]
        
    def iterkeys(self):
        for key in list(self._paths.keys()):
            return key
        
    def iteritems(self):
        for key in list(self._paths.keys()):
            yield key, self[key]

    def __iter__(self):            
        return iter(list(self.keys()))
        
    def keys(self):
        return tuple(self._paths.keys())
        
    def __missing__(self, key):
        if key not in list(self._paths.keys()):
            raise KeyError("%s not in mechanisms")
        
        mech = self[key] = Mechanism(self._paths[key])
        return mech
        
mechanism_dict = _mech_fromkey()

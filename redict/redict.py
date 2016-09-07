import re
from copy import copy
from collections import UserDict


class ReDict(UserDict):
    def re_get(self, s, squeeze=True, default=None): 
        """Return the values whose keys match the parameter `s`.

        Args:
            s: A string that is expected to be matched by one of the keys in 
               this ReDict instance
            squeeze: In the case where a single matching value is found, 
                     `squeeze` as `True` (default) means that only the value
                     will be returned and `False` means a length one list
                     will be returned.

        Returns:
            Value from the dictionary or values as a list.
        """
        res = []
        for pat, key in list(self.data.items()):
            if re.match(pat, s):
                res.append(key)
        if len(res) == 1:
            return res[0]
        elif res == []:
            return default
        else:
            return None


def update_with_redict(d, rd, names, func=None, none_safe=True):
    """Generate a dictionary whose keys are the elements in `names` and
    whose values are found using rd.re_get(names).

    Args:
        d: a dictionary to be updated with a new dictionary formed from `rd`
           and `names`.
        rd: An ReDict.
        names: A sequence of names that will be used to get values from `rd`.
        func: An optional function to be run on the result of `rd.re_get(name)`
              before it is added to `d`.

    Returns:
        A dict of the form `{name: rd.re_get(name)}`
    """
    for name in names:
        v = rd.re_get(name)
        d[name] = _apply_func(func, v, none_safe)
    return d


def _apply_func(func, x, none_safe):
    """Helper for `update_with_redict()` containing logic for running func(x).
    """
    if func is not None:
        if not none_safe:
            x = func(x)
        else:
            if x is not None:
                x = func(x)
    return x

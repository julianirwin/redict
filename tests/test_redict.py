from nose.tools import assert_equal, assert_is_none
from redict import ReDict, update_with_redict


class TestRedict:
    @classmethod
    def setup(cls):
        d = {'.*foo.*': 1, '.*bar.*': 2, '.*baz.*': 3}
        cls.rd = ReDict(d)

    def test_get_no_match(self):
        assert_is_none(self.rd.re_get('asdf_biz_asdf'))

    def test_get_no_match_with_default(self):
        assert_equal(self.rd.re_get('asdf_biz_asdf', default=0), 0)

    def test_get_match(self):
        assert_equal(self.rd.re_get('x_foox'), 1)

    def test_brackets_match(self):
        assert_equal(self.rd.re_get('x_foox'), 1)

    def test_insert_pattern_after_initialization(self):
        pass

class TestUpdateWithReDict:
    @classmethod
    def setup(cls):
        d = {'.*foo.*': 1, '.*bar.*': 2, '.*baz.*': 3}
        cls.rd = ReDict(d)
        cls.names = ('zfooz', 'barai', 'baz9', 'sjg')

    def test_update_empty_dict_no_func(self):
        d = {}
        res = update_with_redict(d, self.rd, self.names)
        actual = {'zfooz': 1, 'barai': 2, 'baz9': 3, 'sjg': None}
        assert_equal(res, actual)

    def test_update_existing_dict_no_func(self):
        d = {'zfooz': 0, 'barai': 1, 'baz9': 0, 'sjg': 0}
        res = update_with_redict(d, self.rd, self.names)
        actual = {'zfooz': 1, 'barai': 2, 'baz9': 3, 'sjg': None}
        assert_equal(res, actual)

    def test_update_empty_dict_func_is_increment(self):
        d = {}
        func = lambda x: x + 1
        res = update_with_redict(d, self.rd, self.names, func=func)
        actual = {'zfooz': 2, 'barai': 3, 'baz9': 4, 'sjg': None}
        assert_equal(res, actual)

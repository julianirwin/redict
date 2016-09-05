from nose.tools import assert_equal, assert_is_none, raises
from redict import Redict



def TestRedict:
    @classmethod
    def setup(cls):
        d = {'.*foo.*': 1, '.*bar.*': 2, '.*baz.*': 3}
        cls.rd = Redict(d)

    def test_get_no_match(self):
        assert_is_none(self.rd.get('asdf_biz_asdf'))

    def test_get_no_match_with_default(self):
        assert_equal(self.rd.get('asdf_biz_asdf', 0), 0)

    def test_get_match(self):
        assert_equal(self.rd.get('x_foox'), 1)

    @raises(KeyError)
    def test_brackets_no_match(self):
        assert_equal(self.rd['x_biz((('])

    def test_brackets_match(self):
        assert_equal(self.rd['x_foox'], 1)


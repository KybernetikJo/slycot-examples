import slycot
from slycot.exceptions import raise_if_slycot_error 
from warnings import warn
import unittest

def fun(info, print_loc_doc=False):
    '''Example function

    Raises
    ------
    SlycotParameterError
        :info = -i: the i-th argument had an illegal value;
        :info = -3: test spezial case;
    SlycotArithmeticError
        :info = 1: INFO is 1
        :info > 1 and info < n:
            INFO is {info}, which is between 1 and {n}
        :n <= info < m:
            {info} is in [{n}, {m:10.2g})!

    Warns
    -----
    SlycotResultWarning
        :info >= 120: {info} is too large
    SlycotResultWarning
        :iwarn == 1: IWARN is 1
    '''
    n, m = 4, 120.

    arg_list = ["a", "b + hidden", "c + hidden"]
    loc = locals()
    # Warns section is only allowed for list [iwarn, info], if simulates that
    doc = (fun.__doc__ if type(info) is list else fun.__doc__[:-144])

    if print_loc_doc:
        print(loc)
        print(doc)
    raise_if_slycot_error(info,
                        arg_list=["a", "b", 3],
                        docstring=doc,
                        checkvars=loc)
    

class TestSyclotExceptions(unittest.TestCase):

    def test_info_neg1(self):
        self.assertRaises(slycot.exceptions.SlycotParameterError,fun,-1)

    def test_info_neg2(self):
        self.assertRaises(slycot.exceptions.SlycotParameterError,fun,-2)

    def test_info_pos1(self):
        self.assertRaises(slycot.exceptions.SlycotArithmeticError,fun,1)

    def test_info_pos2(self):
        self.assertRaises(slycot.exceptions.SlycotArithmeticError,fun,2)

    #def test_info_pos120(self):
    #    self.assertRaises(slycot.exceptions.SlycotResultWarning,fun,120)

    #def test_info_pos_warn1(self):
    #    self.assertRaises(slycot.exceptions.SlycotResultWarning,fun,[1,0])

if __name__ == '__main__':
    unittest.main()

    #fun(120)
# @file utility_functions_test.py
# unit test for utility_functions module.
#
#
# Copyright (c) Microsoft Corporation
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
##

import unittest
import os
import edk2toollib.utility_functions as utilities


class UtilityFunctionsTest(unittest.TestCase):

    def test_RunPythonScript(self):  # simple- run yourself!
        path = __file__
        working_dir = os.path.dirname(__file__)
        ret = utilities.RunPythonScript(path, "", working_dir)
        self.assertEqual(ret, 0)
        # test it with all the named parameters
        ret = utilities.RunPythonScript(path, "", capture=False, workingdir=working_dir,
                                        raise_exception_on_nonzero=True)
        self.assertEqual(ret, 0)
        # now try a bad path
        bad_path = __file__ + ".super.bad"
        ret = utilities.RunPythonScript(bad_path, "", capture=False, workingdir=None, raise_exception_on_nonzero=False)
        self.assertNotEqual(ret, 0)
        # now we expect it to throw an exception
        with self.assertRaises(Exception):
            ret = utilities.RunPythonScript(bad_path, "", capture=False, workingdir=None,
                                            raise_exception_on_nonzero=True)
            self.assertNotEqual(ret, 0)


# DO NOT PUT A MAIN FUNCTION HERE
# this test runs itself to test runpython script, which is a tad bit strange yes.

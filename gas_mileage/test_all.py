"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
Do Not Move on to the next function until its tests report 'ok' or your code
may not work as expected.
"""

import unittest

# This is another test designed for the unittest discovery to find and fail on.
# it will not be used if the file is ran directly.
class TestAllFail(unittest.TestCase):
    def test_fail(self):
        self.fail('You should run the test_all.py file directly, Do not use the "Run Unittests in test_all.py" option from your IDE')

if __name__ == '__main__':
    from test_createNotebook import TestCreateNotebook
    from test_milesPerGallon import TestMilesPerGallon
    from test_recordTrip import TestRecordTrip
    from test_listTrips import TestListTrips
    from test_calculateMPG import TestCalculateMPG
    from test_formatMenu import TestFormatMenu
    from test_formatMenuPrompt import TestFormatMenuPrompt
    from test_getUserString import TestGetUserString
    from test_getUserFloat import TestGetUserFloat
    from test_getDate import TestGetDate
    from test_getMiles import TestGetMiles
    from test_getGallons import TestGetGallons
    from test_recordTripAction import TestRecordTripAction
    from test_listTripsAction import TestListTripsAction
    from test_calculateMPGAction import TestCalculateMPGAction
    from test_quitAction import TestQuitAction
    from test_applyAction import TestApplyAction

    testCases = [
        TestCreateNotebook,
        TestMilesPerGallon,
        TestRecordTrip,
        TestListTrips,
        TestCalculateMPG,
        TestFormatMenu,
        TestFormatMenuPrompt,
        TestGetUserString,
        TestGetUserFloat,
        TestGetDate,
        TestGetMiles,
        TestGetGallons,
        TestRecordTripAction,
        TestListTripsAction,
        TestCalculateMPGAction,
        TestQuitAction,
        TestApplyAction
    ]

    allTests = []
    for testCase in testCases:
        allTests.append(unittest.TestLoader().loadTestsFromTestCase(testCase))

    unittest.TextTestRunner().run(unittest.TestSuite(allTests))
else:
    print('THE TEST SUITE WAS NOT EXECUTED.')
    print('You need to run this file directly; not in "unittest" mode.')
    print('This file can not be imported as a module.')
    print('If you see this message it does not mean your code does not work,')
    print('but rather this file was run incorrectly.')

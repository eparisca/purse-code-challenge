import unittest
import datetime
from dateutil import parser

import api.date_parser


class DateParserTestCase(unittest.TestCase):
    def test_parse_date_string(self):
        """
        Single date "Dec. 20, 2016"
        """
        input_data = "Dec. 20, 2016"
        expected = datetime.date(2016, 12, 20)
        actual = parser.parse(input_data).date()
        self.assertEqual(expected, actual)

    def test_is_date_range_one_date(self):
        input_data = "Dec. 20, 2016"
        self.assertFalse(api.date_parser.is_date_range(input_data))

    def test_is_date_range_two_dates_abbreviated(self):
        input_data = "Dec. 20, 2016 - Dec. 30, 2016"
        self.assertTrue(api.date_parser.is_date_range(input_data))

    def test_is_date_range_two_dates_non_abbreviated(self):
        input_data = "April 20, 2017 - April 30, 2017"
        self.assertTrue(api.date_parser.is_date_range(input_data))

    def test_is_date_range_two_dates_suffixed(self):
        input_data = "May 20th, 2017 - May 31st, 2017"
        self.assertTrue(api.date_parser.is_date_range(input_data))

    def test_format_date_as_iso8601(self):
        input_data = "Dec. 20, 2016"
        dt = api.date_parser.parse_date_string(input_data)
        expected = "2016-12-20"
        actual = api.date_parser.format_date_as_iso8601(dt[0])
        self.assertEqual(expected, actual)

    def test_parse_abbreviated_date_range(self):
        """
        Date Range "Dec. 20, 2016 - Dec. 30, 2016"
        """
        input_data = "Dec. 20, 2016 - Dec. 30, 2016"
        expected_start_date = datetime.date(2016, 12, 20)
        expected_end_date = datetime.date(2016, 12, 30)

        input_start_date = input_data.split(' - ')[0]
        actual_start_date = parser.parse(input_start_date).date()

        input_end_date = input_data.split(' - ')[1]
        actual_end_date = parser.parse(input_end_date).date()

        self.assertEqual(expected_start_date, actual_start_date)
        self.assertEqual(expected_end_date, actual_end_date)

    def test_parse_date_range(self):
        """
        No Abbreviation: "April 20, 2017 - April 30, 2017"
        """
        input_data = "April 20, 2017 - April 30, 2017"
        expected_start_date = datetime.date(2017, 4, 20)
        expected_end_date = datetime.date(2017, 4, 30)

        input_start_date = input_data.split(' - ')[0]
        actual_start_date = parser.parse(input_start_date).date()

        input_end_date = input_data.split(' - ')[1]
        actual_end_date = parser.parse(input_end_date).date()

        self.assertEqual(expected_start_date, actual_start_date)
        self.assertEqual(expected_end_date, actual_end_date)

    def test_parse_date_range_with_suffixed_day(self):
        """
        With  Suffix: "May 20th, 2017 - May 31st, 2017"
        """
        input_data = "May 20th, 2017 - May 31st, 2017"
        expected_start_date = datetime.date(2017, 5, 20)
        expected_end_date = datetime.date(2017, 5, 31)

        input_start_date = input_data.split(' - ')[0]
        actual_start_date = parser.parse(input_start_date).date()

        input_end_date = input_data.split(' - ')[1]
        actual_end_date = parser.parse(input_end_date).date()

        self.assertEqual(expected_start_date, actual_start_date)
        self.assertEqual(expected_end_date, actual_end_date)


if __name__ == '__main__':
    unittest.main()

from dateutil import parser


def is_date_range(date_string):
    if ' - ' in date_string:
        return True
    else:
        return False


def validate_date_string():
    pass


def parse_date_range(date_string):
    """
    :param str date_string:
    :return list:
    """
    return date_string.split(' - ')


def parse_date_string(date_string):
    if is_date_range(date_string):
        start_date, end_date = parse_date_range(date_string)
        return parser.parse(end_date).date(), parser.parse(start_date).date()
    end_date = parser.parse(date_string).date()
    return end_date,


def format_date_as_iso8601(d):
    return d.isoformat()



import icalendar
import unittest

class TestPropertyParams(unittest.TestCase):

    def test_property_params(self):
        cal_address = icalendar.vCalAddress('mailto:john.doe@example.org')
        cal_address.params["CN"] = "Doe, John"
        ical = icalendar.Calendar()
        ical.add('organizer', cal_address)

        ical_str = icalendar.Calendar.to_ical(ical)
        exp_str = """BEGIN:VCALENDAR\r\nORGANIZER;CN="Doe, John":mailto:john.doe@example.org\r\nEND:VCALENDAR\r\n"""

        self.assertEqual(ical_str, exp_str)

        raise Exception

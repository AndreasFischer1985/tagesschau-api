"""
    Tagesschau API

    Die Tagesschau ist eine Nachrichtensendung der ARD (Abkürzung für Arbeitsgemeinschaft der öffentlich-rechtlichen Rundfunkanstalten der Bundesrepublik Deutschland), die von ARD-aktuell in Hamburg produziert und mehrmals täglich ausgestrahlt wird. ARD-aktuell ist seit 1977 die zentrale Fernsehnachrichtenredaktion der ARD, bei welcher es sich wiederum um einen Rundfunkverbund handelt, der aus den Landesrundfunkanstalten und der Deutschen Welle besteht.<br>Über die hier dokumentierte API stehen auf [www.tagesschau.de](https://www.tagesschau.de) aktuelle Nachrichten und Medienbeiträge im JSON-Format zur Verfügung.<br>  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.tagesschau.api.homepage_api import HomepageApi  # noqa: E501

from deutschland import tagesschau


class TestHomepageApi(unittest.TestCase):
    """HomepageApi unit test stubs"""

    def setUp(self):
        self.api = HomepageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_homepage(self):
        """Test case for homepage

        Ausgewählte aktuelle Nachrichten und Eilmeldungen  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()

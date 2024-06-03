# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants

    The version of the OpenAPI document: 2.14.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.report_api import ReportApi


class TestReportApi(unittest.TestCase):
    """ReportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportApi()

    def tearDown(self) -> None:
        pass

    def test_report_create_settlements_report(self) -> None:
        """Test case for report_create_settlements_report

        Creates a settlement report
        """
        pass

    def test_report_get_report(self) -> None:
        """Test case for report_get_report

        Gets a settlement report
        """
        pass

    def test_report_get_status(self) -> None:
        """Test case for report_get_status

        Gets the status of a settlement report
        """
        pass


if __name__ == '__main__':
    unittest.main()

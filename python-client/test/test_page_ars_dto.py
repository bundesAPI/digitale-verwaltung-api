"""
    API zum Digitalisierungsfortschritt der öffentlichen Verwaltung

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.digitale_verwaltung.model.ars_dto import ArsDto
from deutschland.digitale_verwaltung.model.pageable_object import PageableObject
from deutschland.digitale_verwaltung.model.sort_object import SortObject

from deutschland import digitale_verwaltung

globals()["ArsDto"] = ArsDto
globals()["PageableObject"] = PageableObject
globals()["SortObject"] = SortObject
from deutschland.digitale_verwaltung.model.page_ars_dto import PageArsDto


class TestPageArsDto(unittest.TestCase):
    """PageArsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageArsDto(self):
        """Test PageArsDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PageArsDto()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()

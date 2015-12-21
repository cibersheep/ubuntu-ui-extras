# -*- coding: utf-8 -*-
#
# Copyright 2013 Canonical
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.

from __future__ import absolute_import

from testtools.matchers import Equals
from autopilot.matchers import Eventually

from ubuntu_ui_extras.browser.tests import BrowserTestCaseBase


class TestErrorSheet(BrowserTestCaseBase):

    """Tests the error message functionality."""

    def setUp(self):
    	super(TestErrorSheet, self).setUp()
    	self.open_html_page()

    def test_invalid_url_triggers_error_message(self):
        error = self.main_window.get_error_sheet()
        self.assertThat(error.visible, Equals(False))
        self.go_to_url("htpp://invalid")
        self.assertThat(error.visible, Eventually(Equals(True)))
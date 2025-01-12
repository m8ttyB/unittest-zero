#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is UnittestZero.
#
# The Initial Developer of the Original Code is
# Portions created by the Initial Developer are Copyright (C) 2011

# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Joel Andersson <janderssn@gmail.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****


class Assert:

    @classmethod
    def equal(self, first, second, msg=None):
        assert first == second, msg

    @classmethod
    def not_equal(self, first, second, msg=None):
        assert first != second, msg

    @classmethod
    def true(self, first, msg=None):
        assert first is True, msg

    @classmethod
    def false(self, first, msg=None):
        assert first is False, msg

    @classmethod
    def none(self, first, msg=None):
        assert first is None, msg

    @classmethod
    def not_none(self, first, msg=None):
        assert first is not None, msg

    @classmethod
    def fail(self, msg):
        raise AssertionError(msg)
    
    @classmethod
    def is_sorted_ascending(self, first, msg=None):
        assert all([first[i] <= first[i + 1] for i in xrange(len(first) - 1)]) is True, msg

    @classmethod
    def is_sorted_descending(self, first, msg=None):
        assert all([first[i] >= first[i + 1] for i in xrange(len(first) - 1)]) is True, msg
        
    @classmethod
    def raises(self, exception, caller, msg=None, *args, **kwargs):
        try:
            caller(*args, **kwargs )
        except exception:
            return

        if hasattr(exception,'__name__'):
            excName = exception.__name__
        else:
            excName = str(exception)
        
        raise AssertionError("%s was not raised" % excName)

    @classmethod
    def contains(self, needle, haystack):
        try:
            assert needle in haystack
        except AssertionError:
            raise AssertionError('%s not found in %s' % (needle, haystack))

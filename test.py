'''
    Copyright 2017 Farooq Karimi Zadeh <farooghkz at ompbx dot org>

    This file is part of KoranFinder.

    KoranFinder is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This software is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this software.  If not, see <http://www.gnu.org/licenses/>.

    On Debian systems you probably can find a version of GPLv3 in
    /usr/share/common-licenses/
'''

from supybot.test import *


class KoranFinderTestCase(PluginTestCase):
    plugins = ('KoranFinder',)


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

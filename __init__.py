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

"""
KoranFinder: Brings verses from Quran
"""

import supybot
import supybot.world as world

__version__ = "0.01"

__author__ = supybot.Author("Farooq Karimi Zadeh", "FarooqKZ",
        "farooghkz@openmailbox.org")

__contributors__ = { # Let's don't forget that dictionaries don't have order!
        supybot.Author("##islam channel member on Freenode"),
        supybot.Author("Antti Siponen", "lantti"),
        supybot.Author("Usama Akkad", "damascene", "uahello@gmail.com"),
        supybot.Author("Safa Alfulaij", "SafaAlfulaij",
            "safaalfulaij@hotmail.com"),
        supybot.Author("Farooq Karimi Zadeh", "FarooqKZ",
            "farooghkz@openmailbox.org")
        } 

__url__ = 'https://github.com/farooqkz/KoranFinder'

from . import config
from . import plugin
from imp import reload
# In case we're being reloaded.
reload(config)
reload(plugin)
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    from . import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

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

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('KoranFinder')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    KoranFinder = conf.registerPlugin('KoranFinder', True)
    if yn("""Split long verses?""", default=True):
        KoranFinder.splitMessages.setValue(True)
    else:
        KoranFinder.splitMessages.setValue(False)

KoranFinder = conf.registerPlugin('KoranFinder')
# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(KoranFinder, 'splitMessages',
    registry.Boolean(True, _("""Set to split long verses.""")))
conf.registerGlobalValue(KoranFinder, 'splitMessagesAt',
    registry.PositiveInteger(350, _("""Set where to split long verses.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

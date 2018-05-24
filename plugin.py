'''
    Copyright 2017-2018 Farooq Karimi Zadeh <farooghkarimizadeh@gmail.com>

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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from . import pygq
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('KoranFinder')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

# Set languages and translations the bot will accept
quranID = {"ar" : "quran-simple", "en" : "en.sahih", "tr" : "tr.yazir", "fa" : "fa.fooladvand"}

API_TOKEN = ""

class utilities():
    def arg2list(ayat): # TODO: better name for this function
        MAX_AYAT = 6
        ayat = ayat.split(",")
        ayat_l = []
        for aya in ayat:
            if aya.isdigit():
                ayat_l += [int(aya)]
            else:
                t = aya.split('-') 
                start, end = int(t[0]), int(t[1])
                ayat_l += list(range(start, end + 1))

        if len(ayat_l) > MAX_AYAT:
            raise ValueError("Sorry, you can get just " + str(MAX_AYAT) +
                    " ayat each time calling me.")
        else:
            return ayat_l

class KoranFinder(callbacks.Plugin):
    """This plugin gets verse and ayah number and sends you the ayah using a web API."""
    threaded = True

    def __init__(self, irc):
         self.__parent = super(KoranFinder, self)
         self.__parent.__init__(irc)
         self.PyGQ = pygq.PyGQ(token = API_TOKEN, lg_codes=quranID)

    def koran(self, irc, msg, args, surah, ayat, lang):
        """<surah> <ayah/ayat> <lang>

        returns ayah number <ayah> of surah number <surah> in <lang> language or translation or tafsir. for more information visit: https://git.io/vwMz9
        """
        
        try:
            list_of_ayat = utilities.arg2list(ayat)
        except ValueError as e:
            irc.error(str(e))
            return

        try:
            ayat_list = []
            for ayah in list_of_ayat:
                verse_json = self.PyGQ.getAyah(surah, ayah, lang)
                ayat_list.append(str(verse_json["surah"]) + ":" +
                                str(verse_json["ayah"]) + ", " +
                                str(verse_json["verse"]))
        except ValueError as e:
            irc.error(str(e))
            return
        except (KeyError, TypeError) as e: #TypeError incase requesting a audio version. The json would contain a list so qdata would raise a TypeError
            irc.error("Wrong translation code or broken API.") 
            return
        for ayah in ayat_list:

            if self.registryValue('splitMessages'):
                ircMsgBytes = ayah.encode('utf-8')
                while len(ircMsgBytes) > 350:
                    splitPoint = ircMsgBytes[0:351].rfind(' '.encode('utf-8'))
                    irc.reply(ircMsgBytes[0:splitPoint].decode('utf-8').strip())
                    ircMsgBytes = ircMsgBytes[splitPoint:]
                irc.reply(ircMsgBytes.decode('utf-8').strip())
            else:
                irc.reply(ayah)

    koran = wrap(koran, ["int", "something", optional("something", "en")])

Class = KoranFinder
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

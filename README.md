KoranFinder
============

KoranFinder is a fork of
[QuranFinder](https://github.com/SafaAlfulaij/QuranFinder) which is a Limnoria
plugin to get Quran verses using Global Quran API.

## History
It was first time developed by a ##islam channel member on freenode. a few days
later it was
moved to Github. Now that I check the first commit was Mar 27, 2016. After about 2 years I forked it and changed its name to `KoranFinder` so
I can maintain it myself(it seems they don't have much time maintaining this).

## Usage

```
Mybot: quran <surah> <ayah/ayat> [lang]
```
returns ayah number \<ayah\> of surah number \<surah\> in \<lang\> language.
By default, `lang` is `en` which refers to English.
To get just one ayah you should go like this:

```
Mybot: quran 1 1 en
```
Which returns 
```
1,1: Praise be to Allah, Lord of the Worlds,
```
You could also get more than one ayah, like:
```
Mybot: quran 1 1-3
Mybot: quran 1 1,2,4
```
Which returns ayat 1 to 3 from surah 1 and ayat 1,2,4 from surah 1.
You can also combine them:
```
Mybot: quran 1 1-3,5
```
Which returns ayat 1 to 3 and also 5 from surah 1.

The bot can obtain translation of the Quran for different languages. (ar, en, fa, tr) are the main ones. You can get extra translations and other data sources by using the data source key provided by Global Quran API. For more information see the [Wiki](https://github.com/SafaAlfulaij/QuranFinder/wiki)

For example
```
Mybot: quran 1 1 en.hilali
```
provides the Hilali English translation of the Quran.

## Licence
This program is free software under GNU General Public License 3 or any later version and COMES WITHOUT ANY WARRANTY, for more information see LICENCE.

## To-Do
- [ ] Don't send a message for each ayah and split messages, instead use supybot's more(works for English but not Arabic)
- [ ] Use config.py for the maximum difference between two verses which by default is 5.

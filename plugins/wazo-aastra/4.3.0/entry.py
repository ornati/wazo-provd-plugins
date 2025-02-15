# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

common = {}
execfile_('common.py', common)


MODEL_VERSIONS = {
    '6863i': '4.3.0.2036',
    '6865i': '4.3.0.2036',
    '6867i': '4.3.0.2036',
    '6869i': '4.3.0.2036',
    '6873i': '4.3.0.2036',
}


class AastraPlugin(common['BaseAastraPlugin']):
    IS_PLUGIN = True
    _LANGUAGE_PATH = 'Aastra/i18n/'

    pg_associator = common['BaseAastraPgAssociator'](MODEL_VERSIONS)

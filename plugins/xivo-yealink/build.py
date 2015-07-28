# -*- coding: utf-8 -*-

# Copyright (C) 2013-2014 Avencall
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

# Depends on the following external programs:
#  -rsync

from subprocess import check_call


@target('2015-03', 'xivo-yealink-2015-03')
def build_2015_03(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '2015-03/', path])


@target('25.73.0.20', 'xivo-yealink-25.73.0.20')
def build_25_73_0_20(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '25.73.0.20/', path])


@target('70.0', 'xivo-yealink-70.0')
def build_70_0(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '70.0/', path])


@target('72.0', 'xivo-yealink-72.0')
def build_72_0(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '72.0/', path])


@target('v80', 'xivo-yealink-v80')
def build_v80(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--exclude', '/templates',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                'v80/', path])

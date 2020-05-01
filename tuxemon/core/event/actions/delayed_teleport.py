# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tuxemon.core.euclid import Vector3
from tuxemon.core.event.eventaction import EventAction


class DelayedTeleportAction(EventAction):
    """ Set teleport information.  Teleport will be triggered during screen transition

    Only use this if followed by a transition
    """
    name = "delayed_teleport"
    valid_parameters = [
        (str, "map_name"),
        (int, "position_x"),
        (int, "position_y")
    ]

    def start(self):
        position = Vector3(self.parameters.x, self.parameters.y, 0)
        self.session.client.release_controls()
        self.session.world.teleport(self.session.player, self.parameters.map_name, position)

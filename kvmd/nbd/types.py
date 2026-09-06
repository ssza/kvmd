# ========================================================================== #
#                                                                            #
#    KVMD - The main PiKVM daemon.                                           #
#                                                                            #
#    Copyright (C) 2020  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


import dataclasses


# =====
@dataclasses.dataclass(frozen=True)
class NbdImage:
    url:    str
    proto:  str
    name:   str
    size:   int
    mod_ts: float
    rw:     bool


# =====
class BaseNbdEvent:
    pass


@dataclasses.dataclass(frozen=True)
class NbdStartingEvent(BaseNbdEvent):
    image: NbdImage


@dataclasses.dataclass(frozen=True)
class NbdRunningEvent(BaseNbdEvent):
    online: bool
    msg:    str


@dataclasses.dataclass(frozen=True)
class NbdStoppedEvent(BaseNbdEvent):
    src: str
    msg: str
    ok:  bool


# =====
@dataclasses.dataclass(frozen=True)
class NbdState:
    device:  str
    image:   (NbdImage | None) = dataclasses.field(default=None)
    status:  (str | None) = dataclasses.field(default=None)
    info:    (NbdRunningEvent | NbdStoppedEvent | None) = dataclasses.field(default=None)

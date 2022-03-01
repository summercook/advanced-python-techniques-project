"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self.designation = str(info.get('pdes')) if info['pdes'] else None

        self.name = str(info.get('name')) if info['name'] else None

        self.diameter = float(info.get('diameter')) if info['diameter'] else float('nan')

        self.hazardous = info.get('pha') == 'Y'

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    def serialize(self):
        """To serialize an object.
        :return: serialized object of NearEarth
        """
        return {'designation': self.designation,
                'name': self.name,
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f'{self.designation} ({self.name})'
        else:
            return f'{self.designation}'

    def __str__(self):
        """Return `str(self)`."""
        if self.hazardous is True:
            return f"A NearEarthObject {self.fullname} has a diameter of {self.diameter} " \
                   "and is potentially hazardous."
        else:
            return f"A NearEarthObject {self.fullname} has a diameter of {self.diameter} and " \
                   "is not potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self._designation = str(info.get('des')) if info['des'] else ''

        self.time = cd_to_datetime(info.get('cd')) if info['cd'] else None

        self.distance = float(info.get('dist')) if info['dist'] else float('nan')

        self.velocity = float(info.get('v_rel')) if info['v_rel'] else float('nan')

        # Create an attribute for the referenced NEO.
        self.neo = self._designation

        def serialize(self):
            """To serialize an object.
            :return: serialized object of CloseApproach
            """
            return {'datetime_utc': datetime_to_str(self.time),
                    'distance_au': self.distance,
                    'velocity_km_s': self.velocity}

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        self.str_time = datetime_to_str(self.time)
        return self.str_time

    def __str__(self):
        """Return `str(self)`."""
        return f"A CloseApproach {self.neo.fullname} occurred on {self.time_str} at a " \
               f"distance of {self.distance}, at a velocity of {self.velocity}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

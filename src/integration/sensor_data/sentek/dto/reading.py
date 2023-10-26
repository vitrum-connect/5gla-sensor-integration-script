from dataclasses import dataclass


@dataclass
class Reading:
    """A class representing a reading.

    Attributes:
        dateTime (str): The date and time of the reading in ISO 8601 format.
        v1 (float): The value 1.
        v2 (float): The value 2.
        a1 (float): The value of a1.
        t1 (float): The value of t1.
        a2 (float): The value of a2.
        t2 (float): The value of t2.
        a3 (float): The value of a3.
        t3 (float): The value of t3.
        a4 (float): The value of a4.
        t4 (float): The value of t4.
        a5 (float): The value of a5.
        t5 (float): The value of t5.
        a6 (float): The value of a6.
        t6 (float): The value of t6.
        a7 (float): The value of a7.
        t7 (float): The value of t7.
        a8 (float): The value of a8.
        t8 (float): The value of t8.
        a9 (float): The value of a9.
        t9 (float): The value of t9.
    """
    dateTime: str
    v1: float
    v2: float
    a1: float
    t1: float
    a2: float
    t2: float
    a3: float
    t3: float
    a4: float
    t4: float
    a5: float
    t5: float
    a6: float
    t6: float
    a7: float
    t7: float
    a8: float
    t8: float
    a9: float
    t9: float

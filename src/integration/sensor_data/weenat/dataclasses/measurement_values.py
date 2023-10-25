from dataclasses import dataclass


@dataclass
class MeasurementValues:
    """
    The MeasurementValues class represents a collection of various measurement values. Each instance of MeasurementValues contains the following attributes:

    Attributes:
        t (float): Temperature value
        u (float): Wind speed value
        rr (float): Rainfall rate value
        ff (float): Wind gust speed value
        fxy (float): Wind speed in x and y direction value
        t_15 (float): Temperature at 15 cm depth value
        t_30 (float): Temperature at 30 cm depth value
        t_60 (float): Temperature at 60 cm depth value
        whyd_15 (float): Soil water content at 15 cm depth value
        whyd_30 (float): Soil water content at 30 cm depth value
        whyd_60 (float): Soil water content at 60 cm depth value
        t_dry (float): Dry bulb temperature value
        t_wet (float): Wet bulb temperature value
        lw_dry (float): Dry bulb leaf wetness value
        lw_v (float): Vapour pressure deficit value
        t_soil (float): Soil temperature value
        ssi (float): Soil suction index value
        ssi_min (float): Minimum soil suction index value
        ssi_max (float): Maximum soil suction index value
        ppfd (float): Photosynthetic photon flux density value
        ppfd_min (float): Minimum photosynthetic photon flux density value
        ppfd_max (float): Maximum photosynthetic photon flux density value
        t_dew (float): Dew point temperature value
        etp (float): Potential evapotranspiration value

    """
    t: float
    u: float
    rr: float
    ff: float
    fxy: float
    t_15: float
    t_30: float
    t_60: float
    whyd_15: float
    whyd_30: float
    whyd_60: float
    t_dry: float
    t_wet: float
    lw_dry: float
    lw_v: float
    t_soil: float
    ssi: float
    ssi_min: float
    ssi_max: float
    ppfd: float
    ppfd_min: float
    ppfd_max: float
    t_dew: float
    etp: float

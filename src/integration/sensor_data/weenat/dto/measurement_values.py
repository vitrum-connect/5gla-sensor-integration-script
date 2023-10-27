from dataclasses import dataclass


@dataclass
class MeasurementValues:
    """
    The MeasurementValues class represents a collection of various measurement values. Each instance of MeasurementValues contains the following attributes:

    Attributes:
        T (float): Temperature value
        U (float): Wind speed value
        RR (float): Rainfall rate value
        FF (float): Wind gust speed value
        FXY (float): Wind speed in x and y direction value
        T_15 (float): Temperature at 15 cm depth value
        T_30 (float): Temperature at 30 cm depth value
        T_60 (float): Temperature at 60 cm depth value
        WHYD_15 (float): Soil water content at 15 cm depth value
        WHYD_30 (float): Soil water content at 30 cm depth value
        WHYD_60 (float): Soil water content at 60 cm depth value
        T_DRY (float): Dry bulb temperature value
        T_WET (float): Wet bulb temperature value
        LW_DRY (float): Dry bulb leaf wetness value
        LW_V (float): Vapour pressure deficit value
        T_SOIL (float): Soil temperature value
        SSI (float): Soil suction index value
        SSI_MIN (float): Minimum soil suction index value
        SSI_MAX (float): Maximum soil suction index value
        PPFD (float): Photosynthetic photon flux density value
        PPFD_MIN (float): Minimum photosynthetic photon flux density value
        PPFD_MAX (float): Maximum photosynthetic photon flux density value
        T_DEW (float): Dew point temperature value
        ETP (float): Potential evapotranspiration value

    """
    T: float
    U: float
    RR: float
    FF: float
    FXY: float
    T_15: float
    T_30: float
    T_60: float
    WHYD_15: float
    WHYD_30: float
    WHYD_60: float
    T_DRY: float
    T_WET: float
    LW_DRY: float
    LW_V: float
    T_SOIL: float
    SSI: float
    SSI_MIN: float
    SSI_MAX: float
    PPFD: float
    PPFD_MIN: float
    PPFD_MAX: float
    T_DEW: float
    ETP: float

from typing import Optional
from pydantic import BaseModel

class Signal(BaseModel):
    symbol: str
    price: Optional[float] = None
    rule: Optional[str] = None
    first30Green: Optional[bool] = None
    volumeStrong: Optional[bool] = None
    BTC: Optional[float] = None
    GOLD: Optional[float] = None
    date: Optional[str] = None

class TVAlert(BaseModel):
    ticker: Optional[str] = None
    price: Optional[float] = None
    close: Optional[float] = None
    rule: Optional[str] = None
    BTC: Optional[float] = None
    GOLD: Optional[float] = None
    volumeStrong: Optional[bool] = None
    first30Green: Optional[bool] = None
    date: Optional[str] = None
    secret: Optional[str] = None

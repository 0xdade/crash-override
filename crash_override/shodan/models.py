from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class ShodanHostResponse:
    city: str | None
    region_code: str | None
    os: str | None
    tags: list[str]
    ip: int
    isp: str
    area_code: str | None
    longitude: Decimal
    last_update: datetime
    ports: list[int]
    latitude: Decimal
    hostnames: list[str]
    country_code: str
    country_name: str
    domains: list[str]
    org: str
    data: list[str]
    asn: str
    ip_str: str

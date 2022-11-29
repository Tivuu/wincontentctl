

from pydantic import BaseModel, validator, ValidationError

from splunk_contentctl.objects.unit_test_attack_data import UnitTestAttackData
from splunk_contentctl.objects.unit_test_baseline import UnitTestBaseline

class UnitTestTest(BaseModel):
    name: str
    file: str
    pass_condition: str
    earliest_time: str = None
    latest_time: str = None
    baselines: list[UnitTestBaseline] = None
    attack_data: list[UnitTestAttackData]
from pydantic import BaseModel, ConfigDict


class BaseVectorModel(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_default=True, from_attributes=True, validate_assignment=True)

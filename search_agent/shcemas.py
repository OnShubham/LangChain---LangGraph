from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    
    url: str = Field(descriptopm = "The URL of the source")
    


class AgentResponse(BaseModel):
    
    
    answer : str = Field(descption="the agent answer to the query")
    
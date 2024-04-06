from typing import Annotated
from fastapi import Depends
from configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

DataBaseDependency = Annotated[AsyncSession, Depends(get_session)]

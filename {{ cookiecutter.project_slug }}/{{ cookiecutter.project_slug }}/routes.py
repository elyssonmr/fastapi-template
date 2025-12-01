import logging
from http import HTTPStatus

from fastapi import APIRouter

# from {{ cookiecutter.project_slug }}.schemas import ASCHEMA
# from {{ cookiecutter.project_slug }}.services import ASERVICE

logger = logging.getLogger()

router = APIRouter(prefix='/YOUR_PREFIX', tags=['SWAGGER PREFIX'])


@router.post('/YOUR_URL', status_code=HTTPStatus.CREATED)
async def endpoint_name():
    # Here goes the endpoint code
    pass

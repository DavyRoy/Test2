from django.http import QueryDict
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request


def get_token_from_request(request: Request) -> str:
    token_header = request.headers.get('Authorization', None)

    if token_header is not None:
        token = token_header.split(' ')[1]

        return token
    else:
        raise ValidationError('Token Header is empty')


def reveal_query_params(query_params: QueryDict):

    reveal_params = {key: value for key, value in query_params.items() if value != ''}

    return reveal_params

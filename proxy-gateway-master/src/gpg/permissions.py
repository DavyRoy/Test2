import jwt
from django.conf import settings
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from gpg.utils import get_token_from_request


class IsUserApiAuthenticated(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request: Request, view) -> bool:
        has_permission = False
        salt = settings.USER_API_SALT

        try:
            token = get_token_from_request(request)

            payload = jwt.decode(jwt=token, key=salt, algorithms="HS256")
            user_id = payload.get('user_id', None)
            if user_id is not None:
                match request.method:
                    case 'POST':
                        request.data['created_by'] = user_id

                    case 'PATCH':
                        request.data['updated_by'] = user_id

                    case _:
                        pass

                has_permission = payload is not None
        except:
            pass

        return has_permission

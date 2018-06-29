from user_auth.serializers import UserAuthSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserAuthSerializer(user).data
    }

from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema


class SignUpSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="username",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'username' user username min = 10, max = 50"
                    ),
                ),
                coreapi.Field(
                    name="nickname",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'username' user nickname min = 10, max = 60"
                    ),
                ),
                coreapi.Field(
                    name="image_file",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="file - 'image_file' user photo"
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'password' user password min = 8, max = 40"
                    ),
                ),
            ]
            return self._manual_fields + api_fields


class SignInSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="username",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'username' user username min = 10, max = 50"
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'password' user password min = 8, max = 40"
                    ),
                ),
            ]
            return self._manual_fields + api_fields
from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema


class GlobalSearchSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="promt",
                    required=False,
                    location="form",
                    schema=coreschema.String(
                        description="str - 'en_name or ru_name manga'"
                    ),
                ),
            ]
            return self._manual_fields + api_fields
from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema


class MangaListShema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="type",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'type' Filter by manga type"
                    ),
                ),
                coreapi.Field(
                    name="genre__title",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="str - 'genre__title' Filter by manga genre"
                    ),
                ),
                coreapi.Field(
                    name="min_issue_year",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="Filter by issue year value 'from'"
                    )
                ),
                                coreapi.Field(
                    name="max_issue_year",
                    required=False,
                    location="query",
                    schema=coreschema.String(
                        description="Filter by issue year value 'before'"
                    )
                )
            ]
            return self._manual_fields + api_fields


class MangaDetailShema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="slug",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="slug - 'slug field'"
                    ),
                ),
            ]
            return self._manual_fields + api_fields


class MangaCommentSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "POST":
            api_fields = [
                coreapi.Field(
                    name="slug",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="slug - 'slug field'"
                    ),
                ),
                coreapi.Field(
                    name="text",
                    required=False,
                    location="form",
                    schema=coreschema.String(description="str - 'text'"),
                ),
            ]
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="slug",
                    required=False,
                    location="path",
                    schema=coreschema.String(
                        description="slug - 'slug field'"
                    ),
                ),
            ]
            return self._manual_fields + api_fields
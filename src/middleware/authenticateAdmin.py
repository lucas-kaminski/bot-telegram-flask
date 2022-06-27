from flask import request, Response

from database.queries.adm_users import selectAdmUser


def authenticateAdmin():
    print(request.endpoint)
    if request.endpoint == "new_coin" or request.endpoint == "new_message":
        auth_header = request.headers.get("Authorization")

        if auth_header is None:
            return Response("Missing Authorization Header", status=401)

        id = auth_header.split(":")[0]
        pwd = auth_header.split(":")[1]

        if not auth_header:
            print("No auth header")
            return Response("No auth header")

        adm_user = selectAdmUser(id=id)

        if not adm_user:
            print("No adm user")
            return Response("No user", status=401)

        if adm_user["COUNTERSIGN"].decode() != pwd:
            return Response("Invalid credentials")
        else:
            request.args = {"adm_user": adm_user}

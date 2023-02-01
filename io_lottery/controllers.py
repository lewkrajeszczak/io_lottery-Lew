from dataclasses import dataclass


@dataclass
class AddUserRequest:
    json: dict


class AddUserController:
    def add(self, request: AddUserRequest) -> None:
        print(request.json)
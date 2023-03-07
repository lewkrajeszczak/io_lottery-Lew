from dataclasses import dataclass

from io_lottery.repositories import UserRepository


@dataclass
class AddUserRequest:
    json: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add()
        print(request.json)


class GetUserController:
    def get(self, id: int):
        raise NotImplementedError

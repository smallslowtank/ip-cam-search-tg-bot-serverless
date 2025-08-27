from core.entities import CreateUser


from database.repositories.camera import camera_repository_factory
from database.repositories.user import user_repository_factory
from database.uow import unit_of_work


class CameraService:

    def __init__(self, repository_factory):
        self.camera_repository_factory = repository_factory

    async def get_result(self, user: CreateUser) -> list:
        """
        выполнить запрос и получит результат
        """
        async with unit_of_work() as uow:
            camera_repository = self.camera_repository_factory(uow.session)
            list_of_cameras = await camera_repository.get_result(user=user)
            if len(list_of_cameras) != 0:
                cameras = []
                for i in list_of_cameras:
                    cameras.append(i)
                return cameras
            else:
                return ["Список пуст"]


class UserService:

    def __init__(self, repository_factory):
        self.user_repository_factory = repository_factory

    async def check_by_id(self, user_id: int) -> bool:
        """
        Проверить существование пользователя в базе,
        """
        async with unit_of_work() as uow:
            user_repository = self.user_repository_factory(uow.session)
            if await user_repository.get_by_id(user_id=user_id) == None:
                return False
            return True

    async def add(self, user_info: CreateUser) -> bool:
        """
        Добавить пользователя в базу
        """
        async with unit_of_work() as uow:
            user_repository = self.user_repository_factory(uow.session)
            if await user_repository.add(user_info=user_info):
                return True
            return False

    async def get_by_id(self, user_id: int) -> CreateUser:
        """
        Получить параметры для запроса
        """
        async with unit_of_work() as uow:
            user_repository = self.user_repository_factory(uow.session)
            user = await user_repository.get_by_id(user_id=user_id)
            return user

    async def update(self, user: CreateUser) -> bool:
        """
        Обновить в базе данных информацию о пользователе
        """
        async with unit_of_work() as uow:
            user_repository = self.user_repository_factory(uow.session)
            if await user_repository.update(user_info=user):
                return True
            return False


user_service = UserService(user_repository_factory)
camera_service = CameraService(camera_repository_factory)

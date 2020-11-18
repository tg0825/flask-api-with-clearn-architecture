import inject

from app.repositories.orm.orm_repository import BoardRepository


def bind(binder, app):
    binder.bind_to_constructor(
        BoardRepository, lambda: BoardRepository()
    )


def init_provider(app):
    inject.clear_and_configure(lambda binder: bind(binder, app))
from behave import given, when, then
from app import DatabaseManager, SimpleUI


@given('база данных пустая')
def step_db_empty(context):
    context.db = DatabaseManager(":memory:")
    context.ui = SimpleUI()
    context.ui.db = context.db


@given('в базе есть {count:d} записи')
def step_db_has_records(context, count):
    context.db = DatabaseManager(":memory:")
    context.ui = SimpleUI()
    context.ui.db = context.db

    for i in range(count):
        context.db.add_record(f"Имя{i}", f"test{i}@mail.ru")


@given('в базе есть запись')
def step_db_has_record(context):
    context.db = DatabaseManager(":memory:")
    context.ui = SimpleUI()
    context.ui.db = context.db
    context.db.add_record("Тест", "test@mail.ru")


@when('я добавляю запись "{name}" "{email}"')
def step_add_record(context, name, email):
    context.result = context.ui.add_record(name, email)


@when('я смотрю все записи')
def step_view_records(context):
    context.records = context.ui.show_records()


@when('я удаляю запись {record_id:d}')
def step_delete_record(context, record_id):
    context.result = context.db.delete_record(record_id)


@then('запись должна сохраниться')
def step_record_saved(context):
    assert context.result == True


@then('я вижу сообщение "{message}"')
def step_see_message(context, message):
    assert context.ui.get_message() == message


@then('я вижу {count:d} записи')
def step_see_records(context, count):
    assert len(context.records) == count


@then('запись удаляется')
def step_record_deleted(context):
    assert context.result == True

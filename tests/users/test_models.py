from api.users.models import Users


def test_create_user(db):
    user = Users(
        password="test",
        email="test@email.com",
        created_at="2021-01-01",
        updated_at="2021-01-01",
        first_name="test",
        last_name="test",
    )
    with db() as session:
        session.add(user)
        session.commit()
        assert user.id == 1
        assert user.password == "test"
        assert user.email == "test@email.com"
        assert user.created_at == "2021-01-01"
        assert user.updated_at == "2021-01-01"
        assert user.first_name == "test"
        assert user.last_name == "test"


def test_list_users(db):
    user = Users(
        password="test",
        email="teste2@email.com",
        created_at="2021-01-01",
        updated_at="2021-01-01",
        first_name="test",
        last_name="test",
    )
    with db() as session:
        session.add(user)
        session.commit()
        fetched_user = session.query(Users).filter_by(id=user.id).first()
        assert fetched_user is not None
        assert fetched_user.id == 2
        assert fetched_user.password == "test"
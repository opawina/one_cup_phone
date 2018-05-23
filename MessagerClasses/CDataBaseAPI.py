from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, \
    create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

from config import DATABASE


DBase = declarative_base()

class TUsers(DBase):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    login = Column(Unicode())
    date = Column(Unicode())
    host = Column(Unicode())

    check_1 = UniqueConstraint("login")


class TPassw(DBase):
    __tablename__ = "passw"

    id = Column(Integer(), ForeignKey("users.id"), primary_key=True)
    passw = Column(Unicode())

    check_1 = UniqueConstraint("id")

    fk_id_user = relationship("TUsers", foreign_keys=[id])


class THistory(DBase):

    __tablename__ = "users_history"

    id = Column(Integer(), primary_key=True)
    id_user = Column(Integer(), ForeignKey("users.id"))
    message = Column(Unicode())
    date = Column(Unicode())
    id_chat = Column(Integer)

    fk_id_user = relationship("TUsers", foreign_keys=[id_user])


class TListContact(DBase):

    __tablename__ = "users_list_contacts"

    id = Column(Integer(), primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_contact = Column(Integer, ForeignKey("users.id"))

    check_1 = UniqueConstraint("id_user", "id_contact")

    fk_id_user = relationship("TUsers", foreign_keys=[id_user])
    fk_id_contact = relationship("TUsers", foreign_keys=[id_contact])



    # def __repr__(self):
    #     # возвращаем id собеседников
    #     return str(self.id_contact)



class DataBaseAPI():

    def __init__(self):

        # self.id_user = id_user
        engine = create_engine('sqlite:///{}'.format(DATABASE.DB_NAME))
        self.session = sessionmaker(bind=engine)()


    def add_new_user(self, login, host, passw):

        # добавление нового юзера в БД

        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_user = TUsers(login=login, date=date_now, host=host)
        self.session.add(new_user)
        self.session.flush()
        uid = new_user.id
        print(uid, 22222)

        new_p = TPassw(id=uid, passw=passw)
        self.session.add(new_p)

        self.session.commit()


    def authorization_user(self, login, passw):

        # проверяю наличие юзера в БД

        passw_ = self.session.query(TUsers).filter(
            TUsers.login=login).filter(TUsers.id==TPassw.id).first()

        return True if passw == passw_ else False


    def add_history_fact(self, id_user, msg, id_chat):

        # добавляем факт истории

        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        insert_new_fact = THistory(id_user=id_user, message=msg, date=date_now,
                                   id_chat=id_chat)
        self.session.add(insert_new_fact)
        self.session.commit()


    def get_user_list_contacts(self, id_user):

        # получаю весь список контактов

        user_list_contacts = self.session.query(TUsers).filter(
            TListContact.id_user==id_user).filter(
            TListContact.id_contact==TUsers.id).all()

        return [item.login for item in user_list_contacts]


    def add_user_to_list_contacts(self, id_user, id_contact):

        # Добавляем юзера в список контактов

        new_contact = TListContact(id_user=id_user, id_contact=id_contact)
        self.session.add(new_contact)
        self.session.commit()


    def delete_user_from_list_contacts(self, id_user, id_contact):

        # удаляю юзера из списка контактов

        self.session.query(TListContact).filter_by(id_user=id_user,
                                              id_contact=id_contact).delete()
        self.session.commit()


a = DataBaseAPI()
# a.



from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, \
    create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import datetime


DBase = declarative_base()

class TUsers(DBase):

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    login = Column(Unicode())
    date = Column(Unicode())
    host = Column(Unicode())

    check_1 = UniqueConstraint('login')


class THistory(DBase):

    __tablename__ = 'users_history'

    id = Column(Integer(), primary_key=True)
    id_user = Column(Integer(), ForeignKey('users.id'))
    message = Column(Unicode())
    date = Column(Unicode())
    id_chat = Column(Integer)

    fk_id_user = relationship('TUsers', foreign_keys=[id_user])


class TListContact(DBase):

    __tablename__ = 'users_list_contacts'

    id = Column(Integer(), primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_contact = Column(Integer, ForeignKey('users.id'))

    check_1 = UniqueConstraint('id_user', 'id_contact')

    fk_id_user = relationship('TUsers', foreign_keys=[id_user])
    fk_id_contact = relationship('TUsers', foreign_keys=[id_contact])


    # def __repr__(self):
    #     # возвращаем id собеседников
    #     return str(self.id_contact)



engine = create_engine("sqlite:///twocups.db")
session = sessionmaker(bind=engine)()

# шаблоны типовых операций

# # добавление нового юзера в БД
# login = 'qweqwe231'
# date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# host = '133.15.157.12:12674'
#
# insert_new_user = TUsers(login=login, date=date_now, host=host)
# session.add(insert_new_user)

# проверяю наличие юзера в БД
# user = session.query(TUsers).filter_by(login=login).first()
# print(user)

# # добавляем факт истории
# id_user = 4
# message = 'Hello 123'
# date = 'date_of_sending_from_client'
# id_chat = 121
#
# insert_new_fact = THistory(id_user=id_user, message=message, date=date,
#                            id_chat=id_chat)
# session.add(insert_new_fact)

# # Добавляем юзера в список контактов
id_user = 2
id_contact = 5

# insert_new_contact = TListContact(id_user=id_user, id_contact=id_contact)
# session.add(insert_new_contact)
#
# # удаляю юзера из списка контактов
# session.query(TListContact).filter_by(id_user=id_user,
#                                       id_contact=id_contact).delete()
#
# получаю весь список контактов
# КАК ДЕЛАЬ JOIN????????????
user_list_contacts = session.query(TListContact, TUsers).filter(
    TListContact.id_user==id_user).filter(
    TListContact.id_contact==TUsers.id).all()
print(user_list_contacts)

session.commit()

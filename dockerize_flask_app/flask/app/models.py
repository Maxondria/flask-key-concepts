from app import db

# ONE-TO-MANY / MANY TO ONE


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')  # one-to-many


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    # OR Many-to-one
    # owner = db.relationship('Person', backref='pets')
    # person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


'''
person = Person()
person.pets = [List of all pets where person_id = person.id]

pet = Pet()
pet.owner = data in person where id = pet.person_id
'''

# ONE-TO-ONE

'''
'uselist' stresses that this should be a one-to-one relationship
'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    profile = db.relationship('Profile', backref='user', userlist=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)


# MANY TO MANY
subscriptions_table = db.Table('subscriptions',
                               db.Column('sub_id', db.Integer,
                                         db.ForeignKey('subscriber.sub_id')),
                               db.Column('chan_id', db.Integer,
                                         db.ForeignKey('channel.chan_id'))
                               )


class Subscriber(db.Model):
    sub_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    # Many to Many relationship here now
    subscriptions = db.relationship(
        'Channel', secondary='subscriptions_table', backref=db.backref('subscribers'), lazy='dynamic')
    # Subscriber.subscriptions = [all channels]
    # To add channels to user:

    #       Let's say:
    #           user1 = Subscriber('Max')
    #           channel1 = Channel('Traversy Media')
    #           channel1.subscribers.append(user1)
    #           channel1.save() - save is a third party method of course


class Channel(db.Model):
    chan_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    # for user in Channel.subscribers:
    #     print(user.sub_id, user.name)

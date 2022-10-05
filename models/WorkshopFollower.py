class WorkshopFollower(object):
    def __init__(self, id, name, email, createdAt):
        self._id = id
        self._name = name
        self._email = email
        self._created_at = createdAt

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_created_at(self):
        return self._created_at

    def to_json(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'email': self.get_email(),
            'createdAt': self.get_created_at()
        }
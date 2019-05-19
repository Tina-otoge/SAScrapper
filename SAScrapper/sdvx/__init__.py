class SkillCourse:
    def __init__(self):
        self.name = None
        self.dai = None
        self.charts = []

    def __str__(self):
        return '{0.name} ({0.dai}): {0.charts}'.format(self)

    def __repr__(self):
        return self.__str__()

class Chart:
    def __init__(self):
        self.song_title = None
        self.level = None
        self.difficulty = None

    def __str__(self):
        return '{0.song_title} [{0.difficulty} {0.level}]'.format(self)

    def __repr__(self):
        return self.__str__()

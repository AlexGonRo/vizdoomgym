from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomHealthGathering(VizdoomEnv):

    def __init__(self, version):
        if version==1:
            super(VizdoomHealthGathering, self).__init__(10)
        else:
            super(VizdoomHealthGathering, self).__init__(4)

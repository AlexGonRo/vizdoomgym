from vizdoomgym.envs.vizdoomenv import VizdoomEnv


class VizdoomHealthGatheringSupreme(VizdoomEnv):

    def __init__(self, version):
        if version == 2:
            super(VizdoomHealthGatheringSupreme, self).__init__(11)
        elif version == 3:
            super(VizdoomHealthGatheringSupreme, self).__init__(12)
        else: # version 0
            super(VizdoomHealthGatheringSupreme, self).__init__(9)

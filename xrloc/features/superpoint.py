import sys
import torch.nn as nn

from xrloc.utils.miscs import get_parent_dir

sys.path.append(get_parent_dir(__file__) + '/../3rdparty')
from SuperGluePretrainedNetwork.models.superpoint import SuperPoint as SP


class SuperPoint(nn.Module):
    default_config = {
        'descriptor_dim': 256,
        'nms_radius': 4,
        'keypoint_threshold': 0.005,
        'max_keypoints': -1,
        'remove_borders': 4,
    }

    def __init__(self, config=default_config):
        super().__init__()
        self.config = {**self.default_config, **config}
        self.model = SP(self.config)

    def forward(self, image):
        input = {'image': image}
        return self.model(input)
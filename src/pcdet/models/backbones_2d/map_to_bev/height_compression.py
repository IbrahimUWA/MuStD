import torch.nn as nn
import numpy as np
from pcdet.datasets.augmentor.X_transform import X_TRANS
import torch

class HeightCompression(nn.Module):
    def __init__(self, model_cfg,  voxel_size=None, point_cloud_range=None):
        super().__init__()
        self.model_cfg = model_cfg
        self.num_bev_features = self.model_cfg.NUM_BEV_FEATURES
        self.x_trans = X_TRANS()
        self.point_cloud_range = point_cloud_range
        self.voxel_size=voxel_size

    def forward(self, batch_dict):
        """
        Args:
            batch_dict:
                encoded_spconv_tensor: sparse tensor
        Returns:
            batch_dict:
                spatial_features:

        """
        # print(batch_dict.keys(), "Before input to the network")

        # print(batch_dict['encoded_spconv_tensor'].features.shape,"encoded_spconv_tensor")

        batch_dict['spatial_features_stride'] = batch_dict['encoded_spconv_tensor_stride']

        encoded_spconv_tensor = batch_dict['encoded_spconv_tensor']
        spatial_features = encoded_spconv_tensor.dense()
        # print(spatial_features.shape, "Before spatial_features")
        N, C, D, H, W = spatial_features.shape
        spatial_features = spatial_features.view(N, C * D, H, W)
        # print(spatial_features.shape, "spatial_features1")

        pillarfeatures = batch_dict['pillarfeatures']
        # print(pillarfeatures.shape,"Pillarrrrrr features")
        spatial_features = torch.cat([spatial_features, pillarfeatures],1)


        batch_dict['spatial_features'] = spatial_features



        return batch_dict

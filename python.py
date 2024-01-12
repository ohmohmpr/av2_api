# import pyarrow.feather as feather
import av2.utils.io as io_utils

AV2_ROOT = "~/data/datasets/av2/train-000/sensor/train/"

print(io_utils.read_feather("/home/ohmpr/data/datasets/av2/train-000/sensor/train/01bb304d-7bd8-35f8-bbef-7086b688e35e/annotations.feather"))

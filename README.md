在 xrlocalization 基础上适配 open_vio 的结果和 colmap 格式。

## 1. 提取图像的全局特征
```shell
python3 tools/ir_create_database.py \
    --image_dir ~/output/images \
    --database_path ~/output/database.bin
```
## 2. 生成相似图片匹配对
```shell
python3 tools/ir_image_retrieve.py \
    --database_path ~/output/database.bin \
    --save_path ~/output/pair.txt \
    --retrieve_num 10 \
    --keep_pairs
```
## 3. 提取图像的局部特征点
```shell
python3 tools/recon_feature_extract.py \
    --image_dir ~/output/images \
    --image_bin_path ~/output/map/images.bin \
    --feature_bin_path ~/output/models/features.bin \
    --extractor d2net
```
## 4. 2D 特征匹配
```shell
python3 tools/recon_feature_match.py \
    --recon_path ~/output/map \
    --feature_bin_path ~/output/models/features.bin \
    --match_bin_path ~/output/models/matches.bin
```
## 5. 重建
```shell
python3 tools/loc_convert_reconstruction.py \
    --feature_path ~/output/models/features.bin \
    --model_path ~/output/map \
    --output_path ~/output/models_output
```



## Refenrence
- [1] https://github.com/cvg/Hierarchical-Localization
- [2] https://github.com/openxrlab/xrlocalization

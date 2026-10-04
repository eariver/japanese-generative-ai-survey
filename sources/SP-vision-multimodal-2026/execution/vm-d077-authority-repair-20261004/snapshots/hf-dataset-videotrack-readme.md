---
configs:
- config_name: default
  data_files:
  - path: data/**/*.parquet
    split: train
license: odc-by
---

# Molmo2-VideoTrack

Molmo2-VideoTrack is a dataset of video point tracking annotations collected from human annotators across 16 video datasets.
It can be used to fine-tune vision-language models for video object tracking via point trajectories.

Molmo2-VideoTrack is part of the [Molmo2 dataset collection](https://huggingface.co/collections/allenai/molmo2-data) and was used to train the [Molmo2 family of models](https://huggingface.co/collections/allenai/molmo2).

Quick links:
- 📃 [Paper](https://allenai.org/papers/molmo2)
- 🎥 [Blog with Videos](https://allenai.org/blog/molmo2)

## Usage
```python
from datasets import load_dataset

# Load entire dataset
ds = load_dataset("allenai/Molmo2-VideoTrack", split="train")

# Filter by video dataset
dancetrack = ds.filter(lambda x: x == 'dancetrack', input_columns='video_dataset')
```

## Data Format

Each row contains tracking annotations for one or more objects in a video clip:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for this annotation |
| `video` | Video filename |
| `clip` | trimmed clip id |
| `video_dataset` | Source dataset name (e.g., 'dancetrack', 'mose') |
| `video_source` | Video directory used in training (can be ignored) |
| `exp` | Text expression describing the tracked object(s) |
| `obj_id` | List of object IDs per video |
| `mask_id` | List of mask IDs corresponding to tracked objects starting from '0' |
| `points` | List of point trajectories per object. Each entry contains `object_id` (corresponding to an ID in `mask_id`) and `points` (list of [x, y] coordinates per frame). Example: `[{'object_id': '0', 'points': [[x1, y1], [x2, y2], ...]}, ...]` |
| `segments` | List of segment annotations per object. Each entry contains `object_id` (corresponding to an ID in `mask_id`) and `segments`. Example: `[{'object_id': '0', 'segments': [...]}, ...]` |
| `start_frame` | Starting frame index for this clip (use to trim the source video) |
| `end_frame` | Ending frame index for this clip (use to trim the source video) |
| `w` | Video width |
| `h` | Video height |
| `n_frames` | Number of frames in the clip |
| `fps` | Used in training |

**Important:** `start_frame` and `end_frame` indicate which portion of the source video to use. You need to trim the video to this range — the annotations correspond to frames within `[start_frame, end_frame]`, not the entire video.

## Folder Structure
```
Molmo2-VideoTrack/
├── README.md
└── data/
    ├── animaltrack/
    │   └── point_tracks.parquet
    ├── APTv2/
    │   └── point_tracks.parquet
    ├── ...
    └── {video_dataset}/
        └── point_tracks.parquet
```

## Video Sources

The table below contains information on the sources of the third party datasets used or referenced in curating the data for Molmo2-VideoTrack. We do not provide video files or share the original raw data from datasets with restrictions on use and distribution according to the source license. We instead provide the links, license information, and notes for downloading videos from the original datasets for transparency and reproducibility. Please verify the licenses and use requirements that apply to each dataset before downloading as they may change or be updated by the dataset providers.  

| Dataset | Category | Annotation Source | Download | Dataset License | Note |
|---------|----------|-------------------|----------|-----------------|------|
| mose | General | Segmentation | <a href="https://huggingface.co/datasets/FudanCVL/MOSE" target="_blank">MOSE</a> | CC BY-NC-SA 4.0 |
| mosev2 | General | Segmentation | <a href="https://huggingface.co/datasets/FudanCVL/MOSEv2" target="_blank">MOSEv2</a> | CC BY-NC-SA 4.0 |
| sav | General | Segmentation | <a href="https://ai.meta.com/datasets/segment-anything-video/" target="_blank">SA-V</a> | CC BY 4.0 | Sampled at 6 fps from the original 24 fps video to match the segmentation annotation |
| vipseg | General | Segmentation | <a href="https://github.com/VIPSeg-Dataset/VIPSeg-Dataset/" target="_blank">VIPSeg</a> | Non-commercial research use only | Change to 720p format |
| animaltrack | Animals | Bounding Box | <a href="https://hengfan2010.github.io/projects/AnimalTrack/" target="_blank">AnimalTrack</a> | Non-commercial research use only | Train and val videos are used due to data scarcity |
| APTv2 | Animals | Bounding Box | <a href="https://github.com/ViTAE-Transformer/APTv2" target="_blank">APTv2</a> | Apache 2.0 |
| bft | Bird Flocks | Bounding Box | <a href="https://george-zhuang.github.io/nettrack/" target="_blank">BFT</a> | Apache 2.0 |
| soccernet | Sports | Bounding Box | <a href="https://www.soccer-net.org/data" target="_blank">SoccerNet</a> | Non-commercial research use only | Fill in the NDA form to access the videos |
| sportsmot | Sports | Bounding Box | <a href="https://codalab.lisn.upsaclay.fr/competitions/12424#participate" target="_blank">SportsMOT</a> | CC BY-NC 4.0 |
| teamtrack | Sports | Bounding Box | <a href="https://github.com/AtomScott/TeamTrack" target="_blank">TeamTrack</a> | MIT |
| mot2020 | Pedestrians | Bounding Box | <a href="https://motchallenge.net/data/MOT20/" target="_blank">MOT20</a> | CC BY-NC-SA 3.0 |
| personpath22 | Pedestrians | Bounding Box | <a href="https://amazon-science.github.io/tracking-dataset/personpath22.html" target="_blank">PersonPath22</a> | CC BY-NC 4.0 |
| dancetrack | Dancers | Bounding Box | <a href="https://github.com/DanceTrack/DanceTrack?tab=readme-ov-file#dataset" target="_blank">DanceTrack</a> | Non-commercial research use only |
| bdd100k | Autonomous Driving | Bounding Box | <a href="http://128.32.162.150/bdd100k/video_parts/" target="_blank">BDD100K</a> | BSD-3 | Download only bdd100k_videos_train_00.zip |
| uavdt | UAV | Bounding Box | <a href="https://sites.google.com/view/grli-uavdt/%E9%A6%96%E9%A1%B5" target="_blank">UAVDT</a> | Research use only |
| seadrones | UAV | Bounding Box | <a href="https://seadronessee.cs.uni-tuebingen.de/dataset" target="_blank">SeaDronesSee</a> | CC0 / Unknown | Use 'Multi-Object Tracking' |

## License

This dataset is licensed under ODC-BY-1.0. It is intended for research and educational use in accordance with Ai2's [Responsible Use Guidelines](https://allenai.org/responsible-use). Please refer to the Video Sources section for the original datasets that provide the videos used to generate the segmentations and point tracks for this dataset. All use of the videos and original data from these datasets are subject to the licenses and terms of use provided by the sources. Please check the sources to determine if they are appropriate for your use case.
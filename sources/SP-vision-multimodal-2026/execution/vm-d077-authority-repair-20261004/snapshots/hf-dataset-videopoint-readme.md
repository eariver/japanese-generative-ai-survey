---
dataset_info:
- config_name: action_or_event
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 61887340
    num_examples: 175168
  download_size: 21691971
  dataset_size: 61887340
- config_name: animal
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 5444716
    num_examples: 23750
  download_size: 1710493
  dataset_size: 5444716
- config_name: anomaly
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 4550039
    num_examples: 15204
  download_size: 916819
  dataset_size: 4550039
- config_name: comparative reference
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 10095666
    num_examples: 48015
  download_size: 3289855
  dataset_size: 10095666
- config_name: default
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  splits:
  - name: train
    num_bytes: 222742682
    num_examples: 658340
  download_size: 80210096
  dataset_size: 222742682
- config_name: indirect reference
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 10057929
    num_examples: 39567
  download_size: 3946968
  dataset_size: 10057929
- config_name: object
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 111515506
    num_examples: 267749
  download_size: 42374468
  dataset_size: 111515506
- config_name: referring expression
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 16967502
    num_examples: 60902
  download_size: 7024105
  dataset_size: 16967502
- config_name: spatial reference
  features:
  - name: video_id
    dtype: string
  - name: question
    dtype: string
  - name: label
    dtype: string
  - name: count
    dtype: int64
  - name: two_fps_timestamps
    sequence: float64
  - name: points
    list:
      list:
      - name: x
        dtype: float64
      - name: y
        dtype: float64
  - name: raw_frames
    sequence: int64
  - name: raw_timestamps
    sequence: float64
  - name: annotator_unsure
    dtype: bool
  - name: category
    dtype: string
  - name: video_duration
    dtype: float64
  - name: video_source
    dtype: string
  - name: clip_start
    dtype: float64
  - name: clip_end
    dtype: float64
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 7486908
    num_examples: 27985
  download_size: 2881329
  dataset_size: 7486908
configs:
- config_name: action_or_event
  data_files:
  - split: train
    path: action_or_event/train-*
- config_name: animal
  data_files:
  - split: train
    path: animal/train-*
- config_name: anomaly
  data_files:
  - split: train
    path: anomaly/train-*
- config_name: comparative reference
  data_files:
  - split: train
    path: comparative reference/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: indirect reference
  data_files:
  - split: train
    path: indirect reference/train-*
- config_name: object
  data_files:
  - split: train
    path: object/train-*
- config_name: referring expression
  data_files:
  - split: train
    path: referring expression/train-*
- config_name: spatial reference
  data_files:
  - split: train
    path: spatial reference/train-*
license: odc-by
---

# Molmo2-VideoPoint
Molmo2-VideoPoint is a dataset of video pointing data collected from human annotators.
It can be used to fine-tune vision-language models for video grounding by pointing. 

Molmo2-VideoPoint is part of the [Molmo2 dataset collection](https://huggingface.co/collections/allenai/molmo2-data) and was used to train the [Molmo2 family of models](https://huggingface.co/collections/allenai/molmo2).

Quick links:
- 📃 [Paper](https://allenai.org/papers/molmo2)
- 🎥 [Blog with Videos](https://allenai.org/blog/molmo2)

## Usage

```python
from datasets import load_dataset

# Load entire dataset
ds = load_dataset("allenai/Molmo2-VideoPoint", split="train")

# Load a specific subset by config name
object_points = load_dataset("allenai/Molmo2-VideoPoint", "object", split="train")
action_points = load_dataset("allenai/Molmo2-VideoPoint", "action_or_event", split="train")
```

## Data Format
- `video_source`: There are three video sources: `youtube`, `generated` and `MammalNet`. For YouTube videos, you need to download them by their IDs. We provide a mapping from their IDs to the original Youtube URLs and public Google Cloud Storage URLs in `youtube_id_to_urls_mapping.json`. For generated videos, you can find them in the `generated_videos/` folder. For videos from MammalNet, you can download them following the instructions in their Github repo [here](https://github.com/Vision-CAIR/MammalNet?tab=readme-ov-file#dataset-download). 
- `raw_timestamps` vs. `two_fps_timestamps`: We re-encoded all raw videos into 2FPS and annotated the 2FPS videos. You can find the `raw_frames` and `raw_timestamps` we extracted from the original videos, and the `two_fps_timestamps` we used in model training. 
- `points`: Each entry in `points` is a list of lists of 2D coordinates, where `points[i]` corresponds to a list of 2D points for `timestamps[i]`.
- `annotator_unsure`: This column records whether the annotator was unsure about their annotation. During model training, we used only the examples they marked sure (i.e.`annotator_unsure==false`) by default.
- `category`: This column denotes the category of pointing queries, including object, action/event, animal, referring expression, indirect reference, spatial reference, comparative reference and visual artifacts/anomalies (for generative videos only).

## Video Download Helpers
```
import json
import os
import urllib.request
from urllib.parse import urlparse
from google.cloud import storage

MAPPING_URL = "https://huggingface.co/datasets/allenai/Molmo2-VideoPoint/resolve/main/youtube_id_to_urls_mapping.json"
GCP_PROJECT = "YOUR_PROJECT_ID"  

def load_mapping(cache_path: str = "youtube_id_to_urls_mapping.json") -> dict:
    """Fetch the YouTube-ID-to-URL mapping, caching locally after first download."""
    if os.path.exists(cache_path):
        print(f"Loading cached mapping from {cache_path}")
        with open(cache_path) as f:
            return json.load(f)
    print("Fetching URL mapping from HuggingFace...")
    urllib.request.urlretrieve(MAPPING_URL, cache_path)
    with open(cache_path) as f:
        mapping = json.load(f)
    print(f"Cached {len(mapping)} entries to {cache_path}")
    return mapping


def parse_gcs_url(gcs_url: str) -> tuple[str, str]:
    """Parse 'https://storage.googleapis.com/BUCKET/OBJECT' into (bucket, object)."""
    parsed = urlparse(gcs_url)
    parts = parsed.path.lstrip("/").split("/", 1)
    return parts[0], parts[1]


def to_2fps_blob(blob_name: str, youtube_id: str) -> str:
    """Convert original blob path to 2fps path.

    e.g. youtube-cc-exist/X/X.mkv -> youtube-cc-exist-2fps/X_2fps.mp4
    """
    top_dir = blob_name.split("/", 1)[0]
    return f"{top_dir}-2fps/{youtube_id}_2fps.mp4"


def download_video_by_id(youtube_id: str, output_dir: str = "./videos", mapping: dict = None, fps2: bool = False):
    """Download a video from allenai/Molmo2-VideoPoint by YouTube ID using the GCS API.

    Args:
        fps2: If True, download the 2fps version ({top_dir}-2fps/{id}_2fps.mp4).
    """
    if mapping is None:
        mapping = load_mapping()

    if youtube_id not in mapping:
        raise KeyError(f"YouTube ID '{youtube_id}' not found in mapping ({len(mapping)} entries)")

    gcp_url = mapping[youtube_id]["gcp_url"]
    bucket_name, blob_name = parse_gcs_url(gcp_url)

    if fps2:
        blob_name = to_2fps_blob(blob_name, youtube_id)

    # Preserve GCS directory structure
    output_path = os.path.join(output_dir, blob_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Authenticated client with user_project for requester-pays bucket
    client = storage.Client(project=GCP_PROJECT)
    bucket = client.bucket(bucket_name, user_project=GCP_PROJECT)
    blob = bucket.blob(blob_name)

    print(f"Downloading gs://{bucket_name}/{blob_name} -> {output_path}")
    blob.download_to_filename(output_path)
    print(f"Done. Saved to {output_path} ({os.path.getsize(output_path) / 1e6:.1f} MB)")
    return output_path

# Original video
download_video_by_id("YKrWWlbS3uM", output_dir="./video_datasets/youtube-cc", mapping=mapping)
# -> ./video_datasets/youtube-cc/youtube-cc-temporal/YKrWWlbS3uM/YKrWWlbS3uM.mp4

# Uniformly sampled 2fps version
download_video_by_id("YKrWWlbS3uM", output_dir="./video_datasets/youtube-cc", mapping=mapping, fps2=True)
# -> ./video_datasets/youtube-cc/youtube-cc-temporal-2fps/YKrWWlbS3uM_2fps.mp4
```

## License
This dataset is licensed under ODC-BY. A subset of videos from this dataset that are licensed as CC BY-4.0 may be downloaded from our Google Cloud Bucket via the URLs in `youtube_id_to_urls_mapping.json`. The dataset and videos are intended for research and educational use in accordance with Ai2’s [Responsible Use Guidelines](https://allenai.org/responsible-use). This dataset includes questions generated from GPT-4.1 and GPT-5, which are subject to OpenAI’s [Terms of Use](https://openai.com/policies/row-terms-of-use/).
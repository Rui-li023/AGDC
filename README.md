# AGDC

## 📦 Installation

```bash
conda create -n agdc python=3.10
conda activate agdc
conda install pytorch==2.5.0 torchvision==0.20.0 pytorch-cuda=12.4 -c pytorch -c nvidia

mamba install conda-build
pip install -r requirements.txt
```


```bash
mkdir -p deps
cd deps
if [ ! -d "dinov2" ]; then
  git clone https://github.com/facebookresearch/dinov2.git
fi
cd dinov2 && conda-develop . && cd ..

if [ ! -d "segment-anything-2" ]; then
  git clone https://github.com/facebookresearch/segment-anything-2.git
fi
cd segment-anything-2 && pip install -e . && cd ..

# GroundingDINO
if [ ! -d "GroundingDINO" ]; then
  git clone https://github.com/IDEA-Research/GroundingDINO.git
fi
cd GroundingDINO && export CUDA_HOME=/usr/local/cuda-12.4 && pip install --no-build-isolation -e . && cd ..

# PerspectiveFields
if [ ! -d "PerspectiveFields" ]; then
  git clone https://github.com/jinlinyi/PerspectiveFields.git
fi
cd PerspectiveFields && pip install -e . && cd ..

# Depth-Anything-V2
if [ ! -d "Depth-Anything-V2" ]; then
  git clone https://github.com/DepthAnything/Depth-Anything-V2.git
fi
cd Depth-Anything-V2 && pip install -r requirements.txt && conda-develop . && cd ..

# CLIP
pip install git+https://github.com/openai/CLIP.git

# faiss
conda install -c pytorch -c nvidia faiss-gpu=1.8.0
```

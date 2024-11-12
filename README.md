---
tags:
- text-to-image
- lora
- diffusers
- template:diffusion-lora
- Super-Realism
- Flux.1-Dev
- Dynamic-Realism
- Realistic
- Photorealism
- Hi-Res
- UltraRealism
- Diffusion
- Face
widget:
- text: >-
    Super Realism, Woman in a red jacket, snowy, in the style of hyper-realistic
    portraiture, caninecore, mountainous vistas, timeless beauty, palewave,
    iconic, distinctive noses --ar 72:101 --stylize 750 --v 6
  output:
    url: images/3.png
- text: >-
    Super Realism, Headshot of handsome young man, wearing dark gray sweater
    with buttons and big shawl collar, brown hair and short beard, serious look
    on his face, black background, soft studio lighting, portrait photography
    --ar 85:128 --v 6.0 --style rawHeadshot of handsome young man, wearing dark
    gray sweater with buttons and big shawl collar, brown hair and short beard,
    serious look on his face, black background, soft studio lighting, portrait
    photography --ar 85:128 --v 6.0 --style rawHeadshot of handsome young man,
    wearing dark gray sweater with buttons and big shawl collar, brown hair and
    short beard, serious look on his face, black background, soft studio
    lighting, portrait photography --ar 85:128 --v 6.0 --style raw
  output:
    url: images/2.png
- text: >-
    Super Realism, High-resolution photograph, woman, UHD, photorealistic, shot
    on a Sony A7III --chaos 20 --ar 1:2 --style raw --stylize 250
  output:
    url: images/1.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: Super Realism
license: mit
library_name: transformers
---
![strangerzonehf/Flux-Super-Realism-LoRA](images/sz.png)

## Stranger Zone's - Flux Super Realism LoRA

<Gallery />

## Model description for super realism

Image Processing Parameters 

| Parameter                 | Value  | Parameter                 | Value  |
|---------------------------|--------|---------------------------|--------|
| LR Scheduler              | constant | Noise Offset              | 0.03   |
| Optimizer                 | AdamW  | Multires Noise Discount   | 0.1    |
| Network Dim               | 64     | Multires Noise Iterations | 10     |
| Network Alpha             | 32     | Repeat & Steps           | 30 & 4380|
| Epoch                     | 20  | Save Every N Epochs       | 1      |

## Comparison between the base model and related models.

Comparison between the base model FLUX.1-dev and its adapter, a LoRA model tuned for super-realistic realism.
[ 28 steps ]

![strangerzonehf/Flux-Super-Realism-LoRA](images/sz2.png)

However, it performs better in various aspects compared to its previous models, including face realism, ultra-realism, and others.
previous versions [ 28 steps ]

![strangerzonehf/Flux-Super-Realism-LoRA](images/sz3.png)

## Previous Model Links

| Model Name                               | Description                  | Link                                                                                     |
|------------------------------------------|------------------------------|------------------------------------------------------------------------------------------|
| **Canopus-LoRA-Flux-FaceRealism**        | LoRA model for Face Realism  | [Canopus-LoRA-Flux-FaceRealism](https://huggingface.co/prithivMLmods/Canopus-LoRA-Flux-FaceRealism) |
| **Canopus-LoRA-Flux-UltraRealism-2.0**   | LoRA model for Ultra Realism | [Canopus-LoRA-Flux-UltraRealism-2.0](https://huggingface.co/prithivMLmods/Canopus-LoRA-Flux-UltraRealism-2.0) |
| **Flux.1-Dev-LoRA-HDR-Realism [Experimental Version]**          | LoRA model for HDR Realism   | [Flux.1-Dev-LoRA-HDR-Realism](https://huggingface.co/prithivMLmods/Flux.1-Dev-LoRA-HDR-Realism) |
| **Flux-Realism-FineDetailed**            | Fine-detailed realism-focused model                 | [Flux-Realism-FineDetailed](https://huggingface.co/prithivMLmods/Flux-Realism-FineDetailed)    |

## Hosted/Demo Links

| Demo Name                  | Description                | Link                                                                                 |
|----------------------------|----------------------------|--------------------------------------------------------------------------------------|
| **FLUX-LoRA-DLC**          | Demo for FLUX LoRA DLC     | [FLUX-LoRA-DLC](https://huggingface.co/spaces/prithivMLmods/FLUX-LoRA-DLC)           |
| **FLUX-REALISM**           | Demo for FLUX Realism      | [FLUX-REALISM](https://huggingface.co/spaces/prithivMLmods/FLUX-REALISM)             |

## Model Training Basic Details 

| Feature                        | Description                         |
|--------------------------------|-------------------------------------|
| **Labeling**                   | florence2-en (natural language & English) |
| **Total Images Used for Training** | 55 [Hi-Res]                  |
| **Best Dimensions**            | - 1024 x 1024 (Default)             |
|                                | - 768 x 1024                        |

## Setting Up Flux Space
```python
import torch
from pipelines import DiffusionPipeline

base_model = "black-forest-labs/FLUX.1-dev"
pipe = DiffusionPipeline.from_pretrained(base_model, torch_dtype=torch.bfloat16)

lora_repo = "strangerzonehf/Flux-Super-Realism-LoRA"
trigger_word = "Super Realism"   #triggerword
pipe.load_lora_weights(lora_repo)

device = torch.device("cuda")
pipe.to(device)
```
## Trigger words

> [!WARNING]
> **Trigger words:**  You should use `Super Realism` to trigger the image generation.

- The trigger word is not mandatory; ensure that words like "realistic" and "realism" appear in the image description. The "super realism" trigger word should prompt an exact match to the reference image in the showcase.
## Download model

Weights for this model are available in Safetensors format.

[Download](/strangerzonehf/Flux-Super-Realism-LoRA/tree/main) them in the Files & versions tab.
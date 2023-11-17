# FuseCap: Leveraging Large Language Models for Enriched Fused Image Captions

Welcome to the GitHub repository of FuseCap, a framework designed to enhance image captioning by incorporating detailed visual information into traditional captions.

🎉 Exciting News: Paper accepted at WACV 2024!

## Resources

- 💻 **Project Page**: For more details, visit the official [project page](https://rotsteinnoam.github.io/FuseCap/).

- 📝 **Read the Paper**: You can find the paper [here](https://arxiv.org/abs/2305.17718).
    
- 🚀 **Demo**: Try out our BLIP-based model [demo](https://huggingface.co/spaces/noamrot/FuseCap) trained using FuseCap, hosted on Huggingface Spaces.


## Release Status

### Done

- ✅ HuggingFace Captioner demo, including captioner weights.
- ✅ Release of the FuseCap dataset.

### To Do

- 🔜 Publication of the complete codebase.
- 🔜 LLM Fuser weights and code release.


##  Hugging Face Demo
Try out our BLIP-based captioning model trained using FuseCap quickly with this Python snippet.
This code demonstrates how to use the model to generate captions for an image:

```python
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
processor = BlipProcessor.from_pretrained("noamrot/FuseCap")
model = BlipForConditionalGeneration.from_pretrained("noamrot/FuseCap").to(device)

img_url = 'https://huggingface.co/spaces/noamrot/FuseCap/resolve/main/bike.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

text = "a picture of "
inputs = processor(raw_image, text, return_tensors="pt").to(device)

out = model.generate(**inputs, num_beams = 3)
print(processor.decode(out[0], skip_special_tokens=True))
```

##  Datasets
We provide the fused captions that were created using the FuseCap framework.
These captions were used for both pretraining and training phases of our image captioning model. 
The images can downloaded from the respective dataset websites or the provided urls (SBU, CC3, CC12).

Dataset | FuseCap Captions
--- | :---:
COCO | <a href="https://zenodo.org/record/8149179/files/coco_karpathy_train.json?download=1">Train</a>, <a href="https://zenodo.org/record/8132314/files/coco_karpathy_val.json?download=1">Val</a>, <a href="https://zenodo.org/record/8132335/files/coco_karpathy_test.json?download=1">Test</a>
SBU | <a href="https://zenodo.org/record/8133271/files/SBU_FuseCap.json?download=1">Train</a>
CC3 | <a href="https://zenodo.org/record/8133285/files/CC3_FuseCap.json?download=1">Train</a>
CC12 | Soon

## BibTeX

```
@misc{rotstein2023fusecap,
      title={FuseCap: Leveraging Large Language Models for Enriched Fused Image Captions}, 
      author={Noam Rotstein and David Bensaid and Shaked Brody and Roy Ganz and Ron Kimmel},
      year={2023},
      eprint={2305.17718},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

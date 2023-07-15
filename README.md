# FuseCap: Leveraging Large Language Models to Fuse Visual Data into Enriched Image Captions

Welcome to the GitHub repository of FuseCap, a framework designed to generate semantically rich image captions.

## Resources

- 💻 **Project Page**: For more details, visit the official [project page](https://rotsteinnoam.github.io/FuseCap/).

- 📝 **Read the Paper**: You can find the paper [here](https://arxiv.org/abs/2305.17718).
    
- 🚀 **Demo**: Try out our BLIP-based model [demo](https://huggingface.co/spaces/noamrot/FuseCap) trained using FuseCap, hosted on Huggingface Spaces.

## Upcoming Updates

The official datasets, codebase and trained models for this project will be released soon.


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
Flickr30 | Soon

## BibTeX

```
@article{rotstein2023fusecap,
  title={FuseCap: Leveraging Large Language Models to Fuse Visual Data into Enriched Image Captions},
  author={Rotstein, Noam and Bensaid, David and Brody, Shaked and Ganz, Roy and Kimmel, Ron},
  journal={arXiv preprint arXiv:2305.17718},
  year={2023}
}
```

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
COCO | <a href="https://technionmail-my.sharepoint.com/personal/snoamr_campus_technion_ac_il/_layouts/15/download.aspx?UniqueId=28819a77%2D24aa%2D46b8%2Dba21%2D133522a0f081">Train</a>, <a href="https://technionmail-my.sharepoint.com/personal/snoamr_campus_technion_ac_il/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fsnoamr%5Fcampus%5Ftechnion%5Fac%5Fil%2FDocuments%2Ffusecap%5Fdatasets%2Fcoco%5Fkarpathy%5Fval%2Ejson">Val</a>, <a href="https://technionmail-my.sharepoint.com/personal/snoamr_campus_technion_ac_il/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fsnoamr%5Fcampus%5Ftechnion%5Fac%5Fil%2FDocuments%2Ffusecap%5Fdatasets%2Fcoco%5Fkarpathy%5Ftest%2Ejson">Test</a>
SBU | <a href="https://technionmail-my.sharepoint.com/personal/snoamr_campus_technion_ac_il/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fsnoamr%5Fcampus%5Ftechnion%5Fac%5Fil%2FDocuments%2Ffusecap%5Fdatasets%2FSBU%5FFuseCap%2Ejson">Train</a>
CC3 | Soon
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

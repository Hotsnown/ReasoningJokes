# Learning to Reason for Joke Punchline Prediction

Official repo for Learning to Reason for Joke Punchline Prediction, available on [arxiv](https://arxiv.org/abs/2503.22828).

This work presents a new RL-reward paradigm, Verifiable Rewards via Completion Likelihood Improvement (VR-CLI), which is then used to train a model to predict witty punchlines for jokes.

This repo contains five parts:

1. `setup_data`: Compile a Punchline Prediction dataset, used for training and punchline generation
2. `rl_training`: Train a model using our VR-CLI reward paradigm, using either the punchline task or another task of your choosing
3. `sft_training`: Train a model using supervised finetuning on the punchline dataset
4. `story_generation`: Generate reasoning and punchlines using either a pretrained model, or a model you have trained yourself
5. `evaluation`: Replicate our evaluations of the story generation models using human annotations and automated metrics

Consult the `instructions.md` files in each directory for more details.

## Citation

If you find this work useful, please cite it as follows:

```bibtex
@misc{gurung2025learningreasonlongformstory,
      title={Learning to Reason for Long-Form Story Generation}, 
      author={Alexander Gurung and Mirella Lapata},
      year={2025},
      eprint={2503.22828},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.22828}, 
}
```

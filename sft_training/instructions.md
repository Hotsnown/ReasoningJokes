# SFT Training Instructions

## Install Dependencies

```bash
pip install -r requirements.txt
```

Note: the primary requirements is `TRL`, different installations for your own environment may also work.

## Setup Data

First, organize your joke data using the instructions in the `setup_data` directory. Then run

```bash
python setup_sft_data.py --model_name Qwen/Qwen2.5-3B-Instruct --dataset_name joke_dataset --data_dir sft_data/
```

## Train

Modify the config files (`7b_config.yaml` or `3b_config.yaml`) to set the correct parameters for your training run. The current wandb-parameters are placeholders, and should be modified to your own wandb account.

```bash
python train_sft.py --config_name 3b_config.yaml # or 7b_config.yaml
```









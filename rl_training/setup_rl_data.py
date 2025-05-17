import jsonlines
from prompt_utils import generate_punchline_messages
import argparse
# for estimating tokens
from transformers import AutoTokenizer
# for getting stats about the dataset
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--tokenizer_name", type=str, default="Qwen/Qwen2.5-3B-Instruct")
parser.add_argument("--data_dir", type=str, default="rl_data/")
parser.add_argument("--dataset_name", type=str, default="joke_dataset")
args = parser.parse_args()

tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_name)

def get_initial_dataset(split):
    initial_dataset_fname = args.dataset_name + "_" + split + ".jsonl"
    with jsonlines.open(initial_dataset_fname, "r") as reader:
        initial_dataset = list(reader)

    num_tokens = []
    
    prompts = []
    for datapoint in initial_dataset:
        messages = generate_punchline_messages(datapoint)
        num_tokens.append(
            tokenizer.apply_chat_template(messages, tokenize=True, return_tensors="pt").shape[-1]
        )
        prompts.append({"prompt": messages})
    return prompts, num_tokens


train_prompts, train_num_tokens = get_initial_dataset("train")
test_prompts, test_num_tokens = get_initial_dataset("test")
val_prompts, val_num_tokens = get_initial_dataset("val")

# get max, min, mean, std of num_tokens
print(f"Train num_tokens: max {np.max(train_num_tokens)}, min {np.min(train_num_tokens)}, mean {np.mean(train_num_tokens)}, std {np.std(train_num_tokens)}")
print(f"Test num_tokens: max {np.max(test_num_tokens)}, min {np.min(test_num_tokens)}, mean {np.mean(test_num_tokens)}, std {np.std(test_num_tokens)}")
print(f"Val num_tokens: max {np.max(val_num_tokens)}, min {np.min(val_num_tokens)}, mean {np.mean(val_num_tokens)}, std {np.std(val_num_tokens)}")

data_dir = args.data_dir

train_fname = data_dir + "train.jsonl"
test_fname = data_dir + "test.jsonl"
val_fname = data_dir + "val.jsonl"

# for fname, prompts in zip([test_fname], [test_prompts]):
for fname, prompts in zip([train_fname, test_fname, val_fname], [train_prompts, test_prompts, val_prompts]):
    print(f"Writing {fname} with {len(prompts)} prompts")
    with jsonlines.open(fname, "w") as writer:
        writer.write_all(prompts)

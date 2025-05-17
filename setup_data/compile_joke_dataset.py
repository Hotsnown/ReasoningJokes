import json
import random
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--output_dir', type=str, default='.')
parser.add_argument('--seed', type=int, default=42)
args = parser.parse_args()

random.seed(args.seed)

with open(args.input, 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]

random.shuffle(data)

n = len(data)
train_end = int(0.8 * n)
val_end = int(0.9 * n)

splits = {
    'train': data[:train_end],
    'val': data[train_end:val_end],
    'test': data[val_end:]
}

os.makedirs(args.output_dir, exist_ok=True)
for split, items in splits.items():
    fname = os.path.join(args.output_dir, f'joke_dataset_{split}.jsonl')
    with open(fname, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(f'Wrote {len(items)} examples to {fname}')

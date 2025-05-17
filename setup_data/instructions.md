# Setup Joke Data

Store your jokes in a JSONL file where each entry contains a `messages` field. The value should be a list of chat messages with the punchline as the last assistant message.

Example entry:
```json
{"messages": [{"role": "system", "content": "You are a master of witty repartee."}, {"role": "user", "content": "Une de ses admiratrices lui confiait : Cher maître ..."}, {"role": "assistant", "content": "Moi si, hélas, chère madame."}]}
```

Split the data using `compile_joke_dataset.py`:
```bash
python compile_joke_dataset.py --input jokes.jsonl --output_dir dataset/
```

The script will create `joke_dataset_train.jsonl`, `joke_dataset_test.jsonl`, and `joke_dataset_val.jsonl` in the output directory.

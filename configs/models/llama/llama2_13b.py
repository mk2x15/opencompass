from opencompass.models import Llama2

# Please follow the instruction in the Meta AI website https://github.com/facebookresearch/llama
# and download the LLaMA-2 model and tokenizer to the path './models/llama2/llama/'.
#
# The LLaMA requirement is also needed to be installed.
#
# git clone https://github.com/facebookresearch/llama.git
# cd llama
# pip install -e .

models = [dict(
        abbr="llama-2-13b",
        type=Llama2,
        path="./models/llama2/llama/llama-2-13b/",
        tokenizer_path="./models/llama2/llama/tokenizer.model",
        max_out_len=100,
        max_seq_len=2048,
        batch_size=16,
        run_cfg=dict(num_gpus=2, num_procs=2),
    ),]

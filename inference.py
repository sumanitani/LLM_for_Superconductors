from unsloth import FastLanguageModel
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

###############################################
# 1) Load BASE model (required for LoRA)
###############################################
base_model = "unsloth/mistral-7b-v0.3"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=base_model,
    max_seq_length=2048,
    load_in_4bit=True,  # same as you used in training
    load_in_8bit=False,
)

###############################################
# 2) Load YOUR LoRA adapter from HuggingFace
###############################################
lora_repo = "sumanitani/mistral-sc-tc-cs-sg-lora"

model.load_adapter(lora_repo, adapter_name="default")
model.set_adapter("default")

FastLanguageModel.for_inference(model)
###############################################


ALPACA_PROMPT = (
    "Below is an instruction that describes a task, paired with an input that provides further context. "
    "Write a response that appropriately completes the request.\n\n"
    "### Instruction:\n{instruction}\n\n"
    "### Input:\n{input}\n\n"
    "### Response:\n"
)


def make_alpaca_prompt(instr, inp):
    return ALPACA_PROMPT.format(instruction=instr, input=inp)


questions = [
    {
        "instruction": "Given a material’s crystal system, space group, and chemical composition, predict its superconducting transition temperature (Tc).",
        "input": "Material: Bi1.6Pb0.2Sr2Ca2Cu3O10\nCrystal system: Tetragonal",
    },
    {
        "instruction": "Given a material’s crystal system, space group, and chemical composition, predict its superconducting transition temperature (Tc).",
        "input": "Material: Ca0.4La1.25Ba1.35Cu3O6.884\nCrystal system: Tetragonal\nSpace group: P4/mmm",
    },
    {
        "instruction": "Given a material’s crystal system, space group, and chemical composition, predict its superconducting transition temperature (Tc).",
        "input": "Material: Nd1Ba2Cu2.96Ga0.04O6.85\nCrystal system: Orthorhombic",
    },
    {
        "instruction": "Given a material’s crystal system, space group, and chemical composition, predict its superconducting transition temperature (Tc).",
        "input": "Material: Y0.52Eu0.58Ba1.9Cu2.69Al0.42O7\nCrystal system: 123-phase",
    },
]

gen_kwargs = dict(
    max_new_tokens=128,
    temperature=0.1,
    top_p=0.9,
    top_k=40,
    do_sample=True,
    eos_token_id=tokenizer.eos_token_id,
)

for i, qa in enumerate(questions, 1):
    prompt = make_alpaca_prompt(qa["instruction"], qa["input"])

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    input_len = inputs["input_ids"].shape[1]

    with torch.no_grad():
        outputs = model.generate(**inputs, **gen_kwargs)

    answer = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True)

    print(f"\nQ{i}: {qa['input'].splitlines()[0]}")
    print(f"A{i}: {answer}")
    print("-" * 60)

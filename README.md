# LLM_for_Superconductors
# 🔬 Superconductor LLM Collection (LoRA Fine-Tuned Models)

This repository contains the full collection of **LoRA fine-tuned large language models** developed for superconductivity research.  
These models are fine-tuned for:

- **SC / non-SC classification**
- **Tc regression (composition-only)**
- **Tc regression (composition + crystal system + space group)**
- **Tc regression using CIF structural files**
- **Inverse design** (generate candidate compositions given target Tc or structural constraints)

All models are hosted on Hugging Face under:  
👉 https://huggingface.co/sumanitani

The repository includes:

- `inference.py` → universal inference script for all models  
- Instructions on how to load base models + LoRA adapters  
- List of model categories and direct HF links  
- Required base-model paths

---

# 📦 1. Model Categories & HuggingFace Links

## **A. SC / NSC Classification Models**
| Model | HF Link |
|------|---------|
| **Mistral-7B Classification LoRA** | https://huggingface.co/sumanitani/Mistral-7b-classification-sc-lora/ |
| **Qwen3 Classification LoRA** | https://huggingface.co/sumanitani/Qwen3-classification-sc-lora/ |
| **Llama3 Classification LoRA** | https://huggingface.co/sumanitani/Llamma3-classification-sc-lora/ |
| **Phi4 Classification LoRA** | https://huggingface.co/sumanitani/Phi4-classification-sc-lora/ |
| **Qwen3-2507 Classification LoRA** | https://huggingface.co/sumanitani/Qwen3-2507-classification-sc-lora/ |

---

## **B. Tc Regression (Composition-only)**
| Model | HF Link |
|------|---------|
| **Mistral-7B TC-composition LoRA** | https://huggingface.co/sumanitani/Mistral-7b-SC-Tc-composition-lora/ |
| **Qwen3-14B TC-composition LoRA** | https://huggingface.co/sumanitani/Qwen3-14b-SC-Tc-composition-lora/ |
| **Llama3-8B TC-composition LoRA** | https://huggingface.co/sumanitani/Llama3-8b-SC-Tc-composition-lora/ |
| **Phi4-14B TC-composition LoRA** | https://huggingface.co/sumanitani/Phi4-14b-SC-Tc-composition-lora/ |

---

## **C. Tc Regression (Composition + Crystal System + Space Group)**
| Model | HF Link |
|------|---------|
| **Mistral-7B cs+sg LoRA** | https://huggingface.co/sumanitani/mistral-sc-tc-cs-sg-lora/ |
| **Qwen3 cs+sg LoRA** | https://huggingface.co/sumanitani/Qwen3-sc-tc-cs-sg-lora/ |
| **Llama3 cs+sg LoRA** | https://huggingface.co/sumanitani/Llama3-sc-tc-cs-sg-lora/ |

---

## **D. Tc Regression using CIF structural files**
| Model | HF Link |
|------|---------|
| **Qwen3-14B CIF LoRA** | https://huggingface.co/sumanitani/Qwen3-14b-SC-Tc-cif-lora/ |
| **Mistral-7B CIF LoRA** | https://huggingface.co/sumanitani/Mistral-7b-SC-Tc-cif-lora/ |
| **Llama-8B CIF LoRA** | https://huggingface.co/sumanitani/Llama-8b-SC-Tc-cif-lora/ |

---

## **E. Inverse-Design Models**
| Model | HF Link |
|------|---------|
| **Qwen3 SC Inverse-Design LoRA** | https://huggingface.co/sumanitani/Qwen3-SC-inverse-design-lora/ |

---

# ⚙️ 2. Base Models Required for Inference

Each LoRA model must be loaded **on top of its corresponding base model**.

Below are the exact base-model paths:

| Base Model | HuggingFace Path |
|------------|------------------|
| **Mistral-7B (Unsloth)** | `unsloth/mistral-7b-v0.3` |
| **Qwen3-14B** | `unsloth/Qwen3-14B` |
| **Llama-3.1-8B** | `unsloth/Meta-Llama-3.1-8B` |
| **Qwen3-2507-4B** | `unsloth/Qwen3-4B-Instruct-2507` |
| **Phi-4** | `unsloth/Phi-4` |

These go into your inference script.

---

# 🚀 3. How to Use These Models (with `inference.py`)

This repository includes a universal script:

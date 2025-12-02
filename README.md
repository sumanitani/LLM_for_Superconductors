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



---

# 🚀 3. How to Use These Models (with `inference.py`)

This repository includes a universal `inference.py` script that can be used with **any** of the LoRA models listed above.

## 3.1 Install Dependencies
All fine-tuned models in this repository were trained and optimized using the
Unsloth framework. Before running inference, install the Unsloth package and required libraries:

    pip install unsloth

Unsloth enables fast and memory-efficient loading of base models in 4-bit precision.

(Users may also install any additional packages listed at the top of `inference.py`.)

## 3.2 How to Select Which Model to Run
Inside the `inference.py` file, you will find placeholders where you must select:

- **BASE_MODEL** → the original foundation model used before fine-tuning  
- **LORA_MODEL** → one of the LoRA adapters from the Hugging Face links above  

To run a specific model, simply replace these two lines with the correct model names taken from the tables in Section 1 and Section 2 of this README.

**Example instruction for users:**
> “Choose one LoRA model from the list above and replace the BASE_MODEL and LORA_MODEL fields in `inference.py` with the corresponding base model and LoRA model names.”

This allows the same script to work for:
- Classification  
- Tc regression (composition-only)  
- Tc regression (composition + system + space group)  
- CIF-based Tc prediction  
- Inverse design  


## 3.3 Editing Input Format (Instruction / Input Sections)
The models were trained using an Alpaca-style instruction format.  
To use your own materials or queries, modify the fields:

- **instruction** – describes the task  
- **input** – contains the composition, crystal structure, space group, or CIF-based information  

These formats are described in detail in the **Methods section** of the associated manuscripts.  
Users simply replace the example text inside these fields with their own material data.

After replacing:
- BASE_MODEL  
- LORA_MODEL  
- instruction text  
- input text  

the script is fully ready for inference with any model in this repository.


If you use these models in academic or research work, please cite the corresponding papers listed in the **Citation** section below.

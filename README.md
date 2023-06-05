![LOGO](https://github.com/EAGE-Annual-Hackathon/GeoDude/blob/main/geodude.png)

# GeoDude

> **Unleashing the Power of LLM's for Geoscience Data**\
> EAGE Hackathon - Natural Language Processing (NLP)\
> Corrales M.<sup>1</sup>, Luiken N.<sup>1</sup>, Alfarhan M.<sup>1</sup>\
> King Abdullah University of Science and Technology (KAUST)<sup>1</sup>


<br>

The key concept behind this project is the utilization of [Llama loaders](https://llamahub.ai/), which facilitate the seamless integration of structured and unstructured data. These collectors are then used to create [Llama indexes](https://gpt-index.readthedocs.io/en/latest/), enabling in-context learning without the need for fine-tuning. This approach empowers efficient and effective information retrieval and analysis, enhancing the overall learning experience.


## Project structure
This repository is organized as follows:

* :open_file_folder: **package**: python library containing routines for geodude. 
* :open_file_folder: **notebooks**: set of jupyter notebooks reproducing the experiments for the hackathon.
* :open_file_folder: **notebooks/data_test**: folder containing geoscience data for the experiments.
* :open_file_folder: **notebooks/data_petrobowl**: folder containing petrobowl data for alpaca fine-tuning.

## Notebooks
The following notebooks are provided:

- :orange_book: ``01_Camel_Loading_PDF_Example_1.ipynb``: notebook performing 'in context' learning from a pdf provided. The model used is Camel 5B (Example 2).
- :orange_book: ``01_Camel_Loading_PDF_Example_2.ipynb``: notebook performing 'in context' learning from a pdf provided. The model used is Camel 5B (Example 2).
- :orange_book: ``01_GPT_Loading_PDF_Example_1.ipynb``: notebook performing 'in context' learning from a pdf provided. The model used is GPT from openai(Example 1).
- :orange_book: ``01_GPT_Loading_PDF_Example_2.ipynb``: notebook performing 'in context' learning from a pdf provided. The model used is GPT from openai(Example 2).
- :orange_book: ``02_Camel_Loading_Multiple_PDF_Example.ipynb``: notebook performing 'in context' learning from a set of pdf's. The model used is Camel 5B.
- :orange_book: ``02_GPT_Loading_Multiple_PDF_Example.ipynb``: notebook performing 'in context' learning from a set of pdf's. The model used is GPT from openai.
- :orange_book: ``03_Camel_Loading_Youtube_Example.ipynb``: notebook performing 'in context' learning from a youtube video. The model used is Camel 5B.
- :orange_book: ``03_GPT_Loading_Youtube_Example.ipynb``: notebook performing 'in context' learning from a youtube video. The model used GPT from openai.
- :orange_book: ``04_Gradio_Interface.ipynb``: notebook performing example for API generation using gradio.
- :orange_book: ``05_Custom_Dataset_for_Alpaca.ipynb``: notebook performing the dataset creating needed for the alpaca lora fine-tunning.
- :orange_book: ``06_Alpaca-fine-tuning.ipynb``: notebook performing the LoRA alpaca fine-tuning for the petrobowl dataset.



## Getting started :space_invader: :robot:
To ensure reproducibility of the results, we suggest using the `environment.yml` file when creating an environment.

Simply run:
```
./install_env.sh
```
It will take some time, if at the end you see the word `Done!` on your terminal you are ready to go. After that you can simply install your package:
```
pip install .
```
or in developer mode:
```
pip install -e .
```

Remember to always activate the environment by typing:
```
conda activate geodude
```



> **Note** <br>
> All experiments have been carried on a Intel(R) Xeon(R) Silver 4316 CPU @ 2.30GHz equipped with a single NVIDIA TESLA A100 GPU. Different 
> environment configurations may be required for different combinations of workstation and GPU.

> **Warning** <br>
> To simplify the process, we have utilized the model from OpenAI, requiring an API key. If you wish to replicate these notebooks, you can generate 
> your [own API key](https://platform.openai.com/account/api-keys). This will allow you to access the necessary resources and execute the code
> successfully.
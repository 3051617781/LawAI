# LawAI: A Large Language Model-based Legal Assistant Enhanced by RAG. 

<div align="center">
  <a href="https://github.com/3051617781/LawAI">
    <img width="15%" alt="favicon" src="https://github.com/user-attachments/assets/5bc185f0-aeec-4f75-88c5-61c46ce8fd23">
  </a>
  <p align="center">
    <h3>法之昭然于天下者，律则凛然于人心</h3>
    <a href="https://github.com/3051617781/LawAI/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/3051617781/LawAI" />
      </a>
      <a href="https://github.com/3051617781/LawAI/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/3051617781/LawAI?color=0088ff" />
      </a>
      <a href="https://github.com/3051617781/LawAI/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/3051617781/LawAI?color=0088ff" />
      </a>
      <a href="https://github.com/3051617781/LawAI/stargazers">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/3051617781/LawAI?color=ccf" />
      </a>
      <br/>
      <a href="https://huggingface.co/StarUniver/lawllm-gguf"><strong>HuggingFace</strong></a>
  </p>
</div>

# LawAI Models
## <a href="https://huggingface.co/StarUniver/Qwen-LawLLM">LawAI-Qwen</a>
- **Base Model**:Based on `Qwen7b`.
- **Enhancements**: Significantly increased training data volume and rounds (about **2** days of training).
- **Limitation**:Partial overfitting occurs(Caused by **2w** pairs of Q&A with **30** epochs of training).
## <a href="https://huggingface.co/StarUniver/lawllm-gguf">LawAI-7B</a>
- **Base Model**:Based on `llama3`.
- **Enhancements**: Trained for non-professional legal knowledge Q&A (**2** hours of training).
- **Limitation**:Limited support for Chinese and limited dataset (**8000** pairs of non-professional Q&A).


# Introduction
Large Language Models (LLMs) have demonstrated strong universality in various fields. However, in vertical domains such as the legal field, the performance of these large models often leaves much to be desired. The reason lies in the fact that the legal field involves a vast amount of professional knowledge, complex legal principles, and highly refined rules and practices. Relying solely on general-purpose large models makes it difficult to achieve the ideal effect of legal consulting services.

To compensate for this deficiency, we have decided to develop the LawAI model, focusing on the application in the legal field. Our goal is to enable the model to deeply understand and apply legal knowledge through refined learning and training, thereby providing users with more accurate and reliable legal consulting services.

* Focused on the Legal Field: Unlike general-purpose large models, the LawAI model specializes in the legal field. Through the input of a large amount of legal professional knowledge and practical experience, it possesses a stronger legal professionalism.

* Refined Learning: We have conducted refined training for the model, including the study of legal provisions, analysis of cases, understanding of legal principles, etc., to ensure that the model can accurately grasp the core essentials of the legal field.


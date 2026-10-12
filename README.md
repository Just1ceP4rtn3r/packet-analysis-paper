# packet-analysis-paper

面向 Electronics 的网络入侵检测论文项目，围绕双层语义表示、跨流行为证据及并行的告警复判与跨流补充检测组织全文。现有 Introduction 保留原文，后续章节已建立带明确页预算的 22 页骨架。

一级章节采用 Introduction → Related Work → Methodology → Experiments → Discussion → Conclusions。任务定义作为 Methodology 的首个小节；Methodology 共 6 页，Experiments 共 7 页。

## 投稿与全文结构

- [投稿约束与项目约定](Agents.md)
- [七篇同刊结构分析、官方要求与本文逐小节预算](electronics_structure_plan_zh.md)
- [22 页骨架 PDF](src/build/main.pdf)
- [LaTeX 主入口](src/main.tex)
- [官方条款读取记录](research/electronics_author_guidance_evidence.json)
- [参考论文物理页码与章节测量](research/electronics_section_measurements.json)

按常规 Article 准备。Electronics 不设最大论文页数；22 页为本文写作预算。当前 PDF 有显式内容占位，后续填写作者、摘要、方法、结果及声明。

## 编译

需要安装含 `latexmk`、`pdflatex` 和 `bibtex` 的 TeX Live。在仓库根目录执行：

```sh
make -C src
make -C src verify
make -C src package
```

生成文件为 `src/build/main.pdf`；`verify` 核验实际页数及章节位置，`package` 生成可重编译的 `src/build/electronics-skeleton-source.zip`。模板与依赖说明见 [src/README.md](src/README.md)。

## 论文与资料

- [英文 Introduction](src/sections/introduction.tex)
- [参考文献](src/references.bib)
- [早期版本中文逐句译文](src/research/introduction_zh_translation.json)
- [早期版本中英逐句对应](src/research/introduction_zh_alignment.json)
- [同刊引言组织分析](src/research/electronics_intro_study.json)
- [Jev-IDS 引言分析](src/research/jev_ids_intro_study.json)
- [文献与实验组织笔记](reference_index.md)
- [引言组织笔记](intro_organization_zh.md)

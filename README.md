# packet-analysis-paper

面向 Electronics 的网络入侵检测论文项目，围绕统一协议语义、报文依赖和关键流证据组织 Introduction。

## 编译

需要安装含 `latexmk`、`pdflatex` 和 `bibtex` 的 TeX Live。在仓库根目录执行：

```sh
make -C src
```

生成文件为 `src/build/main.pdf`。模板与依赖说明见 [src/README.md](src/README.md)。

## 论文与资料

- [英文 Introduction](src/sections/introduction.tex)
- [参考文献](src/references.bib)
- [中文逐句译文](src/research/introduction_zh_translation.json)
- [中英逐句对应](src/research/introduction_zh_alignment.json)
- [同刊引言组织分析](src/research/electronics_intro_study.json)
- [Jev-IDS 引言分析](src/research/jev_ids_intro_study.json)
- [文献与实验组织笔记](reference_index.md)
- [引言组织笔记](intro_organization_zh.md)

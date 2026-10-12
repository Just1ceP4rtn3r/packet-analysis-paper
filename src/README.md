# Electronics Article 骨架

2026-10-12：按用户确认的常规 Article 要求扩展为 **22 页**全文骨架。Introduction 和 Related Work 已有英文正文；方法、实验等后续章节显示写作职责、图表占位及页预算。该稿采用官方投稿模板，后续正文与作者信息仍需填写。

## 全文预算与操作

| 页面 | 内容 |
| --- | --- |
| 1 | 标题、作者、摘要、关键词，以及骨架模式的预算总览 |
| 2–3 | Introduction，2 页 |
| 4 | Related Work，1 页 |
| 5–10 | Methodology，6 页；首个小节 3.1 Problem Formulation 占第 5 页 |
| 11–17 | Experiments，7 页 |
| 18 | Discussion 0.65 页 + Conclusions 0.35 页 |
| 19 | 文后声明，1 页 |
| 20 | Appendix A，1 页 |
| 21–22 | References，2 页 |

一级章节固定为 Introduction → Related Work → Methodology → Experiments → Discussion → Conclusions。`sections/framework.tex` 承载 Methodology，并在开头嵌入 `sections/problem_formulation.tex`；`sections/evaluation.tex` 承载 Experiments。

Electronics 无最大论文页数限制；本预算是本文组织选择。官方条款、七篇同刊逐章分析及小节职责见仓库根目录 `electronics_structure_plan_zh.md`，长期约束见 `Agents.md`。

```sh
make          # build/main.pdf
make verify   # 实际页数、章节位置、模板哈希、引用、摘要与关键词
make package  # build/electronics-skeleton-source.zip
```

PDF 使用 TeX Live 的 `latexmk`、`pdflatex`、`bibtex` 编译；核验另需 Python 3 标准库、Poppler 的 `pdfinfo` 和 `pdftotext`。源码归档包含已用依赖、官方模板、当前引用、各节源码和 PDF；解压后进入 `electronics-skeleton/` 运行 `make verify`。

`planning.tex` 提供 `\PlanPage`、`\Budget`、`\DraftText`、`\DraftFigure`、`\DraftTable` 等宏。规划分页发生溢出时编译报错，不会静默改变篇幅。预算分数表示写作目标，包含标题、文字及图表；实际章节起始物理页可通过 `build/skeleton_verification.json` 核对。图表编号遵循模板，附录表从 Table A1 开始。

完成正文时以真实内容替换占位，并在 `planning.tex` 将 `\planningtrue` 改为 `\planningfalse`，关闭预算提示及人为分页，恢复自然排版。正文填完后重新核对摘要、作者、声明、引用和篇幅；`verify` 是当前 22 页结构稿校验，预算变更后应同步更新脚本。

## 引言定位

英文引言采用“跨流行为证据需求 → 操作语义对齐与有界上下文 → 语义判别开销与 Jev-IDS → 双层语义表示 → 并行的告警复判与跨流补充检测 → 实验结果 → 两项贡献”的主线。告警复判针对全流快速评分产生的告警集合，提高精确率；跨流补充检测在全流范围独立选择具有跨流攻击线索的候选目标，提高召回率。工作标题为 **Malicious Traffic Detection through Unified Protocol Semantics and Packet Dependencies**。

## 文件与编译

Related Work 的英文初稿采用两个小节：Traffic Representation and Cross-Flow Semantics（0.55 页）与 Semantic Decisions and Computational Allocation（0.45 页）。比较依据是表示保留的信息、trace/目标流判定粒度、生成式或类型化判别接口，以及语义模型参与检测或告警解释的方式。末段对应并行的告警复判与跨流补充检测；Jev 作为已有模型使用。

| 文件 | 内容 |
| --- | --- |
| `main.tex` | 主入口，使用 `electronics,article,submit` 期刊选项 |
| `sections/introduction.tex` | 英文 Introduction 与两项贡献 |
| `sections/related_work.tex` | 英文 Related Work，两个小节共 1 页 |
| 其余 `sections/` 文件 | 任务定义、方法、评价、讨论/结论、声明和附录的骨架 |
| `planning.tex` | 仅用于结构稿的页预算、占位和分页宏 |
| `tools/verify_skeleton.py` | PDF 实际页数与章节起始页核验 |
| `tools/package_skeleton.py` | 可重编译的结构稿源码归档 |
| `references.bib` | 引言引用及已有研究文献条目 |
| `Definitions/` | MDPI 官方类、样式及资源，保留原文件 |
| `verse.sty` | 官方模板依赖的 CTAN 包，随项目提供 |
| `research/electronics_intro_study.json` | 七篇同刊引言和 contribution 的组织方式分析 |
| `research/source_manifest.json` | 早期引言的段落、主张与资料来源对应记录 |
| `research/feishu_*.json` | 本次读取的飞书章节快照 |
| `research/template_manifest.json` | 模板下载地址、版本和文件哈希 |
| `research/mdpi_template_original.tex` | 官方模板原始示例 |

在本目录执行 `make`。生成文件为 `build/main.pdf`；也可执行：

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

## 早期研究记录

本次逐篇阅读了七篇 Electronics 论文的 Introduction 和贡献列表。结构感知表示论文采用“可用信息 → 表示机制 → 结果与贡献”的推进方式；检测与解释论文在动机中建立证据定位的用途；[MeeDet](https://doi.org/10.3390/electronics15051017) 将检测质量、效率和解释各自对应到机制。本文将这些组织方式汇合到统一语义与依赖上下文这一条主线。各篇论文的标题、DOI、本地全文路径和具体映射见 `research/electronics_intro_study.json`。

方法描述来自[指定飞书文档的 Contribution 章节](https://mcniyfj5bw9b.feishu.cn/wiki/UmzGwARgmiUavpkhjclc847rnSh#XAfldQZfWoOpGQxJB9fcoAYcnee)，revision 112，以及上级目录中的资料。引言强调跨协议操作语义、报文依赖和端点角色怎样成为判别输入。[Tracegram](https://www.usenix.org/conference/usenixsecurity26/presentation/qu) 支撑跨流上下文与关键流用途，[关系感知 LLM 工作](https://www.techscience.com/CMES/v148n1/68212) 支撑已有跨流建模背景，[Jev 官方说明](https://docs.typesafe.ai/introduction) 支撑类型化判别接口。

2026-10-05 的修订纳入用户补充的 [Jev-IDS 预印本](https://arxiv.org/abs/2610.01079)。该文采用单流序列化状态和类型化输出；本文将研究问题推进到关联通信的统一操作语义、报文依赖及可回溯的流证据。引言依次说明已有表示保留的信息、仍需显式表达的行为信息，以及两层上下文与结构化判别如何承接这些需求。逐句中英对应见 `research/introduction_zh_alignment.json`，飞书译文位于 [Introduction（中文逐句译文）](https://mcniyfj5bw9b.feishu.cn/wiki/UmzGwARgmiUavpkhjclc847rnSh#doxcnGX5hDASjgPghIsMkgDOxAf)。

模板为 [MDPI 官方 ACS 版本](https://res.mdpi.com/data/MDPI_template_ACS.zip)，归档日期 2026-09-11，数字引用。参见[官方 LaTeX 指引](https://www.mdpi.com/authors/latex)和 [Electronics 作者指南](https://www.mdpi.com/journal/electronics/instructions)。

本机使用 TeX Live 2022。项目附带 [CTAN verse 包](https://ctan.org/pkg/verse)及其 LPPL 源文件，`main.tex` 为旧版内核提供文档元数据条件的兼容定义。依赖来源与生成步骤见 `research/verse_manifest.json`。

## 当前引言

2026-10-12 修订依据本次对话确认的中文稿和双路径方法定义。第一层统一消息操作语义，第二层围绕目标流组织跨流行为证据；判别阶段包括并行的告警复判与跨流补充检测。两项贡献分别为双层语义表示和兼顾精确率、召回率的双路径判别框架。

`references.bib` 新增 BACnet 语义检测（R12）、MISSION（R13）和 From Flows to Words（R14），并保留 Jev-IDS（R02）与 Jev 接口文档（R11）。结果段的数据集、比较模型和实验数值使用 `xxx` 占位。正文采用英文陈述句，结果段使用常规正文样式。

`research/` 中的逐句译文、对齐文件及来源记录属于早期版本；当前英文引言以 `sections/introduction.tex` 为准。标题保留描述性名称，作者、单位和摘要现在使用显式占位；正式内容完成后替换。

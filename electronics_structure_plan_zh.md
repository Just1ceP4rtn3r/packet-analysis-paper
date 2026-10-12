# Electronics 投稿要求、同刊结构分析与本文篇幅方案

核对日期：2026-10-12。对象为 **MDPI Electronics，ISSN 2079-9292，Article**。用户已确认按常规投稿要求完成，不设特刊截稿日期。本文方法定义以 `Agents.md` 和现有英文 Introduction 为准。

## 1. 投稿要求与来源

**Electronics 不设论文最大页数。本文的 22 页是写作预算，不是期刊上限。** 官方要求完整、简洁、可复现的方法与实验。[作者指南](https://www.mdpi.com/journal/electronics/instructions)、[Aims & Scope](https://www.mdpi.com/journal/electronics/about)。

| 项目 | 官方要求及性质 | 本项目处理 |
| --- | --- | --- |
| 投稿类别与范围 | Article 报告原创研究；范围包含 Networks、Computer Science & Engineering、AI | 按方法与检测系统研究组织；题名沿用当前稿 |
| 页数 | 无最大篇幅限制；所核对指南未给出 Article 最小页数、附录单独页数上限 | 22 页含首页、正文、声明、附录和参考文献 |
| 模板 | 接受 free-format 初投稿；鼓励官方模板，修回阶段按期刊格式整理 | 使用官方 MDPI ACS 模板，`electronics,article,submit,moreauthors,pdftex`；A4、单栏、审稿行号均由类文件控制 |
| 摘要 | 单段，约 200 词以内，隐含“背景—方法—结果—结论”顺序，不加小标题 | 留出 150–200 词的最终摘要位置；骨架摘要明确标记为占位 |
| 关键词 | 3–10 个 | 保留现有 6 个关键词 |
| 内容结构 | Introduction、Materials and Methods、Results、Discussion；允许 Results 与 Discussion 合并 | 第 3 节 Methodology 承担任务定义与方法，第 4 节 Experiments 承担实验设置及结果，第 5 节 Discussion 讨论 |
| 结论 | 详细章节说明称可选，free-format 清单又列出 Conclusions | 保留独立 Conclusions，满足两处表述 |
| 作者信息 | 作者全名、单位完整地址及通信作者；单匿名评审，审稿人可见作者身份 | 骨架显示作者、单位、通信信息占位；投稿前填实，不采用匿名会议模板 |
| 文后声明 | 多作者贡献、Funding、Data Availability Statement、Conflicts of Interest；伦理、知情同意按研究适用性填写 | 第 19 页预留声明；不替作者作“无资助”“无利益冲突”等事实承诺 |
| 数据与代码 | 提供支撑结果的数据、软件版本、复现信息；访问限制须写明；DAS 即使无新增数据也需要 | 公开数据链接、划分清单、解析配置、代码版本、Jev/API 版本与实验配置在正文及附录定位 |
| AI 使用 | 涉及文本、图形生成或研究设计等须按指南披露；纯拼写、语法、格式编辑有豁免 | 方法节和 Acknowledgments 保留具体工具、版本、用途及作者复核的填写位置 |
| 图表 | 按出现顺序编号，放在首次引用附近并有图题/表题；栅格图建议至少 600 dpi | 骨架使用可替换图表框，不改模板字号/页边距凑页；600 dpi 是建议，不写作绝对门槛 |
| 引用 | free-format 可用一致格式；期刊格式采用按出现顺序的数字引用，方括号、完整书目信息 | 使用 `mdpi.bst`；保留现有 BibTeX，未编造引文或实验数值 |
| 附录 | 可选；官方模板放在声明之后、References 之前；正文须引用；附录图表采用 A1、A2 等编号 | Appendix A 预留 1 页，放协议映射、问题/schema 与运行配置 |
| 补充材料 | 单独上传，可供审稿人审阅；列出材料名称和标题，采用 S1 等编号 | 长映射表、完整配置及逐攻击结果可作为补充材料；核心方法和主实验留在正文 |
| 上传文件 | LaTeX 须提供包含源码及图像的 ZIP，供编辑部重编译；所有文件合计不超过 120 MB | `make -C src package` 生成骨架源码归档及 PDF，保留依赖目录结构 |
| Cover letter | 每次投稿需附；说明意义、范围适配及作者同意、未一稿多投等声明 | 本轮记录要求，最终提交时依真实情况填写 |

上述条款主要来自[Electronics 作者指南](https://www.mdpi.com/journal/electronics/instructions)；模板与附录细节来自[官方 LaTeX 指引](https://www.mdpi.com/authors/latex)及仓库保存的官方 `src/research/mdpi_template_original.tex`。最新官方 ZIP 的 `mdpi.cls` 与本地文件 SHA-256 一致，版本为 2026-09-11。

访问记录：官方作者指南直连分别返回 HTTP 403/429，本轮通过 Jina Reader 读取该官方 URL 的完整页面，保存来源、传输说明及条款摘录于 `research/electronics_author_guidance_evidence.json`。没有将其他 MDPI 期刊或付费语言编辑服务的规则当作 Electronics 要求。特刊须另核对其 CFP、主题范围和截止日期，不能将任意特刊日期当作全刊截止日期。

## 2. 样本与页数测量

从用户已下载的 Electronics 论文中选取七篇，均提出并实现检测/分类方法并进行实证评价；E02、E03、E04、E05 与恶意流量检测更接近，E01、E06、E07 提供表示设计、组件验证和讨论结构参照。它们不是独立的“软件工具论文”专栏样本，不能据此推断期刊要求提供 GUI 或单设 Software 章节。

**页码采用 PDF 物理页码，从 1 开始。** 下表中 `p3–6 / 2.60` 表示章节从第 3 页开始、下一章节在第 6 页开始，实际占版约 2.60 页；首尾页由相邻章节共享。估算使用标题纵坐标，将每页正文区近似设为 y=70–790 pt；包含图表和留白，不是正文词数，也不是编辑部规定。共享页区间不能直接相加。精确边界、PDF 路径、哈希和提取到的子标题保存于 `research/electronics_section_measurements.json`。

| 样本（DOI 链接） | PDF 总页数 | 主要章节：物理页区间 / 约占版页数 |
| --- | ---: | --- |
| E01 [Beyond Byte-Level Modeling](https://doi.org/10.3390/electronics15091828) | 22 | Introduction p1–3 / 1.67；Related Work p3–6 / 2.60；Methodology p6–10 / 4.53；Experiments p10–20 / 9.91；Conclusions p20–21 / 0.79；声明 p21 / 0.36；References p21–22 / 1.28 |
| E02 [GCN-MHA](https://doi.org/10.3390/electronics14234627) | 20 | Introduction p1–2 / 1.15；Research Status p2–5 / 2.18；GCN-MHA Method p5–11 / 6.00；Experimental Analysis p11–18 / 7.84；Conclusions p18–19 / 0.32；声明/缩略语 p19 / 0.48；References p19–20 / 1.36 |
| E03 [MeeDet](https://doi.org/10.3390/electronics15051017) | 22 | Introduction p1–3 / 1.82；Related Works p3–4 / 0.94；MeeDet p4–9 / 5.25；Experiments p9–19 / 10.11；Conclusions p19–20 / 0.37；声明 p20 / 0.34；References p20–22 / 2.43 |
| E04 [Few-Shot Learning with Sample Relevance Guided Attention](https://doi.org/10.3390/electronics14234717) | 18 | Introduction p1–3 / 1.69；Fundamental Technologies p3–6 / 2.71；Proposed Approach p6–10 / 4.94；Experimental Design and Results Analysis p10–16 / 5.52；Conclusions p16 / 0.41；声明 p16–17 / 0.32；References p17–18 / 1.81 |
| E05 [Unsupervised Anomaly Detection and Explanation](https://doi.org/10.3390/electronics13224570) | 18 | Introduction（含 Related Work）p1–3 / 1.88；T-NAE p3–7 / 3.61；Cyber-Attack Detection and Explanation p7–9 / 2.78；Results and Discussion p9–14 / 4.16；Summary and Outlook p14 / 0.68；声明 p14 / 0.20；Appendices A–C p14–17 / 2.11；References p17–18 / 1.97 |
| E06 [Edge Exemplars Enhanced Incremental Learning](https://doi.org/10.3390/electronics14081589) | 27 | Introduction p1–3 / 1.33；Related Work p3–5 / 2.64；Method p5–14 / 8.87；Experiment p14–23 / 8.62；Discussion p23–25 / 1.87；Conclusions p25 / 0.45；声明 p25 / 0.26；References p25–27 / 2.29 |
| E07 [Fine-Grained Encrypted Traffic Classification](https://doi.org/10.3390/electronics14040778) | 19 | Introduction p1–2 / 1.11；Related Work p2–4 / 1.41；Preliminaries p4–6 / 2.09；Methodology p6–10 / 4.09；Experiments p10–15 / 5.28；Discussion p15–17 / 1.37；Conclusions p17 / 0.41；声明 p17 / 0.22；References p17–19 / 2.37 |

标题、摘要和作者块占各篇剩余的约 0.55–0.89 页。E06 的文本层含额外换页符，直接按 `pdftotext -layout` 的换页符会得到错误的 32 页；最终以 `pdfinfo` 和逐页坐标的 27 页为准。E05 有局部重复文本层，子标题需去重后解释。

## 3. 逐篇叙事与本文可采用的结构

### E01：按表示能力划分相关工作，按机制拆解实验

Related Work 按字节中心、部分结构、结构感知方法分类，最后收束到表示缺口。Methodology 按数据预处理、层级 token 化、输入嵌入、层级打乱预训练、注意力微调推进，先定义输入组织再给学习过程。

Experiments 先列数据集、清洗、设置和基线；§4.5（p13）给主要对比，§4.6（p15）测试预训练组合，§4.7（p16）测试层级聚合，§4.8（p17）扰动结构与内容，§4.9（p18）解释嵌入及注意力。它用独立证据回答“改善来自哪里”，而非只给一个总分表。本文可采用消息层/跨流层消融，并以端点关联和时间顺序扰动检查关系证据。这里借鉴的是验证逻辑，不把其加密应用分类成绩当作本文恶意检测基线成绩。

### E02：显式关系构造先于判别模型

Research Status 建立机器学习与图方法背景；方法章按连接图构造、时空特征融合、多头注意力权重展开。Experimental Analysis 的 §4.1–4.3 给环境、数据和指标；§4.4.1（p13）给结果，§4.4.2（p14）消融，§4.4.3（p16）方法比较。

本文应借鉴“先定义关联规则，再解释判别如何利用关联”的顺序，并在总架构中画清两条路径。该文的任务标签构造需要独立核对，不能把其应用/流量类别直接等同于本文的恶意标签，也不沿用其结果数字。

### E03：最适合本文的效果—效率—机制叙事

Related Works 很短，围绕 Mamba 和早退出两项技术展开。MeeDet 章按 Overview、Data Pre-Processing、Pretraining、Fine-Tuning with Early Exits、LLM-Driven Analysis 推进，每个模块都有检测系统中的位置。

Experiments 用 §4.1（p9–12）建立设置；§4.2（p12–15）依次报告一般恶意检测、APT 检测、效率；§4.3（p15）去除预训练、去除早退出、替换主干；§4.4（p16）分析退出层；§4.5（p17–19）呈现可理解性。其主干是任务成绩、运行代价和机制归因。本文将其改为“全流检测→同任务比较→双层语义→双路径→Jev 及总开销”，并区分 Jev 作为判别模型和 MeeDet 中 LLM 作为告警后解释器的不同职责。

### E04：每个自定义组件都有可定位的验证

Introduction 吸收相关研究，Fundamental Technologies 介绍注意力、MAML、原型网络；Proposed Approach 按 GADF 编码、类别稀疏注意力、特征融合、最近邻原型分类推进。实验设置后，§4.3（p13）比较元学习方法，§4.4（p14）比较其他方法，§4.5（p15）消融模块。

本文可借鉴“具体机制与具体对照成对出现”。Jev 属于已有模型，只需要接口语义、版本和调用位置；没有必要照搬约 2.7 页的通用技术教程。协议归一、上下文构建、折叠和路由则需要本工作自己的定义及控制实验。

### E05：两项能力分别给方法和证据，细节进入附录

Introduction 内含 Motivation、Related Work、Contribution and Organization。方法拆为 T-NAE 表示/重建与 Cyber-Attack Detection and Explanation 两章；后者明确阈值生成和注意力扰动。Results and Discussion 的 §4.1 定义 CIC-IDS-2017 子集与解释评价，§4.2 报检测结果，§4.3 评价解释。Appendices A–C 位于声明后、References 前，承接细节。

本文借鉴“不同能力分别验证”和附录布局。当前贡献是目标流检测与两条路径，不自动增加解释质量或关键流排名任务。包/流映射作为证据可追溯性，先用一个完整案例展示；如果后续主张解释正确率，才补独立真值和评价。

### E06：任务特异性足以改变篇幅分配

Method 包含 Tor 可插拔传输背景、增量学习和边缘样本增强。Experiment 先交代数据收集、指标及设置，再在 §4.4（p17）比较方法、§4.5（p20）做两机制组合消融、§4.6（p20–22）分析参数、§4.7（p22）比较时间与空间。Discussion 独立占约 1.9 页，围绕动态识别应用展开。

它说明方法背景、敏感性和部署分析可以按贡献增减；不说明每篇都应写 27 页。本文保留预算敏感性与运行代价，历史材料中的增量学习/在线适应不进入当前结构。

### E07：任务定义独立、方法先给总览

Related Work 后设置 Preliminaries，定义流、可观察元数据及建模基础。Methodology 先 Overview，再分时间特征、空间特征、训练优化。Experiments 从设置进入结果比较（p12）、消融（p13）、效率（p15），Discussion 独立，Conclusions 简短。

本文在 Methodology 的首个小节 3.1 Problem Formulation 中用一页讲清判别单位、上下文的可用时间和两个候选集合。这比增加一般 NIDS 或 LLM 教科书背景更能帮助理解系统。

## 4. 最终结构结论

**用户确认的六个一级章节为：Introduction → Related Work → Methodology → Experiments → Discussion → Conclusions。** 声明、Appendix 和 References 随后排列。任务定义并入 Methodology 的首个小节 3.1 Problem Formulation。Methodology 和 Experiments 沿用已阅读样本中的一级标题；具体方法与实验小节按本文贡献组织。

这是从已发表样本归纳出的写作选择，不是官方承诺的“偏好”，也不能据此计算接收概率。七篇中五篇有 5 个主要编号章节，一篇有 6 个，一篇有 7 个；其中 E05 的 5 章将两个方法阶段分开。Related Work 有独立或并入引言两种方式。编号章数并非固定条件。

共同特征是输入与任务清楚、方法按功能推进、实验先建立对照条件再检验贡献。六篇存在明确命名的模块消融；E05 的解释扰动也有机制验证用途，但不计为同名 Ablation Study。两篇有独立 Discussion，一篇明确采用 Results and Discussion，其余在实验和结论中讨论结果。本文将部署条件和适用范围集中到短 Discussion，保持主实验连贯。

样本总页数为 18、18、19、20、22、22、27，中位数 20 页。方法与实验合计约占全篇一半至七成（包含图表；E07 的独立 Preliminaries 另计）。本文给予 Methodology 6 页（其中任务定义 1 页）、Experiments 7 页，共 13 页；主要篇幅用于说明新增机制和展示证据。已完成引言保持原文，Related Work 压到 1 页，避免重复。

## 5. 本文 22 页预算与逐小节职责

| 页码 | 章节 / 小节 | 预算 | 叙事与计划图表 |
| --- | --- | ---: | --- |
| 1 | Title, authors, Abstract, Keywords | 1 页 | 摘要单段；骨架模式附篇幅总览，最终替换为真实首页内容 |
| 2–3 | 1. Introduction | 2 页 | 完整保留现有英文；预留摘要扩展后的排版调节空间 |
| 4 | 2. Related Work | 1 页 | 2.1 Traffic Representations and Cross-Flow Detection 0.4；2.2 Semantic and Typed Decision Models 0.35；2.3 Positioning of This Work 0.25；按任务和证据信息比较 |
| 5 | 3.1 Problem Formulation（属于 3. Methodology） | 1 页 | 3.1.1 Target Flows and Observable Evidence 0.5；3.1.2 Decision Paths and Processing Budget 0.5；定义目标流、历史窗、可观察协议信息、候选集合与最终输出 |
| 6 | 3.2 System Overview | 1 页 | 全流分叉总架构、模块输入输出、最终结果归属目标流；Figure 1 |
| 7 | 3.3 Message-Level Operational Semantics | 1 页 | 操作、资源、响应结果、端点角色；跨协议映射与源包标识；Table 1 |
| 8 | 3.4 Cross-Flow Behavioral Semantics | 1 页 | 以目标流为锚的端点/时间关联、事件顺序、统计事实、模板折叠和截断；Figure 2 |
| 9 | 3.5 Dual-Path Candidate Selection | 1 页 | 3.5.1 Alert Verification 0.5；3.5.2 Cross-Flow Discovery 0.5；后一候选集合从全流独立选择 |
| 10 | 3.6 Typed Decisions and Output Integration；3.7 Implementation and Reproducibility | 各 0.5 页 | Jev state/question/type/probability；实际阈值、重叠候选处理及融合；版本、运行边界；不预设旧版融合公式 |
| 11–12 | 4.1 Experimental Setup | 2 页 | 4.1.1 Datasets, Labels, and Temporal Splits 0.75；4.1.2 Baselines and Comparison Conditions 0.75；4.1.3 Metrics and Measurement Protocol 0.5；数据与对照表 |
| 13 | 4.2 End-to-End Detection and Same-Task Comparison | 1 页 | 全流总体 Precision/Recall/F1/FPR/PR-AUC 与每攻击类型结果；同任务方法主表；先回答整个系统是否有效 |
| 14 | 4.3 Semantic Representation Ablations | 1 页 | 去消息语义、去跨流上下文、去统计/折叠及关系扰动；固定 Jev、证据预算与工作点；表和关系效应图 |
| 15 | 4.4 Decision-Path Ablations | 1 页 | fast-only、+verification、+discovery、both；修正 FP、损失 TP、新检出 TP、新增 FP 同时报；Table 6 |
| 16 | 4.5 Jev Comparison and End-to-End Efficiency | 1 页 | 同证据/工作点/并发的判别器比较与全流水线分解；请求数、token、费用、吞吐、p50/p95；Figure 4 |
| 17 | 4.6 Budget Sensitivity and Evidence Case Study | 1 页 | 4.6.1 Context and Routing Budgets 0.6；4.6.2 Traceable Cross-Flow Evidence 0.4；预算曲线与源包/流案例 |
| 18 | 5. Discussion；6. Conclusions | 0.65 + 0.35 页 | 5.1 Deployment Conditions and Scope 0.4；5.2 Validity and Transferability 0.25；结论对应两项贡献和真实主结果 |
| 19 | Back Matter | 1 页 | 贡献、资助、伦理适用性、DAS、AI 使用、利益冲突及拟提交的补充材料 |
| 20 | Appendix A. Reproducibility Details | 1 页 | A.1 Protocol Mapping and Typed Interface 0.6；A.2 Configuration and Run Manifest 0.4；正文明确引用 |
| 21–22 | References | 2 页 | 当前真实引用先正常排版，其余空间明确标记为文献预算；不插入虚构参考文献 |

合计：首页 1 + 正文 17 + 声明 1 + 附录 1 + References 2 = **22 页**。正文中 Methodology 为 6 页（p5–10），Experiments 为 7 页（p11–17）。所有同页小节的预算包含小节标题、文字、图表和留白；PDF 上显示这些目标分配，二级小节的分数不声称为最终文字的实测占版。

## 6. 实验与两项贡献的对应

| 需要成立的判断 | 最低必要对照 | 观察量与呈现位置 |
| --- | --- | --- |
| 完整框架改善目标流检测 | 完整框架、快速检测器、同任务传统/深度模型、适用的跨流模型、Jev-IDS 式单流判别 | 全测试流总体指标及逐攻击结果，§4.2；不能只评价被选中的流 |
| 统一操作表达有用 | 归一化操作与相应原始字段输入；同判别器与 token 预算 | §4.3；保留目标流信息，按协议子集解释变化 |
| 跨流证据有用 | 目标流单独输入、真实邻接上下文、等长度随机邻流；端点关联/时间顺序扰动 | §4.3；跨流攻击子集需有可说明的标签/案例依据，不凭方法输出定义真值 |
| 统计与折叠控制开销且保留证据 | 各移除统计、折叠；说明相同预算时如何截断 | §4.3、§4.6；同时报告质量、token 和构建开销 |
| 两条路径各自承担精确率与召回率目标 | fast-only、fast+verification、fast+discovery、完整两路径 | §4.4；不能将 discovery 接在 alert-only 集合之后；报告收益与引入的错误 |
| Jev 的作用区别于上下文的作用 | 相同语义输入替换为生成式结构化判别器；原版 Jev-IDS 为单流方法参照 | §4.5；区分模型替换控制实验与完整方法比较，记录模型快照、输出约束及 token 预算 |
| 系统能处理全流负载 | 实际两路径系统、适用的全流语义调用参考；统一输入流量及测量工作点 | §4.5；包含解析、关联、候选选择、构建、网络/API、融合和重试，不用单次 API 延迟代替端到端延迟 |
| 预算选择有依据 | 上下文窗口/token 与路由预算扫描 | §4.6；用验证集选工作点，测试集只用于评价 |

数据集、最终基线和所有结果沿用 `xxx` 待定，不把历史笔记中出现的 CIC-IDS2017、UNSW-NB15 或路由率当作当前已经冻结的实验事实。可先筛选有 PCAP、时间戳、端点与可靠目标流标签的数据；只有预计算流特征的数据不足以直接验证消息操作语义。划分须控制主机、会话、时间窗口及上下文跨训练/测试泄漏，在线主张只使用判定时实际可见证据。

同任务方法主表采用各方法的完整实现及明确记录的输入条件；配对机制实验固定实际需控制的证据、模型与预算。不同流/trace 粒度须先定义映射，不能直接把不同论文的表格数值放在同一榜单。若使用统计区间，按捕获/主机时间块等独立性合理的单位计算，避免将相关流误当独立重复。完整主结果与预定控制条件均应报告，不能为了叙事隐藏不利结果。

## 7. 骨架交付与后续填写

`src/main.tex` 是主入口，`src/planning.tex` 控制预算提示和占位符，后续正文分散在 `src/sections/`。运行 `make -C src` 生成 `src/build/main.pdf`；运行 `make -C src verify` 核对 22 页、章节起始页和编译引用。`make -C src package` 生成 `src/build/electronics-skeleton-source.zip`，供离线解压重编译。

当前 PDF 是**采用投稿模板的篇幅规划稿**，作者、摘要、正文与结果尚有显式占位，不能作为完成的研究论文直接投稿。完成正式文本后移除占位内容，在 `src/planning.tex` 将 `\planningtrue` 改为 `\planningfalse` 关闭预算标签和规划分页，重新编译并复核内容、引用与声明。页数可以随证据需要调整；更新本预算表、LaTeX 标注及校验配置即可。

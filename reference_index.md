# Electronics 投稿参考资料索引

整理日期：2026 年 10 月 4 日。本文档服务于基于流量分析的恶意流量检测论文写作，覆盖相关工作、数据集、评价指标、实验对照和 Introduction 引用位置。

建议围绕一个核心问题组织论文：**怎样将异构协议报文及其依赖关系组织成有效、紧凑的判别上下文，使 Jev 同时支持恶意流量二分类和关键流定位，并在流量变化时维持检测能力。** 两层输入模型是方法主线，检测效果、归因质量、在线适应和运行效率是验证这条主线的证据。

## 文档入口

| 文件 | 用途 |
| --- | --- |
| [Introduction 中文组织建议](intro_organization_zh.md) | 7 篇已发表 Electronics 论文的引言结构分析、本文逐段逻辑和两项贡献草案 |
| [本地论文完整盘点](local_papers_inventory.csv) | 289 个 PDF 文件，按论文标识与部分副本内容匹配合并为 270 条检索记录；可按期刊、年份、DOI 和路径筛选 |
| [参考文献 BibTeX](references_selected.bib) | Electronics 27 篇及已核实核心文献的引用条目；键名与本文 E、R 编号对应 |
| [飞书读取快照](reference_materials/feishu/) | 授权文档三章及三张嵌入表格的原始返回与内容快照 |
| [PDF 可检索文本](reference_materials/pdf_text/) | 27 篇 Electronics 及 2 篇补充 LLM 工作的 pdftotext 输出，保留分页符 |

盘点覆盖本地 `05_recent_papers` 的 `pdf`、`selected_traffic_semantic_mapping`、`excluded_after_filter_audit` 和 `analysis` 中的 PDF。270 条记录中 254 条匹配到已有书目元数据，另外 16 条保留文件标识；盘点数量不表示全部论文已精读。Electronics 27 篇均提取了可检索全文，重点精读其中 7 篇的引言，并核查相关方法和实验段落。本次未运行检测模型。

## 1 资料来源与证据范围

| 来源 | 已读取内容 | 写作中的用途 |
| --- | --- | --- |
| [用户指定飞书文档](https://mcniyfj5bw9b.feishu.cn/wiki/IvP2wWXqJiawhGkGcrgcgTlUn4f) | Related work、数据集、Evaluation 三章；文档 revision 199 | 继承现有基线、复现入口和统一评价安排 |
| 飞书嵌入表格 `Cv7xsW7Z1hnuirtQW89cdhMinCl` | `sPcZiN` A1:B6、`nt2dcy` A1:B7、`O2yLZY` A1:B6；工作簿读取时 revision 194 | 论文与数据集对应、数据集频次、指标口径 |
| 本地 Electronics PDF | 2023—2026 年 27 篇 | 同刊写作结构及表示、图关系、少样本、解释、效率等相关工作 |
| [Tracegram 官方论文](https://www.usenix.org/system/files/usenixsecurity26-qu.pdf) | Introduction、§5.5、Discussion 等相关段落 | trace 级任务、关键流归因与归因评价 |
| 项目、模型与数据集官方页面 | Jev-IDS、TypeSafe、AOC-IDS、CARAVAN、NetMamba、CIC、UNSW 等 | 核实原型身份、输入要求、报告值和可复现范围 |

本文标记“作者报告”时，数值来自论文或项目报告；“建议”是针对你当前方法的研究与写作安排。你提供的方法和任务描述是本文定位的依据，尚未提供本文的实测结果。

## 2 最优先阅读的核心文献

### R01 Tracegram 与关键流归因

**Jian Qu 等，Tracegram: Framing Trace-Level Traffic Analysis with Temporally-Aware Multiple Instance Learning，USENIX Security 2026，6127–6146。** [论文页面](https://www.usenix.org/conference/usenixsecurity26/presentation/qu) · [PDF](https://www.usenix.org/system/files/usenixsecurity26-qu.pdf) · [官方代码](https://github.com/YuchenZhang-Academic/Tracegram)

以 trace 为多实例学习的集合、流为实例，通过流编码和时间感知聚合保留跨流关系，并产生关键流排序。§5.5 在 DAPT 上以注意力排名前 α% 的流覆盖多少真实恶意流衡量 Attribution Recall，作者报告前 10% 覆盖超过 95%。Discussion 将归因界定为相关性证据。

**本文引用位置：** 开篇说明单流之外的上下文价值、引出关键流归因需求，以及设计流排序与证据定位实验。**建议比较：** 时间与共现聚合和你构造的协议依赖、角色关系分别提供什么信息；统一 trace 构造和可见输入后比较。本文如输出单流标签，应将带上下文的单流判别与 trace 判别分别定义。

### R02 Jev-IDS 与类型化判别基线

**Paulo Severo、Silvio Quincozes、Amanda Dias，Jev IDS，2026 年公开研究原型。** [官方仓库](https://github.com/jev-sec/jev-ids) · [结果](https://github.com/jev-sec/jev-ids/blob/main/docs/results.md) · [实验协议](https://github.com/jev-sec/jev-ids/blob/main/docs/protocol.md)

输入单条流的特征、字段说明、类别定义和标注示例，返回攻击判别值与类别。已报告实验为 NSL-KDD 固定 2,000 条流、3 个示例种子；k 是每类示例数。k=1 时作者报告攻击类 F1 为 Jev 0.856、Gemini 0.880，延迟分别为 315 ms 和 2,421 ms。Gemini 的并发、拥堵与重试影响这个测量。仓库准备了 NF-UQ-NIDS-v2 入口，尚未报告相应结果。

**本文引用位置：** 方法选择和原始输入基线。**建议比较：** 保留原始流特征输入、统一报文表达输入、完整语义依赖上下文三种 Jev 配置，从而分辨收益来自基础模型还是你的上下文设计。仓库称其为独立研究原型；目前核实的材料不足以把它列为正式发表论文。

### R03 AOC-IDS 与在线检测

**AOC-IDS: Autonomous Online Framework with Contrastive Learning for Intrusion Detection，IEEE INFOCOM 2024。** [论文](https://arxiv.org/abs/2402.01807) · [全文](https://arxiv.org/html/2402.01807v1) · [代码](https://github.com/xinchen930/AOC-IDS)

采用流统计特征、自编码器、CRC 对比损失和统计决策，利用伪标签持续更新。作者在 UNSW-NB15 的五轮在线设置报告平均 Accuracy 89.19%、F1 90.14%；支持 UNSW-NB15 与 NSL-KDD。

**本文引用位置：** 分布变化、有限初始标签、持续适应。飞书资料记录其实现分别拟合训练与测试缩放器，统一比较时应复核代码版本，并改为仅用训练集拟合；原设置与统一设置分别出表。这里只继承该实现观察，本次没有重新运行代码。

### R04 CARAVAN 与低成本在线更新

**Caravan: Practical Online Learning of In-Network ML Models with Labeling Agents，USENIX OSDI 2024。** [论文页面](https://www.usenix.org/conference/osdi24/presentation/zhang-qizheng) · [PDF](https://www.usenix.org/system/files/osdi24-zhang-qizheng.pdf) · [artifact](https://github.com/Per-Packet-AI/Caravan-Artifact-OSDI24)

由标注智能体辅助小型检测模型更新，小模型承担在线检测。CIC-IDS2017 的标注源为 DNN，UNSW-NB15 为 GPT。作者报告的软件三任务均值包含设备分类，F1 改善 30.3%、GPU 重训练计算减少 61.3%。这两个数字分别描述更新后质量与更新计算成本。

**本文引用位置：** 持续变化下的标签与更新开销。**建议比较：** 窗口 F1、标注预算、更新触发次数、恢复时间和更新成本；软件仿真可先于 FPGA 实验复现。

### R05 TAD-GP 与 LLM 提示配置

**Efficient anomaly detection in tabular cybersecurity data using large language models，Scientific Reports 15，3344，2025。** [原文](https://www.nature.com/articles/s41598-025-88050-z)

将表格流量组织为 JSON，利用示例、引导提示和多轮交互判断正常或异常。飞书资料记录 CIC-IDS2017 单轮和多轮 F1 为 0.6047、0.7931；公开数据为各 20,000 条 JSON 子集，notebook 默认抽样规模又与此不同。本次浏览可访问论文页面，但未重新核算表格分数；数值沿用飞书已整理记录。

**本文引用位置：** 上下文组织影响 LLM 检测结果。**建议比较：** 相同输入、示例预算、轮数和测试样本下的生成式 LLM；延迟与吞吐需重新测量，论文标题中的 efficient 不能替代测速数据。

### R06 NetMamba 与字节模型效率

**NetMamba: Efficient Network Traffic Classification via Pre-training Unidirectional Mamba，IEEE ICNP 2024。** [论文](https://arxiv.org/abs/2405.11449) · [全文](https://arxiv.org/html/2405.11449) · [代码](https://github.com/wangtz19/NetMamba)

用报文头与载荷字节、单向 Mamba 和预训练实现流量分类。作者报告 USTC-TFC2016 Accuracy 99.60%、weighted F1 99.57%；batch=64 时吞吐为 YaTC(OF) 的 2.24 倍。输入需要 PCAP／字节，统计 CSV 无法等价替代。

**本文引用位置：** 预训练流量表示与运行效率。适合作为字节输入扩展基线；须统一计数单位、硬件、输入长度和预处理成本，并说明各模型可见信息。

### R07 跨流关系感知 LLM

**Aoran Huang 等，LLM-Driven Cross-Flow Modeling for Network Attack Traffic Detection，CMES 148(1)，2026，DOI 10.32604/cmes.2026.083972。** [出版社页面](https://www.techscience.com/CMES/v148n1/68212) · [本地 PDF](../05_recent_papers/excluded_after_filter_audit/cmes-computer-modeling-in-engineering-sciences/W7166542545__llm-driven-cross-flow-modeling-for-network-attack-traffic-detection.pdf)

通过流排序、分组和跨组采样构造上下文，以端点、端口、协议和统计相似性建立关系矩阵，并将关系偏置加入双向注意力；骨干冻结，新增表示与分类模块参与训练。原文含跨数据集和未见攻击评价。

**本文引用位置：** 与你最接近的“关系上下文＋大模型”工作之一。它虽在旧筛选归档中，仍应纳入此次方法对照。**建议区分：** 你的关系是否由报文请求响应、状态与业务角色推导，怎样统一不同协议，怎样压缩为 Jev 上下文；单纯“加入跨流关系”已有明确先例。

### R08 大参数 LLM 的流量映射与加速

**Xingshen Wei 等，Efficient Network Traffic Analysis Using Large-Parameter LLMs on Consumer-Grade GPUs，Mathematics 13，3754，2025。** [DOI](https://doi.org/10.3390/math13233754) · [本地 PDF](../05_recent_papers/pdf/mathematics/W4416595973__efficient-network-traffic-analysis-using-large-parameter-llms-on-consumer-grade-gpus.pdf)

采用 traffic-to-text 映射、LoRA 和稀疏感知推理优化，说明流量输入适配与大模型运行代价是独立研究问题。本文的建议是分别讨论“上下文保留了什么信息”和“判别过程花费多少时间”，并同时计入上下文构造成本。

### R09 上下文学习用于 NIDS

**Han Zhang 等，Large Language Models in Wireless Application Design: In-Context Learning-enhanced Automatic Network Intrusion Detection，2024。** [作者预印本](https://arxiv.org/abs/2405.11002) · [全文](https://arxiv.org/html/2405.11002v1)

比较三类上下文学习策略，支持通过示例改善检测、无需进一步微调的可能性。用于引出有限标注下的上下文适配。少样本结果依赖具体数据与示例选择，本文需用自己的实验验证。

### R10 LLM 用于 NIDS 的解释角色

**Paul R. B. Houssel 等，Towards Explainable Network Intrusion Detection using Large Language Models，2024。** [作者预印本](https://arxiv.org/abs/2408.04342) · [全文](https://arxiv.org/html/2408.04342v1)

比较 GPT-4、Llama3 与传统／Transformer 模型；报告直接恶意 NetFlow 检测存在精度问题，同时认为辅助解释具有应用潜力。用于界定 LLM 的解释价值和直接判别能力分别需要评价。

### R11 Jev 的官方接口与输出定义

**TypeSafe AI，Jev 模型说明。** [Introduction](https://docs.typesafe.ai/introduction)

官方描述为接收 state 和类型化问题、直接返回结构化决策；Choice、Score 和 Noul 的输出与置信度定义不同。多个问题在同一 state 上独立评价。本文方法部分应注明模型版本、问题类型、阈值和输出语义；API 输出值的校准性质需按官方定义和实测确认。**关键流排序需要本文自己定义的评分／扰动程序或显式证据输出，类型化结果本身不构成归因验证。**

## 3 Electronics 全部 27 篇索引

以下编号同时作为 BibTeX 引用键。优先级表示对本文问题的相关程度；7 篇重点论文另在 [Introduction 建议](intro_organization_zh.md) 中分析其引言。其余论文主要核查摘要、任务类型和可检索全文，不将引言模板观察推广为期刊强制要求。

### 3.1 优先阅读的 7 篇

| 编号 | 论文与入口 | 引用年 | 任务方向 | 本文用途 |
| --- | --- | --- | --- | --- |
| E01 | [Beyond Byte-Level Modeling: Structure-Aware and Adaptive Traffic Classification for Encrypted Networks](https://doi.org/10.3390/electronics15091828) · [PDF](../05_recent_papers/pdf/electronics/W7157222070__beyond-byte-level-modeling-structure-aware-and-adaptive-traffic-classification-for-encrypted-networks.pdf) | 2026 | 协议结构感知分类 | 字段、层和报文层级表示，层级 shuffle 预训练与门控融合；适合引用表示设计。文中 adaptive 指多层表示融合，在线更新需另行定义。 |
| E02 | [GCN-MHA Method for Encrypted Malicious Traffic Detection and Classification](https://doi.org/10.3390/electronics14234627) · [PDF](../05_recent_papers/pdf/electronics/W4416665868__gcn-mha-method-for-encrypted-malicious-traffic-detection-and-classification.pdf) | 2025 | 图关系与检测 | GCN 与多头注意力组织流间关系；适合方法和引言参考，实验的恶意标签构造见下文核查项。 |
| E03 | [MeeDet: Efficient Malicious Traffic Detection Method via Mamba-Based Early-Exit Mechanism in IIoT Scenarios](https://doi.org/10.3390/electronics15051017) · [PDF](../05_recent_papers/pdf/electronics/W7133129863__meedet-efficient-malicious-traffic-detection-method-via-mamba-based-early-exit-mechanism-in-iiot-scenarios.pdf) | 2026 | 高效检测与解释 | Mamba 预训练、动态早退出及告警样本的 LLM 解释；适合效率与证据解释评价。 |
| E04 | [Few-Shot Learning for Malicious Traffic Detection with Sample Relevance Guided Attention](https://doi.org/10.3390/electronics14234717) · [PDF](../05_recent_papers/pdf/electronics/W4416958570__few-shot-learning-for-malicious-traffic-detection-with-sample-relevance-guided-attention.pdf) | 2025 | 少样本恶意流量检测 | GADF 成像、元学习和样本关联注意力；Malicious_TLS、ToN-IoT 的 5-way 任务可参考，二分类需重新定义。 |
| E05 | [Unsupervised Anomaly Detection and Explanation in Network Traffic with Transformers](https://doi.org/10.3390/electronics13224570) · [PDF](../05_recent_papers/pdf/electronics/W4404567899__unsupervised-anomaly-detection-and-explanation-in-network-traffic-with-transformers.pdf) | 2024 | 无监督检测与解释 | Transformer 自编码器、报文与序列两级建模和注意力扰动；解释结果与专家真值比较，适合归因验证。 |
| E06 | [Edge Exemplars Enhanced Incremental Learning Model for Tor-Obfuscated Traffic Identification](https://doi.org/10.3390/electronics14081589) · [PDF](../05_recent_papers/pdf/electronics/W4409432169__edge-exemplars-enhanced-incremental-learning-model-for-tor-obfuscated-traffic-identification.pdf) | 2025 | 增量流量识别 | 面向 Tor 混淆流量类别变化的增量学习和样本记忆；适合作为适应实验组织参考，任务身份为流量识别。 |
| E07 | [Fine-Grained Encrypted Traffic Classification Using Dual Embedding and Graph Neural Networks](https://doi.org/10.3390/electronics14040778) · [PDF](../05_recent_papers/pdf/electronics/W4407627398__fine-grained-encrypted-traffic-classification-using-dual-embedding-and-graph-neural-networks.pdf) | 2025 | 双重表示与图分类 | 结合时间和空间／图表示，分类协议或应用流量；适合解释两种信息的互补作用。 |

### 3.2 表示与检测的 13 篇补充文献

| 编号 | 论文与入口 | 引用年 | 任务方向 | 本文用途 |
| --- | --- | --- | --- | --- |
| E08 | [AI-Based Malicious Encrypted Traffic Detection in 5G Data Collection and Secure Sharing](https://doi.org/10.3390/electronics14010051) · [PDF](../05_recent_papers/pdf/electronics/W4405809998__ai-based-malicious-encrypted-traffic-detection-in-5g-data-collection-and-secure-sharing.pdf) | 2025 | 加密恶意流量检测 | 5G 背景下的检测方法；适合补充同刊任务与数据表示背景。 |
| E09 | [L-GraphSAGE: A Graph Neural Network-Based Approach for IoV Application Encrypted Traffic Identification](https://doi.org/10.3390/electronics13214222) · [PDF](../05_recent_papers/pdf/electronics/W4403835185__l-graphsage-a-graph-neural-network-based-approach-for-iov-application-encrypted-traffic-identification.pdf) | 2024 | 图表示与应用识别 | L-GraphSAGE 用于车联网加密应用识别；可参考动态图与表示设计，应用识别指标单列。 |
| E10 | [STC-BERT (Satellite Traffic Classification-BERT): A Traffic Classification Model for Low-Earth-Orbit Satellite Internet Systems](https://doi.org/10.3390/electronics13193933) · [PDF](../05_recent_papers/pdf/electronics/W4403129571__stc-bert-satellite-traffic-classification-bert-a-traffic-classification-model-for-low-earth-orbit-satellite-in.pdf) | 2024 | 预训练与语义增强 | STC-BERT 的上下文预训练和关键 token 增强；应具体比较 token 表示与本文显式业务／依赖语义。 |
| E11 | [LG-BiTCN: A Lightweight Malicious Traffic Detection Model Based on Federated Learning for Internet of Things](https://doi.org/10.3390/electronics14081560) · [PDF](../05_recent_papers/pdf/electronics/W4409381865__lg-bitcn-a-lightweight-malicious-traffic-detection-model-based-on-federated-learning-for-internet-of-things.pdf) | 2025 | 轻量恶意流量检测 | LG-BiTCN 与联邦学习；适合轻量模型质量与运行预算的相关工作。 |
| E12 | [E2E-MDC: End-to-End Multi-Modal Darknet Traffic Classification with Conditional Hierarchical Mechanism](https://doi.org/10.3390/electronics14224457) · [PDF](../05_recent_papers/pdf/electronics/W4416334889__e2e-mdc-end-to-end-multi-modal-darknet-traffic-classification-with-conditional-hierarchical-mechanism.pdf) | 2025 | 多模态暗网分类 | E2E-MDC 的多模态和条件层级分类；任务标签与恶意二分类分别定义。 |
| E13 | [Network Traffic Classification Model Based on Spatio-Temporal Feature Extraction](https://doi.org/10.3390/electronics13071236) · [PDF](../05_recent_papers/pdf/electronics/W4393235404__network-traffic-classification-model-based-on-spatio-temporal-feature-extraction.pdf) | 2024 | 时空特征分类 | 时空特征提取；适合作为关系与时间信息的补充路线。 |
| E14 | [Machine-Learning-Based Traffic Classification in Software-Defined Networks](https://doi.org/10.3390/electronics13061108) · [PDF](../05_recent_papers/pdf/electronics/W4392912146__machine-learning-based-traffic-classification-in-software-defined-networks.pdf) | 2024 | 传统流量分类 | SDN 中的 ML 流量分类；可用于传统特征表示与业务分类背景。 |
| E15 | [Federated Distributed Network Traffic Classification Based on Deep Mutual Learning](https://doi.org/10.3390/electronics14244928) · [PDF](../05_recent_papers/pdf/electronics/W4417365063__federated-distributed-network-traffic-classification-based-on-deep-mutual-learning.pdf) | 2025 | 分布式流量分类 | 联邦分布式与深度互学习；多客户端协同学习的评价与本文在线适应分开。 |
| E16 | [Integrating Side-Channel Power Signals and Network Traffic for Machine Learning-Based Intrusion Detection in IoT](https://doi.org/10.3390/electronics15143114) · [PDF](../05_recent_papers/pdf/electronics/W7168521608__integrating-side-channel-power-signals-and-network-traffic-for-machine-learning-based-intrusion-detection-in-i.pdf) | 2026 | 多源入侵检测 | 联合功耗侧信道和网络流量；侧信道是额外输入，方法对照需标明可见信息。 |
| E17 | [Unlocking Few-Shot Encrypted Traffic Classification: A Contrastive-Driven Meta-Learning Approach](https://doi.org/10.3390/electronics14214245) · [PDF](../05_recent_papers/pdf/electronics/W4415721048__unlocking-few-shot-encrypted-traffic-classification-a-contrastive-driven-meta-learning-approach.pdf) | 2025 | 少样本加密分类 | 对比驱动的元学习；用于有限标签与少样本适配背景。 |
| E18 | [A Network Traffic Intrusion Detection Method for Industrial Control Systems Based on Deep Learning](https://doi.org/10.3390/electronics12204329) · [PDF](../05_recent_papers/pdf/electronics/W4387780154__a-network-traffic-intrusion-detection-method-for-industrial-control-systems-based-on-deep-learning.pdf) | 2023 | 工控入侵检测 | 多尺度卷积、通道注意力与 BiLSTM，关注漏报；可参考工控检测基线与逐类召回。 |
| E19 | [MFF: A Multimodal Feature Fusion Approach for Encrypted Traffic Classification](https://doi.org/10.3390/electronics14132584) · [PDF](../05_recent_papers/pdf/electronics/W4411673870__mff-a-multimodal-feature-fusion-approach-for-encrypted-traffic-classification.pdf) | 2025 | 多模态特征融合 | MFF 融合时序与统计信息、处理固定截断的信息损失；适合上下文完整性和输入预算实验。 |
| E20 | [Encrypted Traffic Detection via a Federated Learning-Based Multi-Scale Feature Fusion Framework](https://doi.org/10.3390/electronics15081570) · [PDF](../05_recent_papers/pdf/electronics/W7152660535__encrypted-traffic-detection-via-a-federated-learning-based-multi-scale-feature-fusion-framework.pdf) | 2026 | 多尺度图与联邦检测 | 空间、统计和内容三种图尺度；适合补充关系建模相关工作。 |

### 3.3 7 篇背景或相邻任务文献

| 编号 | 论文与入口 | 引用年 | 任务方向 | 本文用途 |
| --- | --- | --- | --- | --- |
| E21 | [Task Offloading Scheme for Survivability Guarantee Based on Traffic Prediction in 6G Edge Networks](https://doi.org/10.3390/electronics12214497) · [PDF](../05_recent_papers/pdf/electronics/W4388141242__task-offloading-scheme-for-survivability-guarantee-based-on-traffic-prediction-in-6g-edge-networks.pdf) | 2023 | 流量预测与卸载 | 预测负载并优化任务卸载；当前主任务相关度低。 |
| E22 | [WVETT-Net: A Novel Hybrid Prediction Model for Wireless Network Traffic Based on Variational Mode Decomposition](https://doi.org/10.3390/electronics13163109) · [PDF](../05_recent_papers/pdf/electronics/W4401353118__wvett-net-a-novel-hybrid-prediction-model-for-wireless-network-traffic-based-on-variational-mode-decomposition.pdf) | 2024 | 无线流量预测 | VMD 与混合预测模型；当前主任务相关度低。 |
| E23 | [Federated Learning Based on Mutual Information Clustering for Wireless Traffic Prediction](https://doi.org/10.3390/electronics12214476) · [PDF](../05_recent_papers/pdf/electronics/W4388040962__federated-learning-based-on-mutual-information-clustering-for-wireless-traffic-prediction.pdf) | 2023 | 联邦流量预测 | 互信息聚类与无线负载预测；当前主任务相关度低。 |
| E24 | [Data Traffic Prediction for 5G and Beyond: Emerging Trends, Challenges, and Future Directions: A Scoping Review](https://doi.org/10.3390/electronics14234611) · [PDF](../05_recent_papers/pdf/electronics/W4416730355__data-traffic-prediction-for-5g-and-beyond-emerging-trends-challenges-and-future-directions-a-scoping-review.pdf) | 2025 | 数据流量预测综述 | 5G 流量预测综述；需要网络负载背景时引用。 |
| E25 | [Traffic Classification and Packet Scheduling Strategy with Deadline Constraints for Input-Queued Switches in Time-Sensitive Networking](https://doi.org/10.3390/electronics13030629) · [PDF](../05_recent_papers/pdf/electronics/W4391486104__traffic-classification-and-packet-scheduling-strategy-with-deadline-constraints-for-input-queued-switches-in-t.pdf) | 2024 | TSN 分类与调度 | 截止时间约束下的调度和流量分类；当前主任务相关度低。 |
| E26 | [A Dynamic Website Fingerprinting Defense by Emulating Spatio-Temporal Traffic Features](https://doi.org/10.3390/electronics14224441) · [PDF](../05_recent_papers/pdf/electronics/W4416334798__a-dynamic-website-fingerprinting-defense-by-emulating-spatio-temporal-traffic-features.pdf) | 2025 | 网站指纹防御 | 指纹防御与时空特征；任务与本文恶意流量检测不同。 |
| E27 | [Evaluating Filter, Wrapper, and Embedded Feature Selection Approaches for Encrypted Video Traffic Classification](https://doi.org/10.3390/electronics14183587) · [PDF](../05_recent_papers/pdf/electronics/W4414098964__evaluating-filter-wrapper-and-embedded-feature-selection-approaches-for-encrypted-video-traffic-classification.pdf) | 2025 | 视频业务分类 | 比较特征选择及计算效率；可借鉴评价口径，业务标签与恶意标签分别保留。 |

E02 的方法与引言可作图关系参考。其 §4.2 Table 4 列出 ISCX-VPN2016 业务类别，Table 5 又赋予部分业务恶意标签／来源说明；采用其检测结论前需核实这种标签构造和数据来源。ISCX-VPN、Tor、暗网或应用类别本身不能直接替代正常／恶意标签。

## 4 本文主张与引用位置

| 本文拟建立的主张 | 适合引用的工作 | 本文需要提供的证据 |
| --- | --- | --- |
| 攻击判别需要报文、流及角色之间的联系 | R01、R07、E02、E07 | 相同事件在单流输入与关联上下文中的判别变化；真实事件案例 |
| 协议结构可补充字节或统计特征 | E01、E19、R06 | 普通解析表达、统一语义表达、依赖角色关系的逐层消融 |
| 示例和上下文配置影响判别 | R02、R05、R09、E04 | 控制 token、示例数和可见字段后的对照 |
| 关键流定位有助于分析人员核验 | R01、E05、E03、R10 | 带标签的流排序、证据回溯、删除／保留证据后的分数变化 |
| 分布变化要求持续适应 | R03、R04、E06 | 时间顺序流、变化前后窗口指标、恢复时间和固定更新预算 |
| 判别质量与运行效率应联合评价 | R02、R06、R08、E03、E11 | 同输入下的 F1—延迟／吞吐曲线及端到端成本 |

“协议归一化、统一语义表达、依赖角色关系”需要在方法中逐项定义。建议给出字段表、关系类型、构造规则和跨协议示例，使读者能够判断哪些信息来自普通解析，哪些来自新增语义机制。若第二层只由固定规则构成，应明确称为语义表示／语义抽象规则；若存在学习过程，给出训练目标和监督来源。

## 5 LLM 对本任务的优势及本文可继承的能力

下面的能力判断由相关文献支持或启发，转化为本文优势仍需要实验。尤其应区分自然语言预训练 LLM、在流量上预训练的 Transformer 和 Jev 类型化判别模型。

| 能力 | 文献依据 | 对本文的意义与验证方式 |
| --- | --- | --- |
| 将字段定义、业务背景和样本示例共同用于判断 | R05、R09；R02 提供 Jev 原型 | 同一流在补充字段含义／业务角色后是否更准确；控制输入长度 |
| 从少量上下文示例调整判别 | R09、R02 | 0、1、2、4、8 等示例预算曲线；同时保留完整训练集传统基线 |
| 利用跨流结构组织上下文 | R07、R01 | 比较时间邻接、端点相似与真实报文依赖，识别哪种关系有效 |
| 帮助解释和提炼调查线索 | R10、E03、E05 | 区分解释可读性、真实恶意流覆盖和对模型决定的忠实性 |
| 在异构场景中复用表示 | R08、R07 | 按协议／业务留出和跨环境评测；收益作为待检验假设 |

据此，Introduction 可以提出：**将流量翻译成保留协议语义与依赖的紧凑上下文，有望发挥模型对字段含义、示例和关系信息的利用能力；类型化判别为控制输出开销提供了实现途径。** Jev 官方文档支持直接结构化输出的机制描述；速度、精度、未见攻击与适应效果由本文数据证明。

语义相关恶意流量的验证应突出合法报文之间的关系：例如请求与响应的状态约束、角色与操作的匹配、跨流事件的业务关联。案例取自已有数据或实际测试记录，并标明模型在决策时能够观察的信息。分析重点是关系信息如何改变判别，避免仅按攻击名称推断模型理解了业务语义。

## 6 数据集选择与输入适用性

### 6.1 飞书五项工作的已报告数据来源

| 工作 | 已报告的检测／恶意相关数据 | 对本文的用途 |
| --- | --- | --- |
| R02 Jev-IDS | NSL-KDD | 原始方法校验；无法用表格恢复完整报文依赖 |
| R03 AOC-IDS | UNSW-NB15、NSL-KDD | 在线学习／有限初始标签基线 |
| R04 CARAVAN | CIC-IDS2017、UNSW-NB15 | 核心在线适应对照；辅助标注训练数据另记 |
| R06 NetMamba | USTC-TFC2016、CICIoT2022 | 字节模型和恶意任务扩展；其他正常应用分类单列 |
| R05 TAD-GP | KDD Cup 1999、CIC-IDS2017、UNSW-NB15 的 JSON 子集 | 生成式 LLM 对照；子集与原发行版分开 |

按飞书当前五项材料计数：UNSW-NB15 3 项、CIC-IDS2017 2 项、NSL-KDD 2 项，KDD Cup 1999／USTC-TFC2016／CICIoT2022 各 1 项；前两项计数包含有条件候选 TAD-GP。该频次反映当前候选集合的可比性。

### 6.2 建议的实验分工

| 数据 | 支持的输入与任务 | 建议的实验职责 | 需要固定的口径 |
| --- | --- | --- | --- |
| [CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) | 官方提供 PCAP、流特征 CSV 和攻击日程／标签信息 | 二分类、从 PCAP 构造协议依赖、按时间适应 | 原版／修订版、会话或 trace 构造、标签匹配、日期和攻击分布 |
| [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) | 提供原始捕获与特征材料；官方训练／测试表是独立发行形式 | 二分类、AOC／CARAVAN 对照；PCAP 适配另列 | 175,341／82,332 官方划分用于表格对照；重新构造 PCAP 流时记录映射与划分 |
| DAPT，入口见 R01 artifact | Tracegram 用于 APT 关键流案例及覆盖率评价 | trace／流定位、攻击阶段证据 | artifact 中的文件、trace 与流标签、阶段标签和构造方式须下载后核对 |
| NSL-KDD | 固定流特征表及标签 | Jev-IDS 原始方法与少样本对照 | 不能据此验证完整报文语义依赖；使用原始固定 split 或注明新划分 |
| Malicious_TLS、ToN-IoT | E04 的少样本任务资料 | 按协议与业务扩展，或有限标签场景 | 类别映射、PCAP 可得性、采样方式；5-way 结果与二分类结果分别出表 |
| USTC-TFC2016 | 正常应用与恶意软件流量，见 R06 | 字节预训练模型扩展 | 正常／恶意映射及完整训练和测试分离 |

建议至少保留一套能够回溯到原始 PCAP 的检测数据，以及一套能够核对真实关键流／攻击阶段的归因材料。只使用统计 CSV 的实验可以检验表格判别，却无法充分验证你新增的报文依赖与角色语义机制。

## 7 实验与指标的组织

以下为建议设计，尚无本文运行结果。主结果按“检测与归因”“在线适应”两组呈现，效率贯穿两组。

### 7.1 恶意流量二分类与语义机制

固定攻击为正类，报告攻击类 Precision／Recall／F1、Macro-F1、FPR；类别不平衡时补充 PR-AUC，并给出混淆矩阵。Accuracy 可作为补充。所有阈值和上下文超参数用验证集选择，至少 3 个种子报告均值与波动。

建议的核心基线是 RF、XGBoost、MLP／合适的序列模型、原始 Jev-IDS、生成式 LLM；AOC-IDS 和 CARAVAN 进入在线组，Tracegram 进入相同粒度的 trace／归因组，NetMamba／MeeDet 在 PCAP 和复现条件具备时扩展。

传统模型同时保留“与上下文模型等标签预算”和“完整训练集”配置。输入分两层比较：一组让各判别器接收等价信息以比较模型；另一组固定 Jev、改变上下文以证明输入设计。新增关系信息可再输入传统图／序列模型，区分信息收益与 Jev 的利用能力。

| 消融配置 | 检验的问题 |
| --- | --- |
| 原始流统计输入＋Jev | 相对于现有 Jev-IDS 的起点 |
| 普通协议解析与归一化报文表达＋Jev | 第一层表达的作用 |
| 统一语义表达＋Jev | 字段和角色含义的作用 |
| 完整语义表达与真实依赖图＋Jev | 关系建模的增量收益 |
| 相同节点与 token 预算、打乱依赖边 | 收益是否来自真实关系 |
| 完整上下文替换为时间邻接／端点关系 | 相对于一般上下文组织的差异 |
| 完整上下文＋生成式 LLM | 在同信息下比较判别质量与开销 |
| 协议／业务留出与未见攻击 | 泛化对象与语义关联检测能力 |

报告关系图大小、报文数、token 数和截断率，控制“加入语义”与“增加更多输入”的混杂。图中的角色从可观测行为或解析规则推导，训练／测试标签不能参与构图。跨集合划分以流、会话或 trace 为单位，防止同一事件的关联报文进入不同集合。

### 7.2 关键流归因

先定义二分类单位 u、关联流集合 F(u)、输出标签 y(u) 和每条候选流的归因分数 s(f,u)。如果检测单位本身是一条流，需说明关键流定位针对它的上下文集合还是针对另一个 trace；同时保留 packet_id、flow_id、时间戳与图节点的映射。

建议报告 Recall@k／Recall@α% 与 Precision@k；存在攻击阶段标签时补充阶段覆盖率。按 trace 计算后做宏平均，同时报告候选流数量分布。以原始恶意概率排序、时间邻近排序、随机排序和可复现的 Tracegram 作为候选基线。

以删除／屏蔽关键流后的判别变化检验证据的重要性，以仅保留关键流后的判别检验证据充分性。扰动应保持事件结构可解释，改变幅度按同样规模的随机流扰动校准。关键流标签覆盖、决定忠实性和案例可读性分别评价；流标签也不自动等同于“这条流对决定是关键”的标签。

如果通过多次 Jev 调用计算归因，记录额外调用数、token、延迟和费用。若利用类型化问题直接对候选流评分，仍需验证评分与真实攻击证据及扰动结果的一致性。

### 7.3 在线适应

在线适应的更新对象尚需按本文实现确定：上下文示例／记忆、语义规则、检测模型参数或其组合。若 Jev 权重固定而更新上下文，使用“上下文驱动的在线适应”并说明更新选择规则；模型参数训练属于另一个机制。

按时间推进，先预测当前窗口，再在允许的标签到达后更新；禁止使用未来报文／流／标签构造当前上下文。图构建和流完成等待也应计入检测时延。固定窗口、变化时点、更新预算、缓存容量及标签延迟，比较静态配置、定期更新、本文更新策略与 AOC／CARAVAN。

报告窗口 F1、攻击 Recall、FPR、变化后恢复时间、旧场景性能，以及标注／更新次数、更新时间、API 调用和 token 成本。少样本换一个静态测试集可以验证适配能力；连续流上的预测与更新才能支持在线适应结论。

### 7.4 质量与运行代价

同一硬件、batch 和并发下，报告 batch=1 的中位数／P95 延迟、固定批量的吞吐和失败率。GPU 测速预热并同步；本地模型与 API 模型分别记录硬件配置或服务版本、访问日期、重试和并发。

时间分解为：报文解析与流构造、依赖／角色图更新、上下文组装、检测调用、归因、在线更新。给出纯检测调用和端到端检测结果，归因与更新成本另列。API 墙钟时间和本地纯 GPU 时间可描述实际部署开销，但其条件差异应保留。flows/s、packets/s、traces/s 和整批耗时各自记录。

## 8 两项贡献的写作定位

建议将第一项贡献写成“**统一语义与依赖上下文驱动的检测和归因机制**”，把二分类和关键流归因作为机制支持的能力；第二项写成“**面向流量变化的在线适应与质量效率验证**”，按实际更新对象补全机制。检测效果和在线实验负责证明贡献，段落中同时交代新机制及其带来的能力。

你目前描述的“比 LLM 快”“比传统训练模型准”“能发现语义相关恶意流量”适合作为实验主张。填入正文时分别注明数据、输入条件、训练／示例预算、指标和比较对象。此前文献中的 7.7 倍、2.24 倍或 F1 分数均为作者报告值，不能转写成本文结果。

完整的逐段引言安排、7 篇 Electronics 的可借鉴结构和中文起草文本见 [Introduction 中文组织建议](intro_organization_zh.md)。

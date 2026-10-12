# 论文定位、投稿约束与章节约定

本文件供论文写作、实验组织和 LaTeX 修改使用。研究定义以用户最新确认和 `src/sections/introduction.tex` 为准；历史研究笔记和旧图据此核对。本项目约定文件采用 `Agents.md`，不维护大小写不同的重复文件。

## 研究问题与贡献

- 目标期刊为 **Electronics（MDPI）**，英文 **Article**，按常规投稿准备。
- 当前标题为 **Malicious Traffic Detection through Unified Protocol Semantics and Packet Dependencies**。
- 判别对象为目标流；关联流提供上下文，最终输出对应目标流的正常/恶意判断。
- 第一个挑战是异构操作对齐与跨流证据组织：统一操作、资源、响应结果和端点角色，在有限上下文中保留支持目标流判定的交互及顺序。
- 第二个挑战是语义计算分配与开销控制：同时支持告警核验和跨流攻击发现，控制上下文大小与调用范围。

两项贡献分别为：

1. **双层语义表示。** 第一层是消息操作语义（message-level operational semantics）；第二层是跨流行为语义（cross-flow behavioral semantics）。第二层围绕目标流，按端点与时间关联组织通信历史、客户端活动、服务端响应及事件顺序。确定性统计提取计数、速率、响应差异；模板折叠压缩重复消息，保留关键变化和到源包/流的映射。
2. **双路径语义判别框架。** 告警复判（alert verification）核验快速检测器在全流评分后产生的告警集合，目标为改善 precision。跨流补充检测（cross-flow discovery）独立从全流选择候选，目标为改善 recall。两条路径并行，不能画成或写成告警筛选后的单条串行链。

Jev 是既有模型，按 state 和类型化问题直接返回判别概率。Jev-IDS（R02）已研究单流类型化入侵检测；接口文档为 R11。本文创新集中于证据组织与双路径机制。快速检测器的双视角与双层语义表示是不同概念。支持多协议表示与关联同一攻击中的跨协议交互也需分别验证。

## Electronics 常规 Article 要求

以下条款在 2026-10-12 核对，来源为[作者指南](https://www.mdpi.com/journal/electronics/instructions)、[Aims & Scope](https://www.mdpi.com/journal/electronics/about)、[官方 LaTeX 指引](https://www.mdpi.com/authors/latex)及仓库中的官方模板示例 `src/research/mdpi_template_original.tex`。正式投稿前复查官方页面。

| 项目 | 项目执行规则 |
| --- | --- |
| 页数 | **无最大论文页数限制**；未查到 Article 最小页数或附录独立页数上限。22 页是写作预算。 |
| 模板 | 初投允许 free-format，修回按期刊格式。本稿使用官方 MDPI ACS，选项 `electronics,article,submit,moreauthors,pdftex`。不修改 `Definitions/`、页边距或字号凑页。 |
| 摘要与关键词 | 单段摘要按约 200 词以内执行，无小标题，结果与正文一致；关键词 3–10 个。 |
| 内容 | 覆盖引言、材料与方法、结果及讨论；结果和讨论允许合并。详细说明称结论可选，free-format 清单列有结论，本稿保留。 |
| 作者 | 填写真实姓名、单位完整地址、通信作者及邮箱；采用单匿名评审，不套用匿名会议规则。 |
| 声明 | 填写实际作者贡献、资助、DAS、利益冲突，伦理及知情同意按研究适用性填写。无新增数据也需 DAS；不自动替作者声明“无资助”等事实。 |
| 复现 | 写明软件版本、代码/数据可用性、配置和必要访问限制。 |
| AI 使用 | 涉及文本、图形生成或研究设计等，按指南在方法及致谢披露工具、版本、用途和作者复核；纯表层语言修改的豁免不自动覆盖研究设计。 |
| 图表与引用 | 图表靠近首次引用，依出现顺序编号并给标题。栅格图建议至少 600 dpi。参考文献采用按首次出现排序的 MDPI 数字样式，信息完整。 |
| 附录 | 可选，置于声明之后、References 之前，正文引用，图表采用 A1、A2 等编号。 |
| 补充材料 | 单独列明名称、标题，使用 S1 等标识，随稿供审稿人查阅；其中引用纳入主文参考文献。核心方法和主实验留正文。 |
| 文件 | LaTeX 提供可重编译源码 ZIP，含必要图像、参考文献、类和样式，并准备 PDF；所有上传文件合计不超过 120 MB。 |
| Cover letter | 正式投稿需要；说明贡献和范围适配，依真实情况确认作者批准、未同时投其他期刊。 |

模板版本为 2026-09-11，本轮重新下载的官方类与本地哈希一致。作者指南直连受限，本轮经 Jina Reader 读取官方页面，条款及来源记录保存在本地 `research/electronics_author_guidance_evidence.json`。模板核对记录为 `research/electronics_template_recheck.json`；`research/` 按当前忽略配置作为本地资料保留。

## 用户确认的六章结构

**Introduction → Related Work → Methodology → Experiments → Discussion → Conclusions**。

| 章节 | 页码 | 预算 |
| --- | --- | ---: |
| 首页：题名、作者、摘要、关键词 | 1 | 1 页 |
| 1. Introduction | 2–3 | 2 页 |
| 2. Related Work | 4 | 1 页 |
| 3. Methodology | 5–10 | 6 页 |
| 4. Experiments | 11–17 | 7 页 |
| 5. Discussion / 6. Conclusions | 18 | 0.65 / 0.35 页 |
| 文后声明 | 19 | 1 页 |
| Appendix A | 20 | 1 页 |
| References | 21–22 | 2 页 |

任务定义是 **3.1 Problem Formulation**，含 3.1.1 Target Flows and Observable Evidence 和 3.1.2 Decision Paths and Processing Budget。随后为 3.2 System Overview、3.3 Message-Level Operational Semantics、3.4 Cross-Flow Behavioral Semantics、3.5 Dual-Path Candidate Selection、3.6 Typed Decisions and Output Integration、3.7 Implementation and Reproducibility。

Experiments 依次为：4.1 Experimental Setup（2 页）；4.2 End-to-End Detection and Same-Task Comparison；4.3 Semantic Representation Ablations；4.4 Decision-Path Ablations；4.5 Jev Comparison and End-to-End Efficiency；4.6 Budget Sensitivity and Evidence Case Study（后五项各 1 页）。

七篇本地同刊样本的范围为 18–27 页、中位数 20 页；样本支持组织方式选择，不证明期刊固定偏好或接收概率。逐篇章节分析及逐小节预算见 `electronics_structure_plan_zh.md`。

## 实验与写作一致性

- 同任务完整方法比较与同证据模型替换实验分别描述。使用一致的任务粒度、标签和指标，不把不同论文中的成绩直接拼成排行榜。
- 双路径消融包含 fast-only、+verification、+discovery、both。按全测试流统计，discovery 始终独立从全流选择；同时报告修正 FP、损失 TP、新检出 TP、新增 FP。
- 语义消融覆盖消息操作表示、跨流上下文、确定性统计和模板折叠；关系扰动检验端点、时间顺序或等长随机邻流。明确固定的模型、证据和预算。
- Jev 效率比较保留已确认的输入证据、检测工作点与并发口径，不自动增加“相同候选流集合”等条件。总开销包含解析、关联、路由、构建、网络/API、融合和重试；区分单调用、观察等待与端到端处理延迟。
- 数据划分检查时间、主机/会话及上下文跨集合泄漏。阈值用验证集确定；数据集、基线、融合公式和结果未冻结时写 `xxx`，不把旧笔记当作当前实测事实。
- 精确率（precision）与总体准确率（accuracy）区分。正文围绕机制和证据；保持论断的技术范围限定。完整报告预定对照及相关结果。
- 关键流归因、在线适应、旧版单调融合等历史方案，需用户确认后才能进入当前贡献或架构。

## 文件与验证

- Introduction 为 `src/sections/introduction.tex`，本轮章节调整保留其原文。
- 主入口 `src/main.tex`；`sections/framework.tex` 承载 Methodology，在开头嵌入 `sections/problem_formulation.tex`；`sections/evaluation.tex` 承载 Experiments。
- `src/planning.tex` 显示预算和占位，超页编译报错。正式内容完成后替换占位并设置 `\planningfalse`，恢复自然分页。
- `make -C src verify` 核对 22 页 A4、实际章节起始页、引用、模板哈希和摘要/关键词。页预算变化时同步修改文档、LaTeX 和校验脚本。
- `make -C src package` 生成 `src/build/electronics-skeleton-source.zip`。当前 PDF/ZIP 是结构占位稿，需填写实际内容后才能投稿。

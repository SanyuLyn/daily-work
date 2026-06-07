# 技术日报 2026-06-07

## Flutter

### [Flutter 发布官方 Skills，Flutter 在 AI 领域再添一助力](https://zhuanlan.zhihu.com/p/2012886441642975382)
**摘要**：Flutter 官方正式发布 flutter/skills，一个专为 AI Agent（Claude Code、Cursor、Copilot 等）设计的技能库，通过 Skills CLI 调用 Gemini 将官方文档转化为可执行的 SKILL.md 文件，为 AI 提供标准化的 Flutter 工程操作流程。此举配合已有的 Flutter MCP 和 GenUI 能力，构建起完整的 AI 辅助 Flutter 开发生态。MCP 负责外部数据接入，Skills 负责专业知识与流程封装，两者互补共同提升 AI 在 Flutter 项目中的实际产出质量。

### [Flutter 鸿蒙 2026 路线发布，加速同步官方生态，进一步优化体验](https://zhuanlan.zhihu.com/p/2016571565735682780)
**摘要**：Flutter HarmonyOS 社区（Flutter-OH）正式发布 2026 路线图，最大变化是大幅压缩版本同步周期——目标从过去 7 个月以上缩短至约 4 个月，逐步跟上官方 Flutter 季度发布节奏（当前最新官方版为 3.41）。路线图还规划了 2026 年内完成至少 200 个高优先级三方库适配，覆盖网络、数据库、图像处理、音视频、地图等常用领域，并由 Flutter SIG 承担主导维护职责，治理结构进一步规范化。

### [Flutter Web 正式移除 HTML renderer，只支持 CanvasKit 和 SkWasm](https://zhuanlan.zhihu.com/p/11809045697)
**摘要**：Flutter Web 正式废弃 HTML 渲染器，仅保留 CanvasKit 与 SkWasm 两种后端。SkWasm 凭借更优的运行时性能成为推荐首选，CanvasKit 作为兼容后备。此变更对所有 Flutter Web 项目均有影响：构建配置需核查渲染器参数，HTML 渲染器特有的降级行为将不再可用，依赖 HTML renderer 的平台渗透策略需重新评估。

### [2026 年鸿蒙跨平台开发：Flutter、React Native 及其他框架前瞻](https://zhuanlan.zhihu.com/p/2000910086613255920)
**摘要**：全面前瞻 2026 年鸿蒙跨平台生态格局。Flutter-OH 与 React Native 鸿蒙版持续演进，Taro、uni-app 等国产框架也在加快鸿蒙适配步伐。文章对比各框架在鸿蒙平台的成熟度、三方库覆盖率及社区活跃度，认为 Flutter-OH 在原生渲染一致性上具备优势，而 React Native 鸿蒙版则更适合已有 RN 代码迁移场景，开发者需结合团队技术栈和项目周期综合选型。

---

## Android

### [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://zhuanlan.zhihu.com/p/2009937286335308608)
**摘要**：本文梳理 Android 17 的主要适配要点，同时详细解析 Google 2026 年推进的开发者身份验证与侧载限制政策。新规核心在于：从 2026 年 9 月起，部分地区安卓设备上运行的应用必须由经过身份验证的开发者发布；未经验证渠道安装的应用将面临强制六步验证流程与 24 小时强制等待期。文章还盘点了 targetSdkVersion 升级、后台限制、通知权限等 Android 17 开发侧的关键适配项。

### [Google 发布 Android CLI：打造面向 Android 工程的 Agent 能力](https://zhuanlan.zhihu.com/p/2029480482035737404)
**摘要**：Google 发布 Android Agent 开发工具包，由 Android CLI、Android Skills 和 Android Knowledge Base 三大组件构成。Android CLI 定位为"终端侧 Android 开发主入口"，可在 Android Studio、Gemini CLI 或第三方 Agent（如 Claude Code）中统一调用，实现环境初始化、项目创建、模拟器控制等核心操作。实测数据显示，引入 Android CLI 后 token 消耗降低 70% 以上，任务完成速度提升约 3 倍。

### [Android CLI 来了！终端一键建项目、控模拟器、给 Agent 喂官方规范](https://zhuanlan.zhihu.com/p/2029843582178137700)
**摘要**：Android CLI 实操上手指南，详解如何通过命令行一键完成 Android 项目创建、AVD 模拟器管理及 ADB 操作，并介绍如何将 Google 官方 Android 规范注入 Agent 上下文，从而让 AI 生成更符合最佳实践的代码。文章指出 Android CLI 特别强调轻量化与可编程性，适合 CI/CD 流水线和 Agent 自动化场景集成。

### [如何看待谷歌逐步收紧安卓应用侧载计划？](https://www.zhihu.com/question/2019018192186557023)
**摘要**：知乎社区对 Google 收紧侧载政策的多角度讨论。支持者认为此举有助于打击恶意应用、提升生态安全；反对者则担忧用户自主权受损，国内 Android 用户依赖侧载安装 Google 服务的路径将受阻，同时对中小开发者的分发门槛提高表示忧虑。多位答主指出此政策与 iOS 生态封闭化趋势方向一致，长期来看或推动 HarmonyOS 等替代生态加速发展。

---

## iOS

### [iOS/iPadOS 26.5 正式版发布！新壁纸 + RCS 加密，大量 Bug 修复](https://zhuanlan.zhihu.com/p/2037595671025422489)
**摘要**：苹果推送 iOS/iPadOS 26.5 正式版，最大亮点是 **RCS 端到端加密**——iPhone 与 Android 用户互发 RCS 消息时现支持加密保护，安全级别媲美 iMessage，加密消息显示专属小锁图标。此外带来多款新彩虹壁纸，地图应用加入广告位，本次共修复 52 个安全漏洞（含 6 个内核漏洞、10 个 WebKit 漏洞），是近期安全补丁量最大的版本之一。

### [苹果 iOS 26.5.1 正式推送：纯修复版本，仅适配两款机型，解决低电量充电故障](https://zhuanlan.zhihu.com/p/2045208112328594133)
**摘要**：苹果于 6 月 2 日推送 iOS 26.5.1（内部版本号 23F81），定向修复特定机型在低电量状态下的充电异常故障，属于小范围精准修复版本，不带新功能。适用机型极为有限，不符合条件的设备不会收到推送提示，建议受影响用户优先升级。

### [WWDC 2026 前瞻：iOS 27 重磅曝光！AI 健康 + Siri 升级 + 跨设备功能齐发力](https://zhuanlan.zhihu.com/p/1984367858281641787)
**摘要**：iOS 27（内部代号"Rave"）前瞻报道，核心定位类似 macOS Snow Leopard——以系统底层优化为主轴，清理历史遗留代码、重写系统组件，目标大幅提升响应速度与续航。AI 层面：Siri 将获 IntelligenceFlow 与 SpotlightSearchToolLLMQueryUnderstanding 新能力，Health+（AI 驱动健康订阅服务）计划同期推出，视觉智能、写作工具与照片编辑亦将深度整合 Apple Intelligence。

### [苹果 WWDC 2026 官宣定档！6 月 9 日开幕，iOS 27 与 AI 升级成重头戏](https://zhuanlan.zhihu.com/p/2019838432499745435)
**摘要**：Apple 正式宣布 WWDC 2026 主题演讲定于北京时间 6 月 9 日凌晨 1 点开幕，iOS 27、iPadOS 27、macOS 及 Apple Intelligence 新一轮升级为核心议程。业界预期本次大会还将展示 M5 系列芯片及新款 Mac mini，同时 Apple Intelligence 的多语言扩展与第三方 AI 集成也将有新动作，是苹果近年来规格最受期待的 WWDC 之一。

---

## AI / 大模型

### [国内外知名大模型及应用——模型/应用维度（2026/06/01）](https://zhuanlan.zhihu.com/p/670574382)
**摘要**：截至 2026 年 6 月 1 日的大模型全景速览。国际第一梯队：Claude 4.7、GPT-5.5、Gemini 3.1 Pro 持续领跑，百万 token 上下文已成标配。国产追赶势头强劲：阿里 Qwen3-Coder、月之暗面 Kimi K2 Thinking、MiniMax M2、DeepSeek V3.2 表现突出，DeepSeek V4 Pro 凭借极低定价（仅为 Claude Sonnet 同类约 1/400）和 90% 顶流水准的性能，成为性价比之王。大模型迭代节奏已从"年更"演变为"季更"乃至"月更"。

### [2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！](https://zhuanlan.zhihu.com/p/2038200846148704182)
**摘要**：对 Claude 4.7、GPT-5.5、Gemini 3.1 Pro、DeepSeek V4 Pro、Qwen3-Coder、小米 MiMo Agent 六款模型的 AI 编程实测对比。Claude Code 蝉联 SWE-Bench 和 Aider Polyglot 双料冠军，是复杂工程任务首选；Gemini 3.1 Pro 以百万级上下文称霸长代码理解；DeepSeek 以极低成本完成高质量代码生成；小米 MiMo Agent 在 token 消耗上有显著优化。整体来看，引入 AI 编程助手可将迭代效率提升一倍以上。

### [Gemma 4 vs Qwen 3.5：开源大模型的"双雄对决"，开发者该如何选择？](https://zhuanlan.zhihu.com/p/2024063273872400836)
**摘要**：深度对比 Google Gemma 4 与阿里 Qwen 3.5 两款主流开源大模型。Gemma 4 26B-A4B 采用 MoE 架构（128 个专家，每次激活 8 个），以接近 4B 的算力实现 26B 智能输出，Apache 2.0 授权对商业项目友好；Qwen 3.5 27B 在纯英文文本任务和静态 Benchmark 上略胜，速度更快，适合隐私敏感的本地部署。综合建议：商业项目和多语言场景选 Gemma 4，速度优先的英文本地部署选 Qwen 3.5。

### [大模型迭代加速：2026 年 4 月已经发布 / 预期发布的 AI 大模型](https://zhuanlan.zhihu.com/p/2024418051664168470)
**摘要**：梳理 2026 年 4 月前后密集发布的主要 AI 大模型，包括智谱 GLM-5V-Turbo（多模态增强）、MiniMax M2.7（Agent 场景优化）、Trinity Large Thinking（超长推理链专项）以及 Google Gemma 4（开源轻量高性能）等。文章以时间轴形式展示大模型发布频率显著加快的趋势，并分析各模型在推理能力、多模态支持、本地部署适配三个维度上的差异，帮助开发者快速把握当前技术窗口。

---

## 行业动态

### [直击 Google I/O 2026 | 轰炸式发布 Agent，狙击 Claude Code，开战！](https://zhuanlan.zhihu.com/p/2040377883764512059)
**摘要**：Google I/O 2026 召开，发布密度创历届之最。重点产品：**Gemini 3.5 Flash**（声称比同类前沿模型快 4 倍，代码/推理/多模态均超 Gemini 3.1 Pro）；**Gemini Omni**（全模态世界模型，支持视频生成与多轮物理一致性对话）；**Antigravity 2.0**（编程 Agent，直接对标 Claude Code）；以及与三星联合发布的首款 **Android XR AI 眼镜**（Gemini 驱动，支持实时翻译、导航和上下文感知）。Gemini CLI 同期正式退出，统一归并至 Antigravity 体系。

### [AI 行业动态 20260516：微软研究——AI 智能体在长任务流程中仍不可靠](https://zhuanlan.zhihu.com/p/2038879852984530318)
**摘要**：微软研究院发布 DELEGATE-52 基准，覆盖 52 个专业领域，测试结果显示当前主流前沿模型在长流程多步骤任务中频繁出现文档损坏或内容丢失，仅 Python 编程场景勉强达到生产可用标准，而配备工具调用能力的 Agent 反而表现更差。METR 的独立测试亦证实：截至 2026 年 4 月，Agent 完成 4 小时任务的成功率仅为 50%。这一发现与 OpenAI 联合创始人 Andrej Karpathy 的判断一致——当前 AI Agent 在上下文记忆与长程规划方面仍存在根本性缺陷。

### [2026 年各大科技巨头对 AI 的趋势预测](https://zhuanlan.zhihu.com/p/2011108769992577031)
**摘要**：综合分析 Google、微软、Meta、英伟达等科技巨头 2026 年 AI 战略布局。核心预测：全球 AI 服务器出货量同比增长 20% 以上；特斯拉人形机器人进入量产元年；L2+ 自动驾驶渗透率突破 40%；AI 能源消耗成为最大结构性挑战，清洁能源供给能力已成地区吸引 AI 投资的核心竞争要素；AI 治理全球化提速，多国监管框架加快落地。

### [2026 年的 AI：一切走向现实之年](https://zhuanlan.zhihu.com/p/2007908435090505994)
**摘要**：深度分析 2026 年 AI 从实验走向大规模商用的关键转型。技术侧，多模态能力、Agent 工作流和 RAG 增强成为落地三大支柱；商业侧，企业级 AI 应用部署成本显著下降但 ROI 验证难度上升；治理侧，中美欧三地监管框架加速分化，数据主权与模型安全成为全球 AI 竞争的新战场。文章指出，2026 年之后 AI 的核心议题将从"能不能用"转向"如何用好、用安全"。

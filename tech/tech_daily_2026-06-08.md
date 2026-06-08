# 技术日报 2026-06-08

## Flutter

### [Flutter 鸿蒙 2026 路线发布，加速同步官方生态，进一步优化体验](https://zhuanlan.zhihu.com/p/2016571565735682780)
**摘要**：Flutter 鸿蒙社区正式发布 2026 年路线计划，将适配周期从过去平均 7 个月以上压缩至约 4 个月以内，并由 Flutter SIG 主导维护。计划适配至少 200 个高优先级三方库，覆盖网络、数据库、图片处理、音视频、地图等常用领域。目前社区最新适配版本为 3.35.7dev，与官方 3.41 仍有小版本差距，2026 年将按季度节奏跟进官方发布。

### [Flutter 3.41 发布，鸿蒙如何选择？](https://zhuanlan.zhihu.com/p/2005202488488378695)
**摘要**：Flutter 3.41 正式发布，本版本以问题修复和细节优化为主，新特性包括：支持按平台打包资源以减少应用体积、新增同步图像解码优化着色器性能、Android 端新增对 Kotlin DSL 的默认支持。文章同时探讨了鸿蒙开发者在 Flutter 跨平台方案选型上的策略，建议关注 Flutter-OH 的季度同步进度再决策。

### [注意，暂时不要升级 macOS，Flutter/RN 等构建 ipa 可能会报错](https://zhuanlan.zhihu.com/p/1892465141636891293)
**摘要**：作者提醒开发者暂缓升级最新版 macOS，否则 Flutter、React Native 等跨平台框架在执行 ipa 构建时可能出现编译报错，根因在于 Xcode 工具链与新系统的兼容性问题。文章列举了常见报错场景并给出了临时规避方法，建议等待框架和 Xcode 发布正式修复版本后再升级。

---

## Android

### [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://zhuanlan.zhihu.com/p/2009937286335308608)
**摘要**：Android 17 正式引入高级保护模式（APM），将在更严格的安全策略下限制侧载、限制 USB 数据传输、强制 Google Play Protect 扫描。同时，Google 计划于 2026 年 9 月起要求在部分地区运行的应用必须由已认证身份的开发者安装。小米、OPPO、vivo、荣耀等金标联盟成员已发布适配公告，要求开发者在 7 月 1 日前完成 Android 17 适配。

### [Google 发布 Android CLI：打造面向 Android 工程的 Agent 能力](https://zhuanlan.zhihu.com/p/2029480482035737404)
**摘要**：Google 在 Google I/O 2026 上正式发布 Android CLI 1.0，这是一套面向 AI Agent 的命令行工具链，可让 Claude Code、Codex、Gemini 等 Agent 直接调用 Android SDK 的能力，完成下载 SDK、在设备上运行应用等任务。与在 Android Studio 内运行 Agent 相比，LLM Token 使用量降低 70% 以上，任务完成速度提升 3 倍。同时推出 Android Skills（SKILL.md 文件），让 Agent 自动触发对应的开发指南。

### [Android Gradle Plugin 9.0 发布，为什么这会是个史诗级大坑版本](https://zhuanlan.zhihu.com/p/1997655149036995133)
**摘要**：AGP 9.0 包含三大破坏性变更：切换至新 DSL 接口（旧实现被完全隐藏，AGP 10.0 将移除退出选项）、内置 Kotlin（自动管理 KGP 版本依赖）、KMP 项目不再兼容 `com.android.application` 与 `com.android.library` 在同一模块共存。现有项目升级前需仔细评估兼容性，Android Studio Otter 3 Feature Drop 2025.2.3 才支持此版本，IntelliJ IDEA 预计 2026 年 Q1 跟进。

---

## iOS

### [iOS/iPadOS 26.5 正式版发布！新壁纸 + RCS 加密，大量 Bug 修复](https://zhuanlan.zhihu.com/p/2037595671025422489)
**摘要**：iOS/iPadOS 26.5 于 2026 年 5 月 12 日正式发布（内部版本号 23F77），作为 iOS 26 系列收官版本，核心更新包括：iPhone 与安卓用户互发 RCS 短信时支持端到端加密（默认开启，安全级别媲美 iMessage）；新增彩虹系列动态壁纸；地图新增基于位置和搜索记录的智能推荐功能；欧盟地区开放第三方设备 AirPods 式快速配对。本次更新共修复超过 50 个安全漏洞。

### [WWDC 2026 今日开幕：iOS 27、Siri 2.0 与 Gemini 深度集成首次亮相](https://www.zhihu.com/question/2040145697911956151/answer/2040419811679801472)
**摘要**：苹果 WWDC 2026 于 6 月 8 日正式开幕（持续至 6 月 12 日），主旨演讲于北京时间今晚发布。核心发布内容包括：iOS 27、iPadOS 27 及 macOS 27；全新 Siri 2.0 不再局限于简单指令，升级为具备文档摘要与复杂交互能力的对话 Agent，底层采用 Google 定制 Gemini 模型（约 1.2 万亿参数）驱动；Photos 应用新增三项端侧生成式 AI 工具。iOS 27 正式版预计于 9 月中旬推送。

### [iOS27 具体信息曝光：发布时间、支持机型、续航情况！](https://zhuanlan.zhihu.com/p/2009034918617949161)
**摘要**：根据此前曝光，iOS 27 将于 WWDC 2026 正式揭晓，预计面向 iPhone 15 及以上机型提供完整 AI 功能支持，旧机型仅获得基础系统更新。Siri 深度接入 Gemini 是本次最大变化，苹果每年约向 Google 支付 10 亿美元授权费。续航方面，得益于系统底层优化，iPhone 15 Pro 实测续航提升约 8%~12%。

---

## AI / 大模型

### [GPT-6 发布：5~6 万亿参数 MoE 架构，上下文窗口扩展至 200 万 Token](https://cloud.tencent.com/developer/article/2659606)
**摘要**：OpenAI 于 2026 年 4 月 14 日正式发布 GPT-6（内部代号"Spud"），采用混合专家架构（MoE），总参数量达 5~6 万亿，实际激活参数约占 10%，上下文窗口扩展至 200 万 Token。同期推出 GPT-5.5 Instant（已取代 5.3 Instant 成为 ChatGPT 默认模型）及 GPT-Image 2。GPT-5.4、GPT-5.5 和 Codex 已全面接入 Amazon Bedrock，企业可通过 AWS 合规工作流调用。

### [MiniMax 发布 M3 新一代模型，AI 大模型竞争转向长上下文与智能体能力](https://finance.sina.com.cn/stock/t/2026-06-01/doc-inhzwuhm8475761.shtml)
**摘要**：MiniMax 于 2026 年 5 月底发布新一代旗舰模型 M3，重点强化长上下文处理与智能体（Agent）编排能力，标志着大模型竞争赛点从单轮问答转向多步骤任务执行。与此同时，MiniMax 已与中信证券签署 IPO 辅导协议，正式启动 A 股科创板上市进程；智谱也宣布计划赴港上市。

### [DeepSeek 与 Qwen 密集更新：V4-Pro、V4-Flash 系列齐发](https://zhuanlan.zhihu.com/p/670574382)
**摘要**：国内头部大模型阵营在 5~6 月密集迭代：DeepSeek 新增通用模型 V4-Pro、V4-Flash 及对应 Thinking 推理版；Qwen 发布 Qwen3.6-27B 并更新 Qwen3.6-Flash；Kimi 更新 K2.6 及 K2.6 Thinking。NVIDIA 同期推出 Cosmos 3 世界基础模型（Mixture-of-Transformers 双塔架构），统一支持视觉推理、多模态生成与机器人动作预测。MCP（模型上下文协议）加速普及，推动跨厂商 AI Agent 协作。

---

## 行业动态

### [Google I/O 2026 开发者主旨演讲要点回顾](https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/)
**摘要**：Google I/O 2026 于 5 月 19 日举行，核心发布包括：Android CLI 1.0 正式可用、Android 17 预览版、Android XR 平台进展、Gemini Intelligence 跨平台集成。Google 强调 Agent 开发是 2026 年的核心战略方向，旗下工具链已全面向 AI Agent 开放，并与 Claude Code、Codex 等第三方 Agent 打通兼容。

### [马斯克解散 xAI 大模型业务，转向"世界最大 AI 芯片工厂"建设](https://www.shobserver.com/staticsg/res/html/web/newsDetail.html?id=1108411&sid=11)
**摘要**：马斯克宣布解散 xAI 大模型研究部门，将资源集中投入大规模 AI 算力基础设施建设，计划打造"世界最大 AI 芯片工厂"。此举被业界解读为从模型研究转向算力层面的战略重心转移，也引发外界对 Grok 系列模型后续维护的关注。这与当前各大科技巨头加速 AI 数据中心扩建的整体趋势一致。

### [2026 年科技行业三大关键趋势：AI 原生硬件、Agent 标准化、绿色算力](https://www.thepaper.cn/newsDetail_forward_32889979)
**摘要**：澎湃新闻整理了 2026 年 AI 行业三个关键趋势：一是 AI 原生终端硬件成为主战场，AI 手机、AI PC 与 XR 设备深度融合多模态大模型；二是 AI Agent 标准化加速，MCP 协议推动不同厂商 AI 系统互联互通；三是绿色算力成为政策与市场双驱动赛道，全球 AI 服务器出货量预计同比增长超 20%，首个绿色算力全栈 AI 平台已于近期上线。

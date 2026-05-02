# 技术日报 2026-05-02

## Flutter

### [Flutter 2026 Roadmap 发布，未来计划是什么？](https://zhuanlan.zhihu.com/p/2009657387510952563)
**摘要**：Flutter 官方发布 2026 年路线图，核心目标包括：完成 Android 平台 Impeller 渲染引擎的全量迁移并移除 Skia 后端（Android 10+），将 WebAssembly 设为 Flutter Web 的默认构建目标以实现近原生性能，推进桌面平台（macOS/Windows/Linux）的 Impeller 适配，并持续优化多窗口和无障碍支持。Dart 语言层面计划引入 Primary Constructor 和 Augmentations，简化类声明与代码生成。

### [新年 Flutter 3.41 就放大招，历经 3 年，多窗口支持终合并](https://zhuanlan.zhihu.com/p/2005389425048307284)
**摘要**：Flutter 3.41 于 2026 年初正式发布，最受瞩目的是经过 3 年开发的桌面多窗口支持终于合并进入主线。此版本修复了多窗口场景下的焦点管理、键盘事件流转和无障碍支持等问题，并完善了窗口生命周期管理，为桌面应用开发打开了重要能力缺口。该功能由 Canonical 背后的公司持续贡献推动。

### [Flutter 发布官方 Skills，Flutter 在 AI 领域再添一助力](https://zhuanlan.zhihu.com/p/2012886441642975382)
**摘要**：Flutter 团队发布官方 flutter/skills 支持，填补了 AI 编程中缺乏 Flutter 官方技能集的空白。Skills 为 AI Agent 提供了决策逻辑、详细指令和严格约束，使 AI 助手在处理 Flutter 项目时能给出更准确、更符合官方最佳实践的开发建议，是 Flutter 拥抱 AI 辅助开发的重要一步。

### [Flutter 鸿蒙 2026 路线发布，加速同步官方生态，进一步优化体验](https://zhuanlan.zhihu.com/p/2016571565735682780)
**摘要**：Flutter 鸿蒙（Flutter-OH）发布 2026 年发展路线，重点方向包括加速追平 Flutter 官方生态进度、进一步优化在鸿蒙平台上的渲染性能和用户体验，以及增强与华为 SDK 的兼容性。这标志着 Flutter 跨平台能力向国产操作系统的持续延伸。

### [Android Vulkan 官宣转正并统一渲染堆栈，这对 Flutter 又有什么影响？](https://zhuanlan.zhihu.com/p/30915375962)
**摘要**：Google 官宣 Android Vulkan 正式成为 Android 统一渲染堆栈，此举对 Flutter 的 Impeller 引擎影响深远。Impeller 在 Android 上主要依赖 Vulkan 后端实现低延迟着色器编译，Vulkan 转正意味着 Flutter 可以更坚定地将 Impeller Vulkan 路径作为主要渲染方式，同时也为移除旧 Skia/OpenGL 路径铺平了道路，有助于提升 Flutter 应用在 Android 上的整体渲染稳定性。

## Android

### [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://zhuanlan.zhihu.com/p/2009937286335308608)
**摘要**：文章梳理了 Android 17 的主要适配要求，并深入解读 Google 于 2026 年推行的"Android 高级侧载流程"政策。该政策要求用户完成六步验证并强制等待 24 小时才能安装非 Play Store 应用，大幅提高侧载门槛。开发者需关注 targetSdkVersion 升级要求及新增的权限与行为变化，提前完成适配工作。

### [Google 发布 Android CLI：打造面向 Android 工程的 Agent 能力](https://zhuanlan.zhihu.com/p/2029480482035737404)
**摘要**：Google 于 2026 年 4 月发布 Android Agent 开发工具集，包括 Android CLI、Android Skills 和 Android Knowledge Base 三大组件。Android CLI 通过减少 LLM 70% 的 token 消耗使 Android 开发提速约 3 倍；Android Skills 覆盖 Navigation 3 配置、Edge-to-Edge UI 实现和 AGP 9 迁移等场景；Knowledge Base 将最新 Android 官方文档实时接入 Agent，解决模型知识截止问题。

### [Android Gradle Plugin 9.0 发布，为什么这会是个史诗级大坑版本](https://zhuanlan.zhihu.com/p/1997655149036995133)
**摘要**：Android Gradle Plugin 9.0 随 Android Studio Otter 3 Feature Drop（2025.2.3）发布，引入大量破坏性 API 变更，包括废弃旧版 Variant API、调整资源合并策略、修改 Lint 任务执行时机等。文章详细分析了升级过程中常见的兼容性陷阱，并提供逐步迁移建议，指出 IntelliJ IDEA 对 AGP 9.0 的完整支持将推迟到 2026 年 Q1。

### [Google 开始正式强制 Android 适配 16K Page Size，你准备好了吗？](https://zhuanlan.zhihu.com/p/1904196757702834168)
**摘要**：Google 宣布自 2025 年 11 月 1 日起，所有提交至 Google Play 且 targetSdk 为 Android 15+ 的新应用必须支持 16K 页面大小。16K Page Size 要求 Native 库按 16KB 对齐编译，不兼容的 so 文件将导致应用在部分新设备上崩溃。文章提供了检测工具使用方法和 CMake/ndk-build 编译参数配置指引。

## iOS

### [iOS/iPadOS 26.5 开发者预览版 Beta 2 发布，核心更新与升级速览](https://zhuanlan.zhihu.com/p/2027450346990052584)
**摘要**：苹果于北京时间 4 月 14 日推送 iOS/iPadOS 26.5 开发者预览版 Beta 2（内部版本号 23F5054d）。此版本主要变化包括：Apple Maps 新增"Suggested Places"推荐位广告功能（附弹窗告知）、应用内购买新增"按月计费 12 个月承诺"订阅选项、iPhone 与 Android 间的 RCS 端到端加密再次开启，整体以 Bug 修复和安全优化为主，属于常规小版本迭代。

### [iOS/iPadOS 26.3 RC 正式推送，iPhone 转安卓换机工具上线](https://zhuanlan.zhihu.com/p/2002807218161075657)
**摘要**：苹果于 2026 年 2 月推送 iOS/iPadOS 26.3 RC 版（版本号 23D125），最大亮点是内置 iPhone 转 Android 数据迁移工具。用户无需第三方软件即可将照片、视频、短信、应用、密码和联系人无线迁移至 Android 设备，并完整保留照片 EXIF 信息与动态效果。此外还新增通知转发和天气壁纸功能。

### [iOS/iPadOS 26.4.2 正式版发布，解决通知残留问题](https://zhuanlan.zhihu.com/p/2030706411789886155)
**摘要**：苹果推送 iOS/iPadOS 26.4.2 正式版，主要针对此前版本中出现的通知横幅残留（通知消失后仍在屏幕显示残影）问题进行了修复，同时包含若干安全补丁。建议使用 26.4.x 版本的用户尽快升级以获得更稳定的通知体验。

## AI / 大模型

### [2026 年 4 月 AI 圈 5 大事件盘点：GPT-6 来袭、国产大模型爆发，普通人如何抓住红利？](https://zhuanlan.zhihu.com/p/2025390002230555538)
**摘要**：2026 年 4 月 AI 领域高度活跃：OpenAI 于 4 月 23 日发布 GPT-6，采用混合专家架构（5-6 万亿参数，激活约 10%），上下文窗口扩展至 200 万 Token，在主流基准上较 GPT-5.4 提升约 40%，战略重心从对话交互转向自主智能体；与此同时，DeepSeek-V4 支持百万 Token 上下文并开源，Kimi K2.5 多模态能力提升 40%，MiniMax M2.5 API 价格下调 30%，国产模型集体发力。

### [2026 年 4 月 AI 大事件：GPT-6 来袭、国产崛起、中美博弈](https://zhuanlan.zhihu.com/p/2026928444483585175)
**摘要**：文章从宏观视角梳理 2026 年 4 月 AI 领域的中美竞争态势。美国方面 GPT-6 发布标志着 AI 能力新里程碑；中国方面 DeepSeek、Kimi、MiniMax 等头部厂商密集发布新版本，在部分垂直能力上实现反超。文章还分析了算力管制、开源策略对中美 AI 格局的长期影响，以及普通开发者如何把握 API 价格下行带来的应用层创业机遇。

### [AI 行业动态 20260215：2026 年新发布的代表性 AI 大模型汇总](https://zhuanlan.zhihu.com/p/2006304089840058657)
**摘要**：文章系统梳理了 2026 年初至 2 月间新发布的代表性大模型：MiniMax M2.5 支持 100+ TPS 输出、输入成本降至约 $0.3/M tokens；ByteDance Doubao-Seed-2.0 专注上下文自主学习；Google Gemini 3 Deep Think 引入"Aletheia"推理逻辑，可求解奥林匹克级数学题；Google Gemma 4 开源系列（2B-31B）推理成本较同规模闭源模型降低 70%。

### [2026 年最佳开源大模型！](https://zhuanlan.zhihu.com/p/1999590757271618835)
**摘要**：文章横评 2026 年最佳开源大模型，涵盖通用推理、代码生成、多模态等维度。Google Gemma 4 以高性价比和 Apache 2.0 协议脱颖而出；DeepSeek 系列在代码和数学能力上表现突出；国内厂商多个开源版本在中文理解和工具调用能力上更具优势。文章为开发者提供了实际部署建议和场景选型参考。

## 行业动态

### [2026 年值得关注的 10 大科技趋势](https://zhuanlan.zhihu.com/p/2010649421336056375)
**摘要**：文章梳理 2026 年 10 大科技趋势，包括：Agentic AI 规模商用（40% 企业应用将嵌入任务型 Agent）、量子计算纳入"十五五"重点方向并设 300 亿专项资金、商业航天市场预计突破 3.5 万亿元、脑机接口进入政府工作报告并有产品进入量产、AI 驱动生物标志物检测从"发现"升级为"预测"等，覆盖面广且有具体数据支撑。

### [2026 科技四大风口：生命、家园、深空、智能，企业如何借势？](https://zhuanlan.zhihu.com/p/1995544744936354162)
**摘要**：文章将 2026 年科技机遇归纳为四大风口：生命（个性化基因编辑疗法开启临床试验）、家园（可再生能源与储能技术加速商业落地）、深空（中国天舟十号/神舟二十二号、美国波音星际客机等多国航天任务密集实施）、智能（AI Agent 全面渗透企业应用，推动 AI 从"会生成"向"会规划行动"演进）。并从企业战略角度给出借势建议。

### [2026 年，科技行业将迎来哪些根本性的巨变？](https://www.zhihu.com/question/2005286734464825320)
**摘要**：知乎高热问答，多位答主从不同角度分析 2026 年科技行业的结构性变化：AI 基础设施市场进入整合期，算力泡沫开始挤出；开源与闭源大模型的竞争格局重塑商业模式；具身智能（机器人）从实验室走向规模制造；数据主权和 AI 监管法规在全球范围加速落地，成为企业合规的新挑战。

### [2026 年，这 8 大科技方向千万别错过！](https://zhuanlan.zhihu.com/p/2018005869384712497)
**摘要**：文章列举 2026 年最具潜力的 8 大科技投资与创业方向，包括：AI Agent 开发框架、多模态大模型应用、具身智能/机器人、卫星互联网终端、钠离子电池商业化、合成生物学工具链、空间计算（AR/VR）以及量子安全通信。每个方向均结合产业现状、代表企业和市场规模进行简要分析。

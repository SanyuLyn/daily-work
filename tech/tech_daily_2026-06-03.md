# 技术日报 2026-06-03

## Flutter

### [Flutter 3.44 有哪些变化？（官方 blog 完整翻译）](https://zhuanlan.zhihu.com/p/2041190868812567494)
**摘要**：Flutter 3.44 带来三大重磅变化：①SwiftPM 正式成为 iOS/macOS 默认依赖管理器，取代 CocoaPods——运行 `flutter upgrade` 后 CLI 自动迁移工程，去掉了 Ruby 依赖和 `pod install` 步骤，构建时间提升 10-20%；CocoaPods trunk 将于 2026-12-02 永久进入只读模式。②Material 和 Cupertino 库从核心 SDK 剥离，迁移为独立包 `material_ui` 与 `cupertino_ui`。③Android Hybrid Composition++ 进一步优化，Impeller Vulkan 支持改善。如果 pubspec 中的插件尚未迁移 SwiftPM，Flutter 会打印警告并对该依赖自动回退到 CocoaPods。

### [Flutter 3.41.6 版本很重要，你大概率需要更新一下](https://zhuanlan.zhihu.com/p/2021619335085454240)
**摘要**：Flutter 3.41.6 修复了一个长期存在的 Android ANR 神秘 bug——根因是 Vulkan Swapchain 在 `vkAcquireNextImageKHR` 返回 `SURFACE_LOST` 后 Fence 永远不被 GPU 置位，导致 UI 线程无限等待。2026 年 3 月 Android 16 安全更新会在锁屏时立即回收 Surface，使该 bug 极易复现。修复思路：只有 Present 成功后才标记 Fence 为 pending，acquire 失败则跳过等待。该 hotfix 仅合入 3.41.6，必须升级才能解决。

### [2026 年鸿蒙跨平台开发：Flutter、React Native 及其他框架前瞻](https://zhuanlan.zhihu.com/p/2000910086613255920)
**摘要**：2026 年鸿蒙跨平台开发生态已初步成形，形成两条主路径：一是以 ArkTS/ArkUI 为核心的纯血鸿蒙原生开发，性能最优；二是以 Flutter-OH（Flutter OpenHarmony 适配层）为代表的生态融合路径，实现"一次开发，多端运行"。Flutter 凭借自绘引擎优势成为追求高流畅 UI 的首选跨平台方案，当前社区重点关注其渲染后端与 ArkUI 引擎的深度集成，以及对鸿蒙"超级终端"跨设备流转特性的底层支持进展。

---

## Android

### [Android 17 新适配要求，各大权限进一步收紧，适配难度提升](https://zhuanlan.zhihu.com/p/2020865242960277920)
**摘要**：Android 17 对多项权限作出重大收紧：联系人访问改由系统 `ACTION_PICK_CONTACTS` 机制替代 `READ_CONTACTS`；位置权限新增一次性授权和系统级位置按钮；SMS/OTP 消息在收到后仅 3 小时内可读；访问本地网络需声明新权限 `ACCESS_LOCAL_NETWORK`。小米、OPPO、vivo、荣耀已联合发布公告，要求开发者于 2026 年 7 月 1 日前完成适配，逾期将面临搜索标签提示、机型屏蔽乃至下架处理。整体适配难度较 Android 16 显著提升。

### [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://zhuanlan.zhihu.com/p/2009937286335308608)
**摘要**：Google 于 2026 年 3 月正式启动"Android 高级侧载流程"——安装未经核验应用需完成六步验证并强制等待 24 小时；2026 年 9 月起，部分地区 Android 设备上的应用须由经过身份认证的开发者发布。Google Android 生态主管明确表示侧载功能不会被取消，但会持续加强开发者身份核验，以平衡开放性与安全性。Android 17 还引入高级保护模式，限制侧载、USB 数据传输，并强制要求 Google Play Protect 扫描高风险权限行为。

### [Google 发布 Android CLI：打造面向 Android 工程的 Agent 能力](https://zhuanlan.zhihu.com/p/2029480482035737404)
**摘要**：Google 于 2026 年 4 月（Google I/O 2026）发布 Android 开发三件套：Android CLI、Android Skills 和 Android Knowledge Base。Android CLI 提供 SDK 组件管理、工程模板创建、虚拟设备管理、应用部署及工具更新等标准化命令；Android Skills 仓库收录了面向各类 AI Agent（Claude Code、Codex 等）的 SOP 操作规范。官方数据：集成后 token 使用量降低超 70%，完成同类 Agent 任务速度提升约 3 倍，当前处于 Preview 阶段。

---

## iOS

### [iOS/iPadOS 26.5 正式版发布！新壁纸 + RCS 加密，大量 Bug 修复](https://zhuanlan.zhihu.com/p/2037595671025422489)
**摘要**：苹果于北京时间 2026 年 5 月 12 日正式推送 iOS/iPadOS 26.5。核心亮点：①RCS 端到端加密正式上线，iPhone 与 Android 互发 RCS 消息时安全级别媲美 iMessage，加密默认开启，消息显示专属小锁标识，依赖运营商支持（国内逐步适配）；②新增 2026 年度彩虹系列动态壁纸，适配 iPhone、iPad 及 Apple Watch 锁屏；③地图 POI 推荐升级，基于用户位置与搜索记录自动推荐附近商业场所；④修复 50+ 安全漏洞。

### [一文看懂 iOS 26.5 Beta 1 更新内容：地图广告就绪，跨平台迁移更灵活](https://zhuanlan.zhihu.com/p/2022379136979669588)
**摘要**：iOS 26.5 Beta 1 预告了正式版的主要功能方向：地图广告系统已就绪，商家可投放基于位置的精准广告；新增"转移至 Android"功能，用户可将数据（联系人、照片、通话记录等）迁移至 Android 设备，跨平台生态互通度提升；同时 Beta 阶段还测试了 RCS 端到端加密，为 5 月正式版奠定基础。此次更新整体方向是强化安全性、提升生态开放性，并为欧盟合规政策准备更多互操作性接口。

### [【设计前沿】iOS 26 设计：用户体验设计专业角度怎么看？](https://zhuanlan.zhihu.com/p/49398865314)
**摘要**：苹果在 WWDC 2025 发布 Liquid Glass（液态玻璃）设计语言，这是继 2013 年 iOS 7 扁平化以来 12 年最大幅度的设计更新，统一贯穿 iOS 26、iPadOS 26、macOS Tahoe、watchOS 26、visionOS 26 全平台。液态玻璃以动态半透明玻璃质感界面为核心，能折射和反射背景内容，随场景自适应变化，强调深度与沉浸感。UX 设计师认为此次更新视觉统一性显著提升，但初期部分控件在强背景下可读性下降，"好看但不好用"的反馈值得关注，开发者需重新审视自定义 UI 组件的视觉层级。

---

## AI / 大模型

### [国内外知名大模型及应用——模型/应用维度（2026/06/01）](https://zhuanlan.zhihu.com/p/670574382)
**摘要**：截至 2026 年 6 月初，国内外大模型差距持续收窄，但国际梯队（Google/OpenAI/Anthropic）在通用模型方面仍保持约一个身位的领先优势。最新动态：Step 发布推理模型 Step-3.7-Flash；MiniMax 上线即将开源的 Agent 模型 MiniMax M3。国内头部模型在 Agent 能力、世界知识和长上下文处理方面快速跟进，部分垂直任务（数学推理、代码生成）已接近国际顶尖水平，整体竞争进入"密集落地"阶段。

### [DeepSeek V4 发布——开源再次比肩世界顶级闭源模型](https://www.zhihu.com/question/2030966008312231624)
**摘要**：2026 年 4 月 24 日，DeepSeek 正式发布 V4 系列：V4-Pro 总参数 1.6 万亿（激活 49B），V4-Flash 总参数 2840 亿（激活 13B），两款均原生支持 100 万 Token 上下文。最大亮点是 V4 全面转向华为昇腾芯片，成为首款完全基于国产算力生态训练和部署的顶级大模型。V4-Pro 在数学、STEM、竞赛型代码等推理任务中超越所有已公开评测的开源模型，达到比肩世界顶级闭源模型的水平，技术报告同步开源。

### [OpenAI GPT-6 发布——AI 从"聊天"迈向"干活"时代](https://cloud.tencent.com/developer/article/2659606)
**摘要**：OpenAI 于 2026 年 4 月 14 日发布代号"Spud"的 GPT-6，采用混合专家（MoE）架构，参数量达 5-6 万亿，支持 200 万 Token 超大上下文（可处理完整百万行代码仓库或整份年报）。跨模态推理准确率提升 65%，数学推理准确率 92.5%，代码生成通过率 96.8%，在 44 类职业测试中 83% 任务接近人类专家水平。以记忆与个性化为核心亮点，标志 AI 从工具型交互正式迈向智能体自主执行新阶段。

### [2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！](https://zhuanlan.zhihu.com/p/2038200846148704182)
**摘要**：文章对 GPT-6、Gemini 3.5 Pro、Claude Opus 4、DeepSeek V4-Pro、Qwen3.6-Plus、Doubao-Seed-2.0 六款顶流大模型进行 AI 编程实测对比，涵盖代码生成、Bug 修复、架构设计、多文件重构等维度。整体结论：相比 2025 年同类工具，2026 年主流模型的编程效率平均提升超 2 倍；国内模型在中文注释和国内框架理解上具有明显优势；多文件复杂重构任务中旗舰模型依然是首选；AI 编程已从"辅助提示"阶段进化为"自主完成"阶段。

---

## 行业动态

### [2026 年 Google I/O 大会有哪些值得关注的信息？](https://www.zhihu.com/question/2040145697911956151)
**摘要**：2026 年 Google I/O 以"Agent 时代"为主题，桑达尔·皮查伊宣布 AI 从内容生成助手升级为可自主规划、执行、验证的 Agent。核心发布：Gemini 3.5 Flash（前沿智能 + 极速推理）与即将推出的 Gemini 3.5 Pro；全模态模型 Gemini Omni（文本/图像/音频/视频统一编码）；搜索进入 Agent 时代，支持用户创建和管理多个 AI Agent 全天候监控信息；音频眼镜秋季上市（内置扬声器/麦克风/摄像头，支持 Gemini 语音交互和实时翻译）；SynthID 水印技术已被全球使用 5000 万次并持续扩展。

### [2026 年各大科技巨头对 AI 的趋势预测](https://zhuanlan.zhihu.com/p/2011108769992577031)
**摘要**：Anthropic、Google、Microsoft 等科技巨头对 2026 年 AI 走向的核心共识包括：①物理 AI 爆发——AI 与工业机器人、人形机器人、低空载具深度融合，推动智能制造和智慧物流规模化商用；②AI 硬件普及——AI 手机、AI PC、XR 设备与多模态大模型深度融合，NPU 算力和传感器融合成为标配；③低空经济加速——eVTOL、低空物流、空中观光在政策放开后迎来商业化订单快速释放，市场规模预计突破万亿；④AI 安全成重要议题，SynthID 水印、内容溯源技术进入主流平台。

### [2026 年科技行业全面转向商业落地，AI 主导格局确立](https://caifuhao.eastmoney.com/news/20260505074828445890980)
**摘要**：2026 年科技行业呈现"从概念验证到商业落地"的核心转变：AI 已从单点技术突破转为系统性渗透各行业，医疗 AI、教育 AI、工业 AI 的商业化订单快速增长；人形机器人进入从"1 到 10"的规模化试用阶段，制造、仓储、家庭服务领域出现标志性商业产品；IDC 预测具身智能机器人 2026 年将在多模态感知融合、系统级安全冗余两大维度取得关键突破；整体行业格局呈现"AI 全面主导、硬科技突围"特征，国内外科技公司均在加快 AI 商业化节奏。

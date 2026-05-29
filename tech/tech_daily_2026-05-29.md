# 技术日报 2026-05-29

## Flutter

### [Flutter 鸿蒙 2026 路线发布，加速同步官方生态，进一步优化体验](https://zhuanlan.zhihu.com/p/2016571565735682780)
**摘要**：Flutter-OH 社区更新 2026 路线图，核心目标是与官方 Flutter 版本保持同步，不再大幅落后。以往适配周期超过 7 个月，2026 年计划压缩至 4 个月以内。从 2026 年起，Flutter-OH 将主要由 Flutter SIG 维护，版本规划通过 SIG 讨论推进。社区计划全年适配至少 200 个高优先级第三方库，覆盖网络、数据库、图像处理、音视频、地图等常用领域，大幅提升鸿蒙平台的 Flutter 生态完整性。

### [Flutter 2026 Roadmap 发布，未来计划是什么？](https://zhuanlan.zhihu.com/p/2009657387510952563)
**摘要**：Flutter 官方 2026 路线图重点聚焦「完成收尾」：在 Android 平台全面完成 Impeller 渲染引擎迁移，彻底移除 Android 10 及以上设备上的老旧 Skia 后端；确保对 Android 17 和新版 iOS 的"零日"支持；推动 WebAssembly（Wasm）成为 Flutter Web 的默认渲染模式；桌面端多窗口支持进入成熟阶段，同时计划引入 Material 3 Expressive 和 Liquid Glass 风格作为可选设计包。

### [新年Flutter3.41就放大招，历经3年，多窗口支持终合并。感谢Ubuntu背后的公司Canonical！](https://zhuanlan.zhihu.com/p/2005389425048307284)
**摘要**：Flutter 3.41 正式合并了历经三年开发的多窗口支持功能，主要由 Canonical（Ubuntu 母公司）工程师主导贡献。新架构从"多引擎模式"升级为"单 Isolate，多视图（Multi-view）"架构，内存占用减少约 60%。支持 Window、Dialog、Satellites、Popup 等多种窗口类型，具备自定义定位和约束调整能力，对桌面端（Linux/Windows/macOS）开发者来说是重大突破。

### [Android Vulkan 官宣转正并统一渲染堆栈，这对 Flutter 又有什么影响？](https://zhuanlan.zhihu.com/p/30915375962)
**摘要**：谷歌宣布 Vulkan 成为 Android 唯一官方 GPU 硬件抽象层（HAL），要求所有应用基于 Vulkan 实现。对 Flutter 来说，此举为 Impeller 引擎的完全迁移扫清了障碍——Vulkan 与 OpenGL 并存显著增加了 Impeller 的稳定性维护成本，统一后可大幅降低设备兼容性问题。Flutter 3.38 已在 API 29+ 设备默认启用 Vulkan 后端的 Impeller，老旧设备自动回退 OpenGL，2026 年路线图计划彻底移除 Skia 后端。

---

## Android

### [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://zhuanlan.zhihu.com/p/2009937286335308608)
**摘要**：小米、OPPO、vivo、荣耀等金标联盟成员已发布 Android 17 适配公告，呼吁开发者在 7 月 1 日前完成适配。主要变化：大屏设备（sw > 600 dp）上不得通过代码锁定屏幕方向或限制宽高比，系统将强制允许应用随窗口自由缩放。谷歌同步推出"开发者验证"机制，计划 2026 年 9 月在部分地区要求应用来自已验证开发者——完全禁止侧载为误读，非认证来源 APK 仍可安装，但需来自"已验证开发者"。

### [Google 发布 Android CLI：打造面向 Android 工程的 Agent 能力](https://zhuanlan.zhihu.com/p/2029480482035737404)
**摘要**：谷歌 2026 年 4 月发布 Android Agent 开发三件套：Android CLI、Android Skills 和 Android Knowledge Base，核心目标是让 AI Agent（无论是 Android Studio、Gemini CLI 还是 Claude Code 等第三方 agent）以统一方式高质量完成 Android 工程任务。Android CLI 提供 SDK 管理、工程创建、模拟器控制、部署运行等标准化操作，官方数据显示 token 用量降低超 70%，完成速度提升约 3 倍。目前处于 preview 阶段。

### [Android Gradle Plugin 9.0 发布，为什么这会是个史诗级大坑版本](https://zhuanlan.zhihu.com/p/1997655149036995133)
**摘要**：AGP 9.0 一次性偿还多年技术债：完全切换至新 DSL 接口并移除旧版 `BaseExtension` 等强转类型，旧版 Variant API（`applicationVariants` 等）被废除，强制迁移到 `androidComponents` API；Kotlin 编译深度整合进 AGP，KMP 插件不能再与 `com.android.application/library` 共存于同一模块。对大量使用自定义 Gradle 插件或 KMP 的项目，升级成本极高，需配套 Android Studio Otter 3 Feature Drop（2025.2.3）及以上版本。

### [Google 开始正式强制 Android 适配 16K Page Size，你准备好了吗？](https://zhuanlan.zhihu.com/p/1904196757702834168)
**摘要**：谷歌正式要求所有 Android 应用适配 16K 内存页大小（从 4KB 提升至 16KB）。受影响的主要是包含 Native 代码（C/C++/Rust）的应用，纯 Java/Kotlin 应用影响较小。未适配的应用在搭载 16K 页大小内核的设备上将无法运行。谷歌建议开发者尽快重新编译 Native 库并在官方模拟器上验证兼容性，该内核已在 Pixel 9 系列等旗舰机型上部署。

---

## iOS

### [iOS/iPadOS 26.5 正式版发布！新壁纸 + RCS 加密，大量 Bug 修复](https://zhuanlan.zhihu.com/p/2037595671025422489)
**摘要**：苹果于 2026 年 5 月 12 日正式推送 iOS/iPadOS 26.5（版本号 23F77），这是 WWDC 2026（6 月 9 日开幕）前的最后一个重要版本。核心更新：实现 iPhone 与 Android 设备之间 RCS 消息端到端加密，安全级别与 iMessage 相当；新增"Pride Luminance"动态彩虹壁纸，提供 11 个预设配色；Apple Maps 新增"建议地点"智能推荐功能；同时修复超过 50 个安全漏洞，更新包约 4.13GB。

### [苹果推送 iOS 26.5 正式版，部分核心变化汇总](https://zhuanlan.zhihu.com/p/2037857321750090387)
**摘要**：iOS 26.5 核心变化汇总：地图广告引入场景化商业植入；欧盟地区为第三方设备开放 AirPods 式快速配对；本次更新未纳入新 Siri 相关能力；新 RCS 加密功能跨平台互通意义重大，是苹果生态与 Android 消息生态互操作的重要一步。开发者需注意部分隐私权限管理变化和 CoreLocation API 的小幅调整，建议在正式发布前完成兼容性验证。

### [苹果再次推迟新系统的发布时间！](https://zhuanlan.zhihu.com/p/2042651008002700680)
**摘要**：由于美国"阵亡将士纪念日"假期影响，苹果推迟了 iOS 26.5.1 正式版与 iOS 26.6 Beta 的发布计划，整体延迟约一周。原计划本周二推送 iOS 26.5.1 修复版，同时启动 iOS 26.6 Beta 测试，双重假期叠加导致进度顺延。业内分析认为，iOS 26.6 可能在 WWDC 前小幅推出修复版本，战略重心已转向 iOS 27 等下一代操作系统的正式发布准备。

### [iOS 26.5 RC版推送：彩虹壁纸成最大亮点，正式版定档5月12日](https://zhuanlan.zhihu.com/p/2035386764278380023)
**摘要**：苹果推送 iOS 26.5 RC 版，确认正式版于 5 月 12 日发布。RC 阶段新增"2026 年度彩虹壁纸"，支持 75 种基础颜色自定义 1-12 色渐变，兼容 Apple Watch 表盘；RCS 消息端到端加密测试进入 RC 阶段，稳定性良好；此外包含大量 Xcode 兼容性修复和系统底层优化，为 WWDC 前 iOS 平台稳定性奠定基础。

---

## AI / 大模型

### [2026 年 AI 编程实测：6 款顶流大模型对比，效率直接翻倍！](https://zhuanlan.zhihu.com/p/2038200846148704182)
**摘要**：对 Claude Opus 4.6、GPT-5.2 Pro、Gemini 3 Pro 等 6 款顶级大模型进行编程实测，从综合能力、推理、编程、视觉多模态、长上下文、速度、价格 8 个维度全面评估。结论：Claude Opus 4.6 与 o3 分别在 Agent 编程和数学推理上领先但成本高昂；Claude Sonnet 4.6、Gemini 2.5 Pro、GPT-4.1 是性价比最高的旗舰选择；DeepSeek-V3.2 和 Gemini 2.5 Flash 提供最低成本，适合高并发生产场景，合理选型可将开发效率提升超 100%。

### [国内外知名大模型及应用——模型/应用维度（2026/05/22）](https://zhuanlan.zhihu.com/p/670574382)
**摘要**：截至 2026 年 5 月 22 日的全球主流大模型横评：国内模型在中文场景全面反超，DeepSeek-V4-Pro（1.6T 参数，A49B 激活，1M context）与 Qwen3.5-397B 进入开源模型 SOTA 梯队；国际阵营以 GPT-5.2、Claude Opus 4.6、Gemini 3 Pro 为第一梯队。AI 的"自主完成任务时长"每 7 个月翻倍，预计 2026 年底可独立完成 8 小时工作流，Agent 化成为各厂商核心竞争焦点。

### [2026 年 5 月最新｜Gemini 免登录直达，国内一站式玩转全主流 AI 大模型](https://zhuanlan.zhihu.com/p/2037202361999963746)
**摘要**：Google 于 2026 年 5 月更新 Gemini-3.5-Flash 并新增视频生成模型 Gemini Omni。对国内开发者而言，直接访问 Gemini 官网仍需翻墙，但已出现国内 AI 聚合平台，整合 Gemini、GPT、Claude 等主流模型为一体，注册后无需 VPN、海外手机号或谷歌账号，部分方案支持免登录直连。香港地区已可直接使用 Gemini 官方服务，为后续大陆地区开放提供参考。

### [2026 年开源大模型 TOP10 完整榜单](https://zhuanlan.zhihu.com/p/2009705203163752429)
**摘要**：2026 年开源模型格局：DeepSeek-V4-Pro 以极致性价比（训练成本 557 万美元）和 MIT 开源协议领跑，API 定价比美国竞品低 90-95%；阿里 Qwen3.5-397B-A17B 提供强大原生多模态能力；智谱 GLM-5（744B 参数，激活 40B）紧随其后；Meta Llama 4 发布但性能低于预期，开源王者地位被国产模型取代。"百模大战"持续，各厂争相在季报期前发布新版，开源生态进入全球竞争的核心圈。

---

## 行业动态

### [2026芯片行情：产能紧、库存低、需求旺、价格走强](https://zhuanlan.zhihu.com/p/2038556501015536438)
**摘要**：2026 年芯片市场进入"量价齐升"黄金周期：台积电产能利用率达 98-100%，客户加价 50-100% 抢购加急产能；全球半导体大厂 Q1 库存周转天数降至 121 天，创三年新低，平均毛利率升至 74%。存储芯片领涨：三星 NAND Flash 涨幅超 100%，DRAM 涨 60-70%，SK 海力士 LPDDR 部分产品涨幅逼近 100%，HBM 高带宽内存供不应求，直接受益于 AI 算力军备竞赛。

### [雷军为何建议有计划在一年内换手机的朋友现在立刻换手机？](https://www.zhihu.com/question/2041775534485529119)
**摘要**：雷军在 2026 年 5 月 21 日小米新品发布会上强烈建议有换机计划的用户立即购买，理由是内存芯片价格将持续上涨两年：Q2 DRAM 合约价预计环比上涨 58-63%，NAND 闪存涨 70-75%。Counterpoint 数据显示 2026 年 Q1 全球智能手机均价同比上涨 12% 至 399 美元，创历史同期新高。知乎讨论中，多数用户认为这既是基于真实供应链判断的诚意提醒，也客观上起到了促进销售的营销效果。

### [2026半导体冲刺万亿美元，繁荣背后的风险](https://zhuanlan.zhihu.com/p/2022372959969452882)
**摘要**：2026 年全球半导体市场预计突破万亿美元，2 月销售额达 8878 亿美元，同比增长 61.8%，AI 算力、汽车电子和工业控制是三大驱动力。存储芯片收入预计约 2000 亿美元，占总量 25%；DRAM 资本支出增长 14%，NAND 增长 5%。但繁荣背后存在隐忧：AI 投资回报尚未充分验证，地缘政治风险持续，若终端需求（PC、手机）增长不及预期，可能引发新一轮库存周期调整。

### [2026 科技政策风向变了：从"弯道超车"到"换道领跑"，普通人能抓住什么机会？](https://zhuanlan.zhihu.com/p/2015356424050458927)
**摘要**：中国科技政策正从"追赶型"向"换道领跑"转变：工信部 2026 年部署十项重点工作，重点培育量子科技、生物制造、氢能与核聚变能、脑机接口、具身智能、第六代移动通信等"未来产业"。量子计算方面，105 比特超导量子原型机"祖冲之三号"已取得重大突破；人形机器人 2026 年开始进入家庭和养老机构试点；NPU 成为终端设备标配，本地 AI 推理成为主流。AI 产品经理、具身智能工程师、算力运维等岗位成为新蓝海。

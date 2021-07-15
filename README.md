# 一、测试理论

 ## 1、软件测试方法有哪些？

  - 黑盒、白盒、灰盒
    
 ## 2、设计一个模块测试用例

  - 考察面试者的经验、用例设计能力、思维、以及掌握的测试方法是否全面  
  - 从功能测试、接口测试、性能测试方面分析

 ## 3、你在测试中发现了一个bug，但是开发经理认为这不是一个bug，你应该怎样解决？

  - 首先，将问题提交到缺陷管理库进行备案。
  - 然后，要获取判断的依据和标准：
  - 根绝需求说明书，产品说明、设计文档等，确认实际结果是否与计划有不一致的地方，提供缺陷是都确认的直接依据；
  - 如果没有文档依据，根据类似软件的一般特性来说明是否存在不一致的地方，来确认是否是缺陷；
  - 根据用户的一般使用习惯，来确认是否是缺陷；
  - 与设计人员，开发人员和客户代表等相关人员探讨，确认是否是缺陷；
  - 合理论述，客观严谨的向测试经理说明自己的判断理由；
  - 等待测试经历做出最终决定，如果仍然存在争议，可以通过公司政策所提供的渠道，向上级反应，并由上级做出决定
  
 ## 4、给你一个网站，你如何测试？

  - 首先，查找需求说明、网站设计等相关文档，分析测试需求；
  - 制定测试计划，确定测试范围和测试策略，一般包括以下及部分，功能性测试、界面测试、性能测试、数据库测试、安全性测试、兼容性测试；
  - 设计测试用例：
  - 功能测试（包括不限于）：
  - 链接测试。链接是否正确跳转，是否存在空页面和无效页面，是否有不正确的出错信息返回
  - 提交功能的测试
  - 多媒体元素是否可以正确加载和显示
  - 多语言支持是否能够正确显示选择的语言
  - 界面测试（包括但不限于）：
  - 页面是否风格统一，美观
  - 页面布局是否合理，重点内容和热点内容是否突出
  - 空间是否正常使用
  - 对于必须但未安装的控件，是否提供自动下载并安装的功能
  - 文字检查
  - 性能测试：
  - 压力测试
  - 负载测试
  - 强度测试
  - 数据库测试：
  - 具体决定是否需要展开。数据库一般需要考虑连结性，对数据的存取操作，数据内容的验证等方面。
  - 安全性测试：
  - 基本的登陆功能的检查
  - 是否存在溢出错误，导致系统崩溃或者权限泄露
  - 相关开发语言的常见安全性问题检查，例如：SQL注入
  - 如果需要高级的安全性问题，确定获得专业安全公司的帮助，外包测试，或者获取支持
  - 兼容性测试，根据需求说明的内容，确定支持的平台组合：
  - 浏览器的兼容性
  - 操作系统的兼容性
  - 软件平台的兼容性
  - 数据库的兼容性
  - 开展测试，并记录缺陷，合理的安排调整测试进度，提前获取测试所需的资源，建立管理体系（例如：需求变更，风险，配置，测试文档，缺陷报告，人力资源等内容）
  - 定期评审，对测试进行评估和总结，调整测试内容
  
 ## 5、目前主要的测试用例方法是？
  - 白盒测试：路径覆盖、代码走查、静态分析
  - 黑盒测试：边界值分析，等价类划分，错误推测法，因果图，状态图法
 
 ## 6、软件测安全性从哪几个方面测试？
  - 软件安全性测试包括：程序、数据库安全测试
  - 用户认证安全的测试要考虑问题： 明确区分系统中不同用户权限 、系统中会不会出现用户冲突 、系统会不会因用户的权限的改变造成混乱 、用户登陆密码是否是可见、可复制 、是否可以通过绝对途径登陆系统（拷贝用户登陆后的链接直接进入系统）、用户退出系统后是否删除了所有鉴权标记，是否可以使用后退键而不通过输入口令进入 系统 、系统网络安全的测试要考虑问题 、测试采取的防护措施是否正确装配好，有关系统的补丁是否打上 、模拟非授权攻击，看防护系统是否坚固 、采用成熟的网络漏洞检查工具检查系统相关漏洞（即用最专业的黑客攻击工具攻击试一下，现在最常用的是 NBSI 系列和 IPhacker IP ） 、采用各种木马检查工具检查系统木马情况 、采用各种防外挂工具检查系统各组程序的外挂漏洞
  - 数据库安全考虑问题： 系统数据是否机密、系统数据的完整性 、系统数据可管理性 、系统数据的独立性 、系统数据可备份和恢复能力（数据备份是否完整，可否恢复，恢复是否可以完整）

## 7、什么是测试用例？什么是测试脚本？两者关系？
  - 测试用例：为实现测试而向被测试系统提供的输入数据、操作或各种环境设置以及期望结果的一个特定的合集
  - 测试脚本：为了进行自动化测试而编写的脚本
  - 关系：测试脚本的编写必须对应相应的测试用例

 ## 8、简述： 静态测试、动态测试、黑盒测试、白盒测试、α测试 、β测试
  - 静态测试：不运行程序本身而寻找程序代码中可能存在的错误或评估程序代码的过程
  - 动态测试：实际运行被测程序，输入相应的测试实例，检查运行结果与预期结果的差异，判定执行结果是否符合要求，从而检测程序的正确性、可靠性、有效性、并分析系统运行效率和健壮性等性能
  - 黑盒- 测试：一般用来确认软件功能的正确性和可操作性，目的是检测软件的各个功能是否得以实现，把北侧程序当作一个黑盒，不考虑其内部结构,在知道该程序的输入和输出之间的关系或程序功能的情况下,依靠软件规格说明书来确定测试用例和推断测试结果的正确性
  - 白盒测试：根据软件内部的逻辑结构分析来进行测试,是基于代码的测试，测试人员通过阅读程序代码或者通过使用开发工具中的单步调试来判断软件的质量，一般黑盒测试由项目经理在程序员开发中来实现。
  - α测:由一个用户在开发环境下进行的测试，也可以是公司内部的用户在模拟实际操作环境下进行的受控测试，Alpha测试不能由程序员或测试员完成
  - β测试: 软件的多个用户在一个或多个用户的实际使用环境下进行的测试，开发者通常不在测试现场，Beta测试不能由程序员或测试员完成

## 9、软件测试分为几个阶段，各阶段的测试策略和要求是什么？
  - 和开发过程相对应，测试过程会依次经历单元测试、集成测试、系统测试、验收测试四个主要阶段：
  - 单元测试：单元测试是针对软件设计的最小单位––程序模块甚至代码段进行正确性检验的测试工作，通常由开发人员进行。
  - 集成测试：集成测试是将模块按照设计要求组装起来进行测试，主要目的是发现与接口有关的问题。由于在产品提交到测试部门前，产品开发小组都要进行联合调试，因此在大部分企业中集成测试是由开发人员来完成的。
  - 系统测试：系统测试是在集成测试通过后进行的，目的是充分运行系统，验证各子系统是否都能正常工作并完成设计的要求。它主要由测试部门进行，是测试部门最大最重要的一个测试，对产品的质量有重大的影响。
  - 验收测试：验收测试以需求阶段的《需求规格说明书》为验收标准，测试时要求模拟实际用户的运行环境。对于实际项目可以和客户共同进行，对于产品来说就是最后一次的系统测试。测试内容为对功能模块的全面测试，尤其要进行文档测试。
  - 单元测试测试策略：
  - 自顶向下的单元测试策略- ：比孤立单元测试的成本高很多，不是单元测试的一个好的选择。
  - 自底向上的单元测试策略：比较合理的单元测试策略，但测试周期较长。
  - 孤立单元测试策略：最好的单元测试策略。
  - 集成测试的测试策略：
  - 大爆炸集成：适应于一个维护型项目或被测试系统较小
  - 自顶向下集成：适应于产品控制结构比较清晰和稳定；高层接口变化较小；底层接口未定义或经常可能被修改；产口控制组件具有较大的技术风险，需要尽早被验证；希望尽早能看到产品的系统功能行为。
  - 自底向上集成：适应于底层接口比较稳定；高层接口变化比较频繁；底层组件较早被完成。
  - 基于进度的集成
  - 优点：具有较高的并行度；能够有效缩短项目的开发进度。
  - 缺点：桩和驱动工作量较大；有些接口测试不充分；有些测试重复和浪费。
  - 系统测试的测试策略：
  - 数据和数据库完整性测试；功能测试；用户界面测试；性能评测；负载测试；强度测试；容量测试；安全性和访问控制测试；故障转移和恢复测试；配置测试；安装测试；加密测试；可用性测试；版本验证测试；文档测试

 ## 10、测试人员在软件开发过程中的任务是什么？
  - 1、尽可能早的找出系统中的Bug；
  - 2、避免软件开发过程中缺陷的出现；
  - 3、衡量软件的品质，保证系统的质量；
  - 4、关注用户的需求，并保证系统符合用户需求。
  - 总的目标是：确保软件的质量。

 ## 11、在您以往的工作中，一条软件缺陷（或者叫Bug）记录都包含了哪些内容？如何提交高质量的软件缺陷（Bug）记录？
  ### 1. 一条Bug记录最基本应包含：
   - bug编号
   - bug严重级别，优先级
   - bug产生的模块首先要有bug摘要，阐述bug大体的内容；
   - bug对应的；
   - bug详细现象描述，包括一些截图、录像....
   - b   ug出现时的测试环境，产生的条件即对应操作步骤；
  ### 2. 高质量的Bug记录：
   - 1) 通用UI要统一、准确
　　缺陷报告的UI要与测试的软件UI保持一致，便于查找定位。
   - 2) 尽量使用业界惯用的表达术语和表达方法
　　使用业界惯用的表达术语和表达方法，保证表达准确，体现专业化。
   - 3) 每条缺陷报告只包括一个缺陷
　　每条缺陷报告只包括一个缺陷，可以使缺陷修正者迅速定位一个缺陷，集中精力每次只修正一个缺陷。校验者每次只校验一个缺陷是否已经正确修正。
   - 4) 不可重现的缺陷也要报告
　　首先缺陷报告必须展示重现缺陷的能力。不可重现的缺陷要尽力重现，若尽力之后仍不能重现，仍然要报告此缺陷，但在报告中要注明无法再现，缺陷出现的频率。
   - 5) 明确指明缺陷类型
　　根据缺陷的现象，总结判断缺陷的类型。例如，即功能缺陷、界面缺陷、数据缺陷，合理化建议这是最常见的缺陷或缺陷类型，其他形式的缺陷或缺陷也从属于其中某种形式。
   - 6) 明确指明缺陷严重等级和优先等级
　　时刻明确严重等级和优先等级之间的差别。高严重问题可能不值得解决，小装饰性问题可能被当作高优先级。
   - 7) 描述 (Description) ，简洁、准确，完整，揭示缺陷实质，记录缺陷或缺陷出现的位置
　　描述要准确反映缺陷的本质内容，简短明了。为了便于在软件缺陷管理数据库中寻找制定的测试缺陷，包含缺陷发生时的用户界面（UI）是个良好的习惯。例如记录对话框的标题、菜单、按钮等控件的名称。
   - 8) 短行之间使用自动数字序号，使用相同的字体、字号、行间距
　　短行之间使用自动数字序号，使用相同的字体、字号、行间距，可以保证各条记录格式一致，做到规范专业。
   - 9) 每一个步骤尽量只记录一个操作
　　保证简洁、条理井然，容易重复操作步骤。
   - 10) 确认步骤完整，准确，简短
　　保证快速准确的重复缺陷，“完整”即没有缺漏，“准确”即步骤正确，“简短”即没有多余的步骤。
   - 11) 根据缺陷，可选择是否进行图象捕捉
　　为了直观的观察缺陷或缺陷现象，通常需要附加缺陷或缺陷出现的界面，以图片的形式作为附件附着在记录的“附件”部分。为了节省空间，又能真实反映缺陷或缺陷本质，可以捕捉缺陷或缺陷产生时的全屏幕，活动窗口和局部区域。为了迅速定位、修正缺陷或缺陷位置，通常要求附加中文对照图。
　　? 附加必要的特殊文档和个人建议和注解
　　如果打开某个特殊的文档而产生的缺陷或缺陷，则必须附加该文档，从而可以迅速再现缺陷或缺陷。有时，为了使缺陷或缺陷修正者进一步明确缺陷或缺陷的表现，可以附加个人的修改建议或注解。
   - 12) 检查拼写和语法缺陷
　　在提交每条缺陷或缺陷之前，检查拼写和语法，确保内容正确，正确的描述缺陷。
   - 13) 尽量使用短语和短句，避免复杂句型句式
　　软件缺陷管理数据库的目的是便于定位缺陷，因此，要求客观的描述操作步骤，不需要修饰性的词汇和复杂的句型，增强可读性。
　　以上概括了报告测试缺陷的规范要求，随着软件的测试要求不同，测试者经过长期测试，积累了相应的测试经验，将会逐渐养成良好的专业习惯，不断补充新的规范书写要求。此外，经常阅读、学习其他测试工程师的测试缺陷报告，结合自己以前的测试缺陷报告进行对比和思考，可以不断提高技巧。
   - 14) 缺陷描述内容
　　缺陷描述的内容可以包含缺陷操作步骤，实际结果和期望结果。操作步骤可以方便开发人员再现缺陷进行修正，有些开发的再现缺陷能力很差，虽然他明白你所指的缺陷，但就是无法再现特别是对系统不熟悉的新加入开发人员，介绍步骤可以方便他们再现。实际结果可以让开发明白错误是什么，期望结果可以让开发了解正确的结果应该是如何。
　　
 ## 12、黑盒测试和白盒测试是软件测试的两种基本方法，请分别说明各自的优点和缺点！
  - 黑盒测试
　　优点：比较简单，不需要了解程序内部的代码及实现；与软件的内部实现无关；  从用户角度出发，能很容易的知道用户会用到哪些功能，会遇到哪些问题；基于软件开发文档，所以也能知道软件实现了文档中的哪些功能；在做软件自动化测试时较为方便。
　　缺点：不可能覆盖所有的代码，覆盖率较低，大概只能达到总代码量的30%；自动化测试的复用性较低。
  - 白盒测试
　　优点：帮助软件测试人员增大代码的覆盖率，提高代码的质量，发现代码中隐    藏的问题。
　　缺点：程序运行会有很多不同的路径，不可能测试所有的运行路径；测试基于代码，只能测试开发人员做的对不对，而不能知道设计的正确与否，可能会漏掉一些功能需求；系统庞大时，测试开销会非常大。

 ## 13、如何测试一个纸杯？
 
  - 用户文档：使用手册是否对杯子的用法、限制、使用条件等有详细描述
  - 功能度：用水杯装水看漏不漏；水能不能被喝到
  - 安全性：杯子有没有毒或细菌
  - 可靠性：杯子从不同高度落下的损坏程度
  - 可移植性：杯子在不同的地方、温度等环境下是否都可以正常使用
  - 兼容性：杯子是否能够容纳果汁、白水、酒精、汽油等
  - 易用性：杯子是否烫手、是否有防滑措施、是否方便饮用
  - 疲劳测试：将杯子盛上水（案例一）放24小时检查泄漏时间和情况；盛上汽油（案例二）放24小时检查泄漏时间和情况等
  - 压力测试：用根针并在针上面不断加重量，看压强多大时会穿透

 ## 14、测试计划工作的目的是什么？测试计划文档的内容应该包括什么？其中哪些是最重要的？
 
  - 软件测试计划是指导测试过程的纲领性文件：
  - 领导能够根据测试计划进行宏观调控，进行相应资源配置等
  - 测试人员能够了解整个项目测试情况以及项目测试不同阶段的所要进行的工作等
  - 便于其他人员了解测试人员的工作内容，进行有关配合工作
  - 包含了产品概述、测试策略、测试方法、测试区域、测试配置、测试周期、测试资源、测试交流、风险分析等内容。借助软件测试计划，参与测试的项目成员，尤其是测试管理人员，可以明确测试任务和测试方法，保持测试实施过程的顺畅沟通，跟踪和控制测试进度，应对测试过程中的各种变更。
  - 测试计划编写6要素（5W1H）：
  - why——为什么要进行这些测试；
  - what—测试哪些方面，不同阶段的工作内容；
  - when—测试不同阶段的起止时间；
  - where—相应文档，缺陷的存放位置，测试环境等；
  - who—项目有关人员组成，安排哪些测试人员进行测试；
  - how—如何去做，使用哪些测试工具以及测试方法进行测试
  - 测试计划和测试详细规格、测试用例之间是战略和战术的关系，测试计划主要从宏观上规划测试活动的范围、方法和资源配置，而测试详细规格、测试用例是完成测试任务的具体战术。所以其中最重要的是测试测试策略和测试方法（最好是能先评审）。
　　
 ## 15、详细的描述一个测试活动完整的过程
　　（以瀑布模型为例）
　　项目经理通过和客户的交流，完成需求文档，由开发人员和测试人员共同完成需求文档的评审，评审的内容包括：需求描述不清楚的地方和可能有明显冲突或者无法实现的功能的地方。项目经理通过综合开发人员，测试人员以及客户的意见，完成项目计划。然后SQA进入项目，开始进行统计和跟踪
　　开发人员根据需求文档完成需求分析文档，测试人员进行评审，评审的主要内容包括是否有遗漏或双方理解不同的地方。测试人员完成测试计划文档，测试计划包括的内容上面有描述。
　　测试人员根据修改好的需求分析文档开始写测试用例，同时开发人员完成概要设计文档，详细设计文档。此两份文档成为测试人员撰写测试用例的补充材料。
　　测试用例完成后，测试和开发需要进行评审。
　　测试人员搭建环境
　　开发人员提交第一个版本，可能存在未完成功能，需要说明。测试人员进行测试，发现BUG后提交给BugZilla。
　　开发提交第二个版本，包括Bug Fix以及增加了部分功能，测试人员进行测试。
　　重复上面的工作，一般是3-4个版本后BUG数量减少，达到出货的要求。
　　如果有客户反馈的问题，需要测试人员协助重现并重新测试。
　　
 ## 16、一台客户端有三百个客户与三百个客户端有三百个客户对服务器施压，有什么区别?
　　300个用户在一个客户端上，会占用客户机更多的资源，而影响测试的结果。线程之间可能发生干扰，而产生一些异常。
　　300个用户在一个客户端上，需要更大的带宽。
　　IP地址的问题，可能需要使用IP Spoof来绕过服务器对于单一IP地址最大连接数的限制。
　　所有用户在一个客户端上，不必考虑分布式管理的问题；而用户分布在不同的客户端上，需要考虑使用控制器来整体调配不同客户机上的用户。同时，还需要给予相应的权限配置和防火墙设置。
　
　　
 ## 17、软件生存周期及其模型是什么？
　　软件生存周期（Software life cycle）又称为软件生命周期，生存期。是指从形成开发软件概念起，所开发的软件使用以后，直到失去使用价值消亡为止的整个过程。一般来说，整个生存周期包括，计划、开发、运行（维护）三个时期，每个时期又划分为若干个阶段，每个阶段有明确的任务。
　　周期模型（典型的几种）：
　　瀑布模型
　　快速原型模型：快速原型模型允许在需求分析阶段对软件的需求进行初步而非完全的分析和定义，快速设计开发出软件系统的原型，该原型向用户展示待开发软件的全部或部分功能和性能；用户对该原型进行测试评定，给出具体改进意见以丰富细化软件需求；开发人员据此对软件进行修改完善，直至用户满意认可之后，进行软件的完整实现及测试、维护。
　　迭代模型：迭代包括产生产品发布（稳定、可执行的产品版本）的全部开发活动和要使用该发布必需的所有其他外围元素。在某种程度上，开发迭代是一次 完整地经过所有工作流程的过程：需求分析、设计、实施和测试工作流程。实质上，它类似小型的瀑布式项目。RUP认为，所有的阶段都可以细分为迭代。每一次 的迭代都会产生一个可以发布的产品，这个产品是最终产品的一个子集。
　　生命周期阶段：
　　软件计划与可行性分析
　　需求分析
　　软件设计
　　编码
　　软件测试
　　运行与维护
　　
 ## 18、什么是软件测试？目的和原则？
　　在规定的条件下对程序进行操作，以发现程序错误，衡量软件质量，并对其是否能满足设计要求进行评估的过程
　　软件测试的目的：
　　测试是程序的执行过程，目的在于发现错误
　　一个成功的测试用例在于发现至今未发现的错误
　　一个成功测试是发现了至今未发现的错误的测试
　　确保产品完成了她所承受或公布的功能，并且用户可以访问到的功能都有明确的书面说明
　　确保产品满足性能和效率的要求
　　确保产品是健壮的和适应用户环境的
　　软件测试的原则：
　　测试用例中一个必须部分是对预期输出或接过进行定义
　　程序员应避免测试自己编写的程序
　　编写软件的组织不应当测试自己编写的软件
　　应当彻底检查每个测试的执行结果
　　测试用例的编写不仅应当根据有效和预料到的输入情况，而且也应当根据无效和未预料到的输入情况
　　检擦程序是否“未做其应该做的”仅是测试的一半，测试的另一半是检查程序是否“做了其不应该做的”
　　应避免测试用例用后即弃，除非软件本身就是个一次性的软件
　　计划测试工作时不应默许假定不会发现错误
　　程序某部分存在更多错误的可能性，与该部分已经发现错误的数量成正比
　　软件测试是一项极富创造性，极具智力的挑战性的工作
　　

 ## 19、您认为在测试人员同开发人员的沟通过程中，如何提高沟通的效率和改善沟通的效果？维持测试人员同开发团队中其他成员良好的人际关系的关键是什么？
　　尽量面对面的沟通，其次是能直接通过电话沟通，如果只能通过Email等非及时沟通工具的话，强调必须对特性的理解深刻以及能表达清楚。
　　运用一些测试管理工具如TestDirector进行管理也是较有效的方法，同时要注意在TestDirector中对BUG有准确的描述。
　　在团队中建立测试人员与开发人员良好沟通中注意以下几点：
　　一真诚、二是团队精神、三是在专业上有共同语言、四是要对事不对人，工作至上
　　当然也可以通过直接指出一些小问题，而不是进入BUG Tracking System来增加对方的好感。
　　
 ## 20、Internet采用哪种网络协议？该协议的主要层次结构？Internet物理地址和IP地址转换采用什么协议？
　　TCP/IP协议主要层次结构为： 应用层/传输层/网络层/数链路层。
　　ARP (Address Resolution Protocol)（地据址解析协议）
　　
 ## 21、软件验收测试包括正式验收测试、alpha测试、beta测试三种测试。
　　
 ## 22、系统测试的策略有很多种的，有性能测试、负载测试、强度测试、易用性测试、安全测试、配置测试、安装测试、文档测试、故障恢复测试、用户界面测试、恢复测试、分布测试、可用性测试。
　　
 ## 23、设计系统测试计划需要参考的项目文档有软件测试计划、软件需求工件、和迭代计划
　　
 ## 24、 设计测试用例时应该考虑哪些方面，即不同的测试用例针对那些方面进行测试？
　　设计测试用例时需要注意的是，除了对整体流程及功能注意外，还要注意强度测试、性能测试、压力测试、边界值测试、稳定性测试、安全性测试等多方面。（测试用例需要考虑的四个基本要素是输入、输出、操作和测试环境；另外，测试用例需要考虑的是测试类型（功能、性能、安全……），这部分可以参照TP做答。此外，还需要考虑用例的重要性和优先级）
　　
 ## 25、假设有一个文本框要求输入10个字符的邮政编码，对于该文本框应该怎样划分等价类？
　　特殊字符，如10个*或￥；英文字母，如ABCDefghik；小于十个字符，如123；大于十个字符，如11111111111；数字和其他混合，如123AAAAAAA；空字符；保留字符
　　
 ## 26.软件测试项目从什么时候开始，？为什么？
　　软件测试应该在需求分析阶段就介入,因为测试的对象不仅仅是程序编码,应该对软件开发过程中产生的所有产品都测试,并且软件缺陷存在放大趋势.缺陷发现的越晚,修复它所花费的成本就越大.
　　
 ## 27、什么是回归测试?
　　回归测试: (regression   testing): 回归测试有两类：用例回归和错误回归；用例回归是过一段时间以后再回头对以前使用过的用例在重新进行测试，看看会重新发现问题。错误回归，就是在新版本中，对以前版本中出现并修复的缺陷进行再次验证，并以缺陷为核心，对相关修改的部分进行测试的方法。
　　
 ## 28.单元测试、集成测试、系统测试的侧重点是什么？
　　单元测试针对的是软件设计的最小单元--程序模块（面向过程中是函数、过程；面向对象中是类。）,进行正确性检验的测试工作,在于发现每个程序模块内部可能存在的差错.一般有两个步骤:人工静态检查\动态执行跟踪
　　集成测试针对的是通过了单元测试的各个模块所集成起来的组件进行检验,其主要内容是各个单元模块之间的接口,以及各个模块集成后所实现的功能.
　　系统测试针对的是集成好的软件系统，作为整个计算机系统的一个元素,与计算机硬件\外设\某些支持软件\数据和人员等其他系统元素结合在一起,要在实际的运行环境中,对计算机系统进行一系列的集成测试和确认测试.
　　
 ## 29：你所了解的的软件测试类型都有哪些，简单介绍一下。
　　按测试策略分类：1、静态与动态测试2、黑盒与白盒测试 3、手工和自动测试 4、冒烟测试 5、回归测试；
　　按测试阶段分类：单元测试、集成测试、系统测试；
　　其他常见测试方法：1、功能测试 2、性能测试 3、压力测试 4、负载测试 5、易用性测试 6、安装测试 7、界面测试 8、配置测试 9、文档测试 10、兼容性测试 11、安全性测试 12、恢复测试
　　
 ## 30：你认为做好测试计划工作的关键是什么？
　　明确测试的目标，增强测试计划的实用性
　　编写软件测试计划得重要目的就是使测试过程能够发现更多的软件缺陷，因此软件测试计划的价值取决于它对帮助管理测试项目，并且找出软件潜在的缺陷。因此，软件测试计划中的测试范围必须高度覆盖功能需求，测试方法必须切实可行，测试工具并且具有较高的实用性，便于使用，生成的测试结果直观、准确
　　坚持“5W”规则，明确内容与过程
　　“5W”规则指的是“What（做什么）”、“Why（为什么做）”、“When（何时做）”、“Where（在哪里）”、“How（如何做）”。利用“5W”规则创建软件测试计划，可以帮助测试团队理解测试的目的（Why），明确测试的范围和内容（What），确定测试的开始和结束日期（When），指出测试的方法和工具（How），给出测试文档和软件的存放位置（Where）。
　　采用评审和更新机制，保证测试计划满足实际需求
　　测试计划写作完成后，如果没有经过评审，直接发送给测试团队，测试计划内容的可能不准确或遗漏测试内容，或者软件需求变更引起测试范围的增减，而测试计划的内容没有及时更新，误导测试执行人员。
　　分别创建测试计划与测试详细规格、测试用例
　　应把详细的测试技术指标包含到独立创建的测试详细规格文档，把用于指导测试小组执行测试过程的测试用例放到独立创建的测试用例文档或测试用例管理数据库中。测试计划和测试详细规格、测试用例之间是战略和战术的关系，测试计划主要从宏观上规划测试活动的范围、方法和资源配置，而测试详细规格、测试用例是完成测试任务的具体战术。
　　
 ## 31：您认为做好测试用例设计工作的关键是什么？
　　白盒测试用例设计的关键是以较少的用例覆盖尽可能多的内部程序逻辑结果
　　黑盒法用例设计的关键同样也是以较少的用例覆盖模块输出和输入接口。不可能做到完全测试，以最少的用例在合理的时间内发现最多的问题
　　
 ## 32：你的测试职业发展目标是什么？
　　测试经验越多，测试能力越高。所以我的职业发展是需要时间累积的，一步步向着高级测试工程师奔去。而且我也有初步的职业规划，前3年累积测试经验，不断的更新自己改正自己，做好测试任务。
　　
 ## 33：测试结束的标准是什么？
　　从微观上来说，在测试计划中定义，比如系统在一定性能下平稳运行72小时，目前Bug Tracking System中，本版本中没有一般严重的BUG，普通BUG的数量在3以下，BUG修复率90%以上等等参数，然后由开发经理，测试经理，项目经理共同签字认同版本Release。
　　如果说宏观的，则是当这个软件彻底的消失以后，测试就结束了。
　　
 ## 34、一套完整的测试应该由哪些阶段组成？
　　可行性分析、需求分析、概要设计、详细设计、编码、单元测试、集成测试、系统测试、验收测试
　　
 ## 35、您是否了解以往所工作的企业的软件开发过程？如果了解，请试述一个完整的开发过程需要完成哪些工作？分别由哪些不同的角色来完成这些工作？您在以往的测试工作中都曾经具体从事过哪些工作？其中最擅长哪部分工作？
　　开发过程---需求调研（需求人员）、需求分析（需求人员）、概要设计（设计人员）、详细设计(设计人员)、编码（开发人员）
　　测试过程---需求评审、系统测试设计、概要设计评审、集成测试设计、详细设计评审、单元测试设计、测试执行
　　测试工作的整个过程都做过，擅长做测试设计
　　过程决定质量，软件的过程改进正是为了提高软件的质量，将过往的种种经验教训积累起来。
　　
 ## 36、测试用例设计的原则是什么？目前主要的测试用例设计方法有哪些？
　　代表性：能够代表并覆盖各种合理的和不合理、合法的和非法的、边界的和越界的、以及极限的输入数据、操作和环境设置等.
　　可判定性：即测试执行结果的正确性是可判定的，每一个测试用例都应有相应的期望结果.
　　可再现性：即对同样的测试用例，系统的执行结果应当是相同的。
　　方法有等价类、边界值、因果图、状态图、正交法、大纲法
　
 ## 37、您所熟悉的软件测试类型都有哪些？请试着分别比较这些不同的测试类型的区别与联系（如功能测试、性能测试……）
　　测试类型有：功能测试，性能测试，界面测试。
　　功能测试在测试工作中占的比例最大，功能测试也叫黑盒测试。是把测试对象看作一个黑盒子。利用黑盒测试法进行动态测试时，需要测试软件产品的功能，不需测试软件产品的内部结构和处理过程。采用黑盒技术设计测试用例的方法有：等价类划分、边界值分析、错误推测、因果图和综合策略。
　　性能测试是通过自动化的测试工具模拟多种正常、峰值以及异常负载条件来对系统的各项性能指标进行测试。负载测试和压力测试都属于性能测试，两者可以结合进行。通过负载测试，确定在各种工作负载下系统的性能，目标是测试当负载逐渐增加时，系统各项性能指标的变化情况。压力测试是通过确定一个系统的瓶颈或者不能接收的性能点，来获得系统能提供的最大服务级别的测试。
　　界面测试，界面是软件与用户交互的最直接的层，界面的好坏决定用户对软件的第一印象。而且设计良好的界面能够引导用户自己完成相应的操作，起到向导的作用。同时界面如同人的面孔，具有吸引用户的直接优势。设计合理的界面能给用户带来轻松愉悦的感受和成功的感觉，相反由于界面设计的失败，让用户有挫败感，再实用强大的功能都可能在用户的畏惧与放弃中付诸东流。
　　区别在于，功能测试关注产品的所有功能上，要考虑到每个细节功能，每个可能存在的功能问题。性能测试主要关注于产品整体的多用户并发下的稳定性和健壮性。界面测试更关注于用户体验上，用户使用该产品的时候是否易用，是否易懂，是否规范（快捷键之类的），是否美观（能否吸引用户的注意力），是否安全（尽量在前台避免用户无意输入无效的数据，当然考虑到体验性，不能太粗鲁的弹出警告）？做某个性能测试的时候，首先它可能是个功能点，首先要保证它的功能是没问题的，然后再考虑该功能点的性能测试
　　
 ## 38、请试着比较一下黑盒测试、白盒测试、单元测试、集成测试、系统测试、验收测试的区别与联系。
　　黑盒测试：已知产品的功能设计规格，可以进行测试证明每个实现了的功能是否符合要求。
　　白盒测试：已知产品的内部工作过程，可以通过测试证明每种内部操作是否符合设计规格要求，所有内部成分是否以经过检查。
　　软件的黑盒测试意味着测试要在软件的接口处进行。这种方法是把测试对象看做一个黑盒子，测试人员完全不考虑程序内部的逻辑结构和内部特性，只依据程序的需求规格说明书，检查程序的功能是否符合它的功能说明。因此黑盒测试又叫功能测试或数据驱动测试。黑盒测试主要是为了发现以下几类错误：
　　1、是否有不正确或遗漏的功能？2、在接口上，输入是否能正确的接受？能否输出正确的结果？3、是否有数据结构错误或外部信息（例如数据文件）访问错误？4、性能上是否能够满足要求？5、是否有初始化或终止性错误？
　　软件的白盒测试是对软件的过程性细节做细致的检查。这种方法是把测试对象看做一个打开的盒子，它允许测试人员利用程序内部的逻辑结构及有关信息，设计或选择测试用例，对程序所有逻辑路径进行测试。通过在不同点检查程序状态，确定实际状态是否与预期的状态一致。因此白盒测试又称为结构测试或逻辑驱动测试。白盒测试主要是想对程序模块进行如下检查：
　　1、对程序模块的所有独立的执行路径至少测试一遍。
　　2、对所有的逻辑判定，取“真”与取“假”的两种情况都能至少测一遍。
　　3、在循环的边界和运行的界限内执行循环体。
　　4、测试内部数据结构的有效性，等等。
　　单元测试（模块测试）是开发者编写的一小段代码，用于检验被测代码的一个很小的、很明确的功能是否正确。通常而言，一个单元测试是用于判断某个特定条件（或者场景）下某个特定函数的行为。
　　单元测试是由程序员自己来完成，最终受益的也是程序员自己。可以这么说，程序员有责任编写功能代码，同时也就有责任为自己的代码编写单元测试。执行单元测试，就是为了证明这段代码的行为和我们期望的一致。
　　集成测试（也叫组装测试，联合测试）是单元测试的逻辑扩展。它的最简单的形式是：两个已经测试过的单元组合成一个组件，并且测试它们之间的接口。从这一层意义上讲，组件是指多个单元的集成聚合。在现实方案中，许多单元组合成组件，而这些组件又聚合成程序的更大部分。方法是测试片段的组合，并最终扩展进程，将您的模块与其他组的模块一起测试。最后，将构成进程的所有模块一起测试。
　　系统测试是将经过测试的子系统装配成一个完整系统来测试。它是检验系统是否确实能提供系统方案说明书中指定功能的有效方法。（常见的联调测试）
　　系统测试的目的是对最终软件系统进行全面的测试，确保最终软件系统满足产品需求并且遵循系统设计。
　　验收测试是部署软件之前的最后一个测试操作。验收测试的目的是确保软件准备就绪，并且可以让最终用户将其用于执行软件的既定功能和任务。
　　验收测试是向未来的用户表明系统能够像预定要求那样工作。经集成测试后，已经按照设计把所有的模块组装成一个完整的软件系统，接口错误也已经基本排除了，接着就应该进一步验证软件的有效性，这就是验收测试的任务，即软件的功能性能如同用户所合理期待的那样。
　　
 ## 39、当开发人员说不是BUG时，你如何应付？
 
  - 开发人员说不是bug，有2种情况，一是需求没有确定，所以我可以这么做，这个时候可以找来产品经理进行确认，需不需要改动，3方商量确定好后再看要不要改。二是这种情况不可能发生，所以不需要修改，这个时候，我可以先尽可能的说出是BUG的依据是什么？如果被用户发现或出了问题，会有什么不良结果？程序员可能会给你很多理由，你可以对他的解释进行反驳。如果还是不行，那我可以给这个问题提出来,跟开发经理和测试经理进行确认,如果要修改就改,如果不要修改就不改。其实有些真的不是bug，我也只是建议的方式写进TD中，如果开发人员不修改也没有大问题。如果确定是bug的话，一定要坚持自己的立场，让问题得到最后的确认。

 ## 40、什么是兼容性测试？请举例说明如何利用兼容性测试列表进行测试。
 
  - 主要验证软件产品在不同版本之间的兼容性。包括向下兼容和交错兼容，向下兼容是测试软件新版本保留它早期版本功能的情况，交错兼容是验证共同存在的两个相关但不相同的产品之间的兼容性。
　　
 ## 41、对某软件进行测试，发现在WIN98上运行得很慢，怎么判别是该软件存在问题还是其软硬件运行环境存在问题？
 
  - 看软件的运行环境要求。如果符合要求则是程序存在问题，若不符合要求则是硬件系统存在问题
　　
 ## 42、需求测试的注意事项有哪些？
 
  - 是否使用了公司的模板、文档内容是否符合规范、所有的需求是分级是否清析适当、所有的需求是否具有一致性、需求是否可行（即，该需求组合有解决方案）、需求可否用己知的约束来实现、需求是否足够（即，可以把它送到一个规范的开发组织，并有一个生产出所需要产品的合理的可能性）、所有的其它需求是交叉引用是否正确、用户描述是否清楚、是否用客户的语言来描述需求、每个需求描述是否清楚没有岐义，可以移交给一个独立的组去实现时也能理解、是否所有的需求都是可验证的、是否每条需求都具有独立性，即使发生了变化也不会影响其它需求、性能指标是否明确、非功能性需求是否得到充分表现、是否完整列出适用的标准或协议、标准和协议之间是否存在冲突

 ## 43、主键、外键的作用，索引的优点与不足?
  - 答：主键：是表中的唯一标示键。作用：保证实体的完整性;加快数据库的操作速度;增加新的表记录时，数据库会自动检索新记录的主键值，不允许该值与其他表中记录的主键重复;数据库会按主键值的顺序显示记录，如果没有设定主键，则按输入的顺序显示记录。
　　外键：是主键的从属，表示了两个表之间的联系。作用：使用外键可以避免冗余。
　　索引的优点： 1、通过创建唯一性的索引，可以保证表中数据的唯一性; 2、加速数据的检索速度; 3、加快表与表之间的连接; 4、在使用分组与排序数据检索时，可以显著检索分组与排序的时间; 5、在查询的过程中使用优化隐藏器，提供系统性能。
　　缺点： 1、创建索引需要时间，且随着数据量的增加而增加; 2、索引需要占用物理空间;
　　3、当对表中数据进行修改时，索引也要动态维护，降低了数据的维护速度。
　　
 ## 44、性能测试的流程?
 
  - 1.测试需求分析 
  - 2.测试计划制定与评审
  - 3.测试用例设计与开发
  - 4.测试执行与监控
  - 5.分析测试结果
  - 6.编写性能测试报告 
  - 7.测试经验总结
　　
 ## 45、简述bug的生命周期?
 
  - 1， 有效地记录BUG 
  - 2， 使用BUG模板 
  - 3， 评价BUG优先级和严重性 
  - 4， BUG的生命 
  - 5， 维护BUG数据库
　　
 ## 46、您认为做好测试计划工作的关键是什么?
 
  - 了解项目或系统的业务需求
  - 和项目经理协调好，了解项目的进度计划安排情况
　　
 ## 47、您认为做好测试用例设计工作的关键是什  - 
 
  - 对业务和软件需求非常清楚，可以根据需求不同选择不同的测试用例设计
　　
 ## 48、您以往的工作中是否曾开展过测试用例的评审工作?如果有，请描述测试用例评审的过程和评审的内容。
 
  - 评审计划->预审->评审;
  - 评审内容主要是测试用例对软件需求的覆盖程度，对于相关边界是否考虑，是否针对复杂流程准备多套测试数据，是否有专门针对非功能性需求的测试。
　　
 ## 49、您认为性能测试工作的目的是什么?做好性能测试工作的关键是什么?
 
  - 关键是测试脚本的录制，测试时候测试环境的干净。
　
 ## 50、您如何看待软件过程改进?在您曾经工作过的企业中，是否有一些需要改进的东西呢?您期望的理想的测试人员的工作环境是怎样的?
  
  - 将先进的经验或思想固化到过程中，通过过程改进和能力提高来改进软件质量


# 二、网络协议

 ## 1、http与https有何区别

  - https协议需要到ca申请证书，一般免费证书较少，因而需要一定 - 
  - http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输 - 
  - http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是4 - 
  - http的连接很简单，是  状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
  
  
 ## 2、HTTP状态响应码
 
  ### 1、200-299成功响应
  
   - 200 OK： 请求成功
   - 201 Created: 常用于POST，PUT 请求，表明请求已经成功，并新建了一个资源。并在响应体中返回路径。
   - 202 Accepted: 请求已经接收到，但没有响应，稍后也不会返回一个异步请求结果。 该状态码适用于等待其他进程处理或者批处理的场景。
   - 203 No-Authoritative Information: 表明响应返回的元信息（meta-infomation）和最初的服务器不同，而是从本地或者第三方获取的。主要用于其他资源的镜像和备份。除了前面的情况，首选还是200。
   - 204 No Content: 请求没有数据返回，但是头信息有用。用户代理(浏览器)会更新缓存的头信息。
   - 205 Reset Content: 告诉用户代理（浏览器）重置发送该请求的文档。
   - 206 Partical Content: 当客户端使用Range请求头时，返回该状态码。

  ### 2、300-399重定向消息
  
   - 300 Multiple Choice： 返回多个响应，需要浏览器或者用户选择；
   - 301 Moved Permanently: 请求资源的URL被永久的改变，新的URL会在响应的Location中给出。浏览器到新的URL重新请求资源，因为有些客户端会把请求方式method改成GET。所以该状态码建议GET和HEAD方法中使用。搜索引擎会更新地址到资源的链接（SEO中‘link-judge’被发送到新的URL）。
   - 302 Found:  请求资源的URL被暂时修改到Location提供的URL。未来可能还会有新的修改。浏览器会根据新的URL重新请求资源。有些客户端会把方法method改为GET，建议在GET和HEAD方法中使用。搜索引擎不会更改URL到资源的。
   - 304 Not Modified: 资源未变更。服务器根据请求头判断，需要资源未修改，只返回响应头；否则将资源一起返回。

    发生场景：
     1）请求方法安全（如GET，HEAD请求）
     2）条件请求并且使用了If-None-Match或者If-Modified-Since 的请求头，如果想使用200状态码达到相同304效果，需要强制缓存，需要额外的请求头：Cache-Control, Expires, Vary

  ### 3、 400-499 客户端错误响应
  
   - 400 Bad Request: 请求语法有问题，服务器无法识别。没有host请求头字段，或者设置了超过一个的host请求头字段。
   - 401 UnAuthorized: 客户端未授权该请求。缺乏有效的身份认证凭证，一般可能是未登陆。登陆后一般都解决问题。
   - 403 Forbidden: 服务器拒绝响应。权限不足。
   - 404 Not Found: URL无效或者URL有效但是没有资源。
   - 405 Method Not Allowed: 请求方式Method不允许。但是GET和HEAD属于强制方式，不能返回这个状态码。
   - 406 Not Acceptable: 资源类型不符合服务器要求。
   - 407 Proxy Authorization Required: 需要代理授权。
   - 408 Request Timeout：服务器将不再使用的连接关闭。响应头会有Connection: close。
   - 426 Upgrade Required: 告诉客户端需要升级通信协议。

  ### 4、 500-599 服务器错误响应
   - 500 Internal Server Error: 服务器内部错误，未捕获。
   - 502 Bad Gateway: 服务器作为网关使用时，收到上游服务器返回的无效响应。
   - 503 Service Unavailable: 无法服务。一般发生在因维护而停机或者服务过载。一般还会伴随着返回一个响应头Retry-After: 说明恢复服务的估计时间。
   - 504 Gateway Timeout: 网关超时。服务器作为网关或者代理，不能及时从上游服务器获取响应返回给客户端。
   - 505 Http Version Not Supported: 发出的请求http版本服务器不支持。如果请求通过http2发送，服务器不支持http2.0，就会返回该状态码。


 ## 3、tcp/ip三次握手 

    ①含义理解

     TCP/IP协议不仅仅指的是TCP 和IP两个协议，而是指一个由FTP、SMTP、TCP、UDP、IP等协议构成的协议簇， 只是因为在TCP/IP协议中TCP协议和IP协议最具代表性，所以被称为TCP/IP协议。

    ②三次握手：

     （1）客户 端发送一个带SYN标志的TCP报文到server。这是三次握手过程中的报文1。
     （2） server端回应client的，这是三次握手中的第2个报文。这个报文同一时候带ACK标志和SYN标志。

    因此它表示对刚才clientSYN报文的回应。同一时候又标志SYN给client，询问client是否准备好进行数据通 讯。

     （3） 客户必须再次回应服务段一个ACK报文，这是报文段3。

     （4）连接终止协议（四次握手）
     
 ## 4、cookie、token、session的区别
   
    最近在总结一些容易理解混淆的概念，之前面试的时候提到过，我觉得也说不清楚，这两天项目做接口测试发现用的cookie而不是之前的token，于是总结一下，便于以后用到的时候再阅读以及分享给需要的人。后期如果发现总结不对会持续更新

    从安全性优先级来说：

    ### 1、优先级
      Cookie<session<token

    ### 2、 安全性
      Cookie:

      ①cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑到安全应当使用session

      ②HTTP是一种无状态协议,服务器没有办法单单从网络连接上面知道访问者的身份,为了解决这个问题,就诞生了Cookie

      Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie

      客户端浏览器会把Cookie保存起来。当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器。服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。

 
     session:

       ①session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能，考虑到减轻服务器性能方面，应当使用cookie

       ②关闭浏览器不会关闭session,它具失效日期，失效后服务器认为客户端停止了活动，并删除session以节省空间

 
     Token:

      ①  作为身份认证 token安全性比session好，因为每个请求都有签名还能防止监听以及重放攻击

      ②  Oauth token提供的是认证和授权，认证针对用户，授权针对app

      ③  token的生成一般是采用uuid保证唯一性，当用户登录时为其生成唯一的token，存储一般保存在数据库中。token过期时间采用把token二次保存在cookie或session里面，根据cookie和session的过期时间去维护token的过期时间

 
    开发过程举例：

    案例一：

     项目中我们的用户数据可能需要和第三方共享,或允许第三方调用我们的API则用token

    案例二:

     公司内部的网站，自己的App，就可以用cookie、session

    一般来说我们可以将登录信息放在session，其他信息保存在cookie

    案例三：

     观察微信、支付宝登录接口用的就是token
     

 ## 5、首先，什么是接口呢？

   - 接口一般来说有两种，一种是程序内部的接口，一种是系统对外的接口。
   
   - 系统对外的接口：比如你要从别的网站或服务器上获取资源或信息，别人肯定不会把数据库共享给你，他只能给你提供一个他们写好的方法来获取数据，你引用他提供的接口就能使用他写好的方法，从而达到数据共享的目的，比如说咱们用的app、网址这些它在进行数据处理的时候都是通过接口来进行调用的。
   
   - 程序内部的接口：方法与方法之间，模块与模块之间的交互，程序内部抛出的接口，比如bbs系统，有登录模块、发帖模块等等，那你要发帖就必须先登录，要发帖就得登录，那么这两个模块就得有交互，它就会抛出一个接口，供内部系统进行调用。

    一、常见接口：

    1、webService接口：是走soap协议通过http传输，请求报文和返回报文都是xml格式的，我们在测试的时候都用通过工具才能进行调用，测试。可以使用的工具有SoapUI、jmeter、loadrunner等；

    2、http api接口：是走http协议，通过路径来区分调用的方法，请求报文都是key-value形式的，返回报文一般都是json串，有get和post等方法，这也是最常用的两种请求方式。可以使用的工具有postman、RESTClient、jmeter、loadrunner等；

    二、前端和后端：

    在说接口测试之前，我们先来搞清楚这两个概念，前端和后端。
      前端是什么呢，对于web端来说，咱们使用的网页，打开的网站，这都是前端，这些都是html、css写的；对于app端来说呢，它就是咱们用的app，android或者object-C（开发ios上的app）开发的，它的作用就是显示页面，让我们看到漂亮的页面，以及做一些简单的校验，比如说非空校验，咱们在页面上操作的时候，这些业务逻辑、功能，比如说你购物，发微博这些功能是由后端来实现的，后端去控制你购物的时候扣你的余额，发微博发到哪个账号下面，那前端和后端是怎么交互的呢，就是通过接口。
      前面说的你可能不好理解，你只需记住：前端负责貌美如花，后端负责挣钱养家。

    三、什么是接口测试：

    接口测试是测试系统组件间接口的一种测试。接口测试主要用于检测外部系统与系统之间以及内部各个子系统之间的交互点。测试的重点是要检查数据的交换，传递和控制管理过程，以及系统间的相互逻辑依赖关系等。

    OK，上面是百度百科上说的，下面才是我说的

    其实我觉得接口测试很简单，比一般的功能测试还简单（这话我先这样说，以后可能会删O(∩_∩)O哈！），现在找工作好多公司都要求有接口测试经验，也有好多人问我（也就两三个人）什么是接口测试，本着不懂也要装懂的态度，我会说：所谓接口测试就是通过测试不同情况下的入参与之相应的出参信息来判断接口是否符合或满足相应的功能性、安全性要求。

    我为啥说接口测试比功能测试简单呢，因为功能测试是从页面输入值，然后通过点击按钮或链接等传值给后端，而且功能测试还要测UI、前端交互等功能，但接口测试没有页面，它是通过接口规范文档上的调用地址、请求参数，拼接报文，然后发送请求，检查返回结果，所以它只需测入参和出参就行了，相对来说简单了不少。

    四、接口组成

    接口都有那些部分组成呢？

    首先，接口文档应该包含以下内容：

    1、接口说明
    2、调用url
    3、请求方法（get\post）
    4、请求参数、参数类型、请求参数说明
    5、返回参数说明

    由接口文档可知，接口至少应有请求地址、请求方法、请求参数（入参和出参）组成，部分接口有请求头header。
    
    标头 (header)：是服务器以HTTP协议传HTML资料到浏览器前所送出的字串，在标头与 HTML 文件之间尚需空一行分隔，一般存放cookie、token等信息
    
    有同学问我header和入参有什么关系？它们不都是发送到服务器的参数吗？
    
    OK，首先，它们确实都是发送到服务器里的参数，但它们是有区别的，header里存放的参数一般存放的是一些校验信息，比如cookie，它是为了校验这个请求是否有权限请求服务器，如果有，它才能请求服务器，然后把请求地址连同入参一起发送到服务器，然后服务器会根据地址和入参来返回出参。也就是说，服务器是先接受header信息进行判断该请求是否有权限请求，判断有权限后，才会接受请求地址和入参的。
    
    五、为什么要做接口测试：
    
    大家都知道，接口其实就是前端页面或APP等调用与后端做交互用的，所以好多人都会问，我功能测试都测好了，为什么还要测接口呢？OK，在回答这个问题之前，先举个栗子：
    
    比如测试用户注册功能，规定用户名为6~18个字符，包含字母（区分大小写）、数字、下划线。首先功能测试时肯定会对用户名规则进行测试时，比如输入20个字符、输入特殊字符等，但这些可能只是在前端做了校验，后端可能没做校验，如果有人通过抓包绕过前端校验直接发送到后端怎么办呢？试想一下，如果用户名和密码未在后端做校验，而有人又绕过前端校验的话，那用户名和密码不就可以随便输了吗？如果是登录可能会通过SQL注入等手段来随意登录，甚至可以获取管理员权限，那这样不是很恐怖？
    
    所以，接口测试的必要性就体现出来了：
    
    ①、可以发现很多在页面上操作发现不了的bug
    
    ②、检查系统的异常处理能力
    
    ③、检查系统的安全性、稳定性
    
    ④、前端随便变，接口测好了，后端不用变
    
    六、接口测试怎么测：
    
    在进行接口测试前，还需要了解：
    
    1）、GET和POST请求：
        如果是get请求的话，直接在浏览器里输入就行了，只要在浏览器里面直接能请求到的，都是get请求，如果是post的请求的话，就不行了，就得借助工具来发送。
    GET请求和POST请求的区别：
        1、GET使用URL或Cookie传参。而POST将数据放在BODY中。
        2、GET的URL会有长度上的限制，则POST的数据则可以非常大。
        3、POST比GET安全，因为数据在地址栏上不可见。
        4、一般get请求用来获取数据，post请求用来发送数据。
    其实上面这几点，只有最后一点说的是比较靠谱的，第一点post请求也可以把数据放到url里面，get请求其实也没长度限制，post请求看起来参数是隐式的，稍微安全那么一些些，但是那只是对于小白用户来说的，就算post请求，你通过抓包也是可以抓到参数的。所以上面这些面试的时候你说出来就行了。
    
    2）、http状态码
    
    每发出一个http请求之后，都会有一个响应，http本身会有一个状态码，来标示这个请求是否成功，常见的状态码有以下几种：
    1、200 2开头的都表示这个请求发送成功，最常见的就是200，就代表这个请求是ok的，服务器也返回了。
    2、300 3开头的代表重定向，最常见的是302，把这个请求重定向到别的地方了，
    3、400 400代表客户端发送的请求有语法错误，401代表访问的页面没有授权，403表示没有权限访问这个页面，404代表没有这个页面
    4、500 5开头的代表服务器有异常，500代表服务器内部异常，504代表服务器端超时，没返回结果
    
    接下来再说接口测试怎么测：
    
    1）、通用接口用例设计
    
    ①、通过性验证：首先肯定要保证这个接口功能是好使的，也就是正常的通过性测试，按照接口文档上的参数，正常传入，是否可以返回正确的结果。
    ②、参数组合：现在有一个操作商品的接口，有个字段type，传1的时候代表修改商品，商品id、商品名称、价格有一个是必传的，type传2的时候是删除商品，商品id　　是必传的，这样的，就要测参数组合了，type传1的时候，只传商品名称能不能修改成功，id、名称、价格都传的时候能不能修改成功。
    
    ③、接口安全：
         1、绕过验证，比如说购买了一个商品，它的价格是300元，那我在提交订单时候，我把这个商品的价格改成3元，后端有没有做验证，更狠点，我把钱改成-3，是不是我的余额还要增加？
         2、绕过身份授权，比如说修改商品信息接口，那必须得是卖家才能修改，那我传一个普通用户，能不能修改成功，我传一个其他的卖家能不能修改成功
         3、参数是否加密，比如说我登陆的接口，用户名和密码是不是加密，如果不加密的话，别人拦截到你的请求，就能获取到你的信息了，加密规则是否容易破解。
         4、密码安全规则，密码的复杂程度校验
    
    ④、异常验证：
    　　所谓异常验证，也就是我不按照你接口文档上的要求输入参数，来验证接口对异常情况的校验。比如说必填的参数不填，输入整数类型的，传入字符串类型，长度是10的，传11，总之就是你说怎么来，我就不怎么来，其实也就这三种，必传非必传、参数类型、入参长度。
    
    2）、根据业务逻辑来设计用例
    　　根据业务逻辑来设计的话，就是根据自己系统的业务来设计用例，这个每个公司的业务不一样，就得具体的看自己公司的业务了，其实这也和功能测试设计用例是一样的。
        　　举个例子，拿bbs来说，bbs的需求是这样的：
      　　  1、登录失败5次，就需要等待15分钟之后再登录
      　　  2、新注册的用户需要过了实习期才能发帖
       　　 3、删除帖子扣除积分
       　　 4、......
       　　像这样的你就要把这些测试点列出来，然后再去造数据测试对应的测试点。
    
     七、用什么工具测
    



# 三、数据库

   1、左连接、右连接和全连接

     左连接：左边有的，右边没有的为null

     右连接：左边没有的，右边有的为null

     内连接：显示左边右边共有的

  2、数据库中sum和count的区别以及使用

    一般面试会把sum与order by 分组一起使用

    count:统计你查询出来的数据记录条数  ：select count(*) from 学生表；

    sum:求和     ：select sum(chengji) from 学生表 where name='张三'；

 



 
 
 
# 四、工具类
   - 接口测试的工具很多，比如 postman、RESTClient、jmeter、loadrunner、SoapUI等，本人首推的测试工具是postman和jmeter，接下来就简单介绍下如何使用这两款工具进行接口测试，其他工具本次暂不介绍。
    
    1）、Postman是谷歌的一款接口测试插件，它使用简单，支持用例管理，支持get、post、文件上传、响应验证、变量管理、环境参数管理等功能，可以批量运行，并支持用例导出、导入。
    
    jmeter是一款100%纯Java编写的免费开源的工具，它主要用来做性能测试，相比loadrunner来说，它内存占用小，免费开源，轻巧方便、无需安装，越来越被大众所喜爱。
    
    注：以下用例中所用地址皆为本人在本地所搭的环境，外网无法访问，见谅。

  1、POSTMAN
  2、
  3、
  4、jmeter中跟踪重定向和自动重定向区别？

    1）跟踪重定向通俗的理解就是跟踪请求执行的过程，并记录一些信息给开发者看到，我们一般可以在结果日志和监控中看到

    2）自动重定向是不用跟踪请求执行过程，也不用记录

 ## LoadRunner分为哪三个模块？请简述各模块的主要功能。
　　Virtual User Generator：用于录制脚步  
　　Mercury LoadRunner Controller：用于创建、运行和监控场景  
　　Mercury LoadRunner Analysis：用于分析测试结果  


# 五、Linux & Docker
Linux [菜鸟教程](https://www.runoob.com/w3cnote/linux-common-command-2.html)

 ## 1、ls 查看目录文件  
  - ls -a  列出目录所有文件，包含以.开始的隐藏文件   
  - ls -A  列出除.及..的其它文   
  - ls -r  反序排列   
  - ls -t  以文件修改时间排序   
  - ls -S  以文件大小排序   
  - ls -h  以易读大小显示   
  - ls -l  除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来  

 ## 2、cd 切换
  - cd /  进入要目录
  - cd ~  进入"家"目录
  - cd -  进入上一次工作路径
  - cd !$  把上个命令的参数作为cd参数使用。

 ## 3、pwd 查看当前工作目录路径
  - pwd  查看当前路径
  - pwd -P  查看软链接的实际路径

 ## 4、mkdir 创建文件夹
  - mkdir t  当前工作目录下创建名为t的文件夹
  - mkdir -p /tmp/test/t1/t  在tmp目录下创建路径为test/t1/t的目录，若不存在，则创建 

 ## 5、rm 删除文件
  - rm -i *.log  删除任何.log文件；删除前逐一询问确认
  - rm -rf test  删除test子目录及子目录中所有档案删除,并且不用一一确认 
  - rm -- -f*  删除以-f开头的文件

 ## 6、rmdir 删除空目录
  - rmdir -p parent/child/child11  当parent子目录被删除后使它也成为空目录的话，则顺便一并删除

 ## 7、mv　移动/修改文件名
  - mv test.log test1.txt  将文件test.log重命名为test1.txt
  - mv llog1.txt log2.txt log3.txt /test3  将文件log1.txt,log2.txt,log3.txt移动到根的test3目录中
  - mv -i log1.txt log2.txt  将文件file1改名为file2，如果file2已经存在，则询问是否覆盖
  - mv * ../  移动当前文件夹下的所有文件到上一级目录

 ## 8、cp　复制  
  - -i  提示
  - -r  复制目录及目录内所有项目  
  - -a  复制的文件与原文件时间一样 
  - cp -ai a.txt test  复制a.txt到test目录下，保持原文件时间,如果原文件存在提示是否覆盖  
  - cp -s a.txt link_a.txt  为a.txt建议一个链接（快捷方式）  

 ## 9、cat 显示文件详情
  ### 1、cat主要有三大功能：
   - ​cat filename 一次显示整个文件
   - cat > filename 从键盘创建一个文件，只能创建新文件,不能编辑已有文件.
   - cat file1 file2 > file 将几个文件合并为一个文件
  
  - -b对非空输出行号
  - -n输出所有行号
  - ​cat -n log2012.log log2013.log 把log2012.log的文件内容加上行号后输入 log2013.log 这个文件里
  - cat -b log2012.log log2013.log log.log 把log2012.log和log2013.log的文件内容加上行号（空白行不加）之后将内容附加到 log.log 里
  - cat >log.txt <<EOF 使用here doc生成新文件

 ## 10、more　分页显示
  - 功能类似于cat, more会以一页一页的显示方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示  - 
​  
  - 命令参数：
  - +n 从笫n行开始显示
  - -n 定义屏幕大小为n行
  - +/pattern 在每个档案显示前搜寻该字串（pattern），然后从该字串前两行之后开始显示
  - -c 从顶部清屏，然后显示
  - -d 提示“Press space to continue，’q’ to quit（按空格键继续，按q键退出）”，禁用响铃功能
  - -l 忽略Ctrl+l（换页）字符
  - -p 通过清除窗口而不是滚屏来对文件进行换页，与-c选项相似
  - -s 把连续的多个空行显示为一行
  - -u 把文件内容中的下画线去掉

  - 常用操作命令：
  
  - Enter 向下n行，需要定义。默认为1行
  - Ctrl+F 向下滚动一屏
  - 空格键 向下滚动一屏
  - Ctrl+B 返回上一屏
  - = 输出当前行的行号
  - ：f 输出文件名和当前行的行号

  - V 调用vi编辑器
  - !命令 调用Shell，并执行命令
  - q 退出more

  - 实例：
  - more +3 text.txt 显示文件中从第3行起的内容
  - ls -l | more -5 在所列出文件目录详细信息，借助管道使每次显示5行


 ## 11、less命令
  - less 与 more 类似，但使用 less 可以随意浏览文件，而 more 仅能向前移动，却不能向后移动，而且 less 在查看之前不会加载整个文件。

  - 常用命令参数
  - -i 忽略搜索时的大小写
  - -N 显示每行的行号
  - -o <文件名> 将less 输出的内容在指定文件中保存起来
  - -s 显示连续空行为一行
  - /字符串：向下搜索“字符串”的功能
  - ?字符串：向上搜索“字符串”的功能
  - n：重复前一个搜索（与 / 或 ? 有关）
  - N：反向重复前一个搜索（与 / 或 ? 有关）

  - -x <数字> 将“tab”键显示为规定的数字空格
  - b 向后翻一页
  - d 向后翻半页
  - h 显示帮助界面
  - Q 退出less 命令
  - u 向前滚动半页
  - y 向前滚动一行
  - 空格键 滚动一行
  - 回车键 滚动一页

  - [pagedown]： 向下翻动一页
  - [pageup]： 向上翻动一页

  - 实例：
  - （1）ps查看进程信息并通过less分页显示
  - ps -aux | less -N
  
  - （2）查看多个文件
  - less 1.log 2.log
  - 可以使用n查看下一个，使用p查看前一个

 ## 12、head　从头ｎ行文本内容
  - 用于显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。

  - 常用参数：
  - -f 循环读取（常用于查看递增的日志文件）
  - -n<行数> 显示行数（从后向前）
  
  - （1）循环读取逐渐增加的文件内容
  - ping 127.0.0.1 > ping.log &（后台运行：可使用jobs -l查看，也可使用fg将其移到前台运行）
  - tail -f ping.log（查看日志）

 ## 13、tail　从尾ｎ行文本
  - 用于显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。

  - 常用参数：
  - -f 循环读取（常用于查看递增的日志文件）
  - -n<行数> 显示行数（从后向前）
  
  - （1）循环读取逐渐增加的文件内容
  - ping 127.0.0.1 > ping.log &（后台运行：可使用jobs -l查看，也可使用fg将其移到前台运行）
  - tail -f ping.log（查看日志）

 ## 14、which　查看可执行文件的位置
  - 在linux要查找某个文件，但不知道放在哪里了，可以使用下面的一些命令来搜索：
  - ​which 查看可执行文件的位置。
  - ​whereis 查看文件的位置。
  - ​locate 配合数据库查看文件位置。
  - ​find 实际搜寻硬盘查询文件名称。
  - ​which是在PATH就是指定的路径中，搜索某个系统命令的位置，并返回第一个搜索结果。使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令。

  - 常用参数：

  - -n 　指定文件名长度，指定的长度必须大于或等于所有文件中最长的文件名。

  - 实例：

​  - which ls 查看ls命令是否存在，执行哪个
  - ​which which 查看which
​  - which cd（显示不存在，因为cd是内建命令，而which查找显示是PATH中的命令） 查看cd

  - 查看当前PATH配置：echo $PATH；或使用env查看所有环境变量及对应值

 ## 15、locate命令
  - locate通过搜寻系统内建文档数据库达到快速找到档案，数据库由updatedb程序来更新，updatedb是由cron daemon周期性调用的。默认情况下locate命令在搜寻数据库时比由整个由硬盘资料来搜寻资料来得快，但较差劲的是locate所找到的档案若是最近才建立或 刚更名的，可能会找不到，在内定值中，updatedb每天会跑一次，可以由修改crontab来更新设定值。(etc/crontab)。
  - ​locate与find命令相似，可以使用如*、?等进行正则匹配查找

  ### 常用参数：
  - ​-l num（要显示的行数）
  - -f 将特定的档案系统排除在外，如将proc排除在外
  - -r 使用正则运算式做为寻找条件
  - ​locate pwd 查找和pwd相关的所有文件(文件名中包含pwd）
  - ​locate /etc/sh 搜索etc目录下所有以sh开头的文件
  - locate -r '^/var.reason$'（其中.表示一个字符，表示任务多个；.*表示任意多个字符） 查找/var目录下，以reason结尾的文件

 ## 16、find　文件树中查找文件

  - find -atime -2 查找48小时内修改过的文件
  - find ./ -name '*.log' 在当前目录查找 以.log结尾的文件。 ". "代表当前目录
  - find /opt -perm 777 查找/opt目录下 权限为 777的文件
  - find -size +1000c 查找大于1K的文件
  - find -size 1000c 查找等于1000字符的文件
  - -exec 参数后面跟的是command命令，它的终止是以;为结束标志的，所以这句命令后面的分号是不可缺少的，考虑到各个系统中分号会有不同的意义，所以前面加反斜杠。{} 花括号代表前面find查找出来的文件名。
  - find . -type f -mtime +10 -exec rm -f {} ; 在当前目录中查找更改时间在10日以前的文件并删除它们(无提醒）
  - find . -name '*.log' mtime +5 -ok -exec rm {} ; 当前目录中查找所有文件名以.log结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。 按y键删除文件，按n键不删除
  - find . -f -name 'passwd*' -exec grep "pkg" {} ; 当前目录下查找文件名以passwd开头，内容包含"pkg"字符的文件
  -  find . -name '*.log' -exec cp {} test3 ; 用exec选项执行cp命令

  - -xargs find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。

  - 实例：

  - （9）查找当前目录下每个普通文件，然后使用xargs来判断文件类型
  - find . -type f -print | xargs file

  - （10）查找当前目录下所有以js结尾的并且其中包含'editor'字符的普通文件
  - find . -type f -name "*.js" -exec grep -lF 'ueditor' {} ;
  - find -type f -name '*.js' | xargs grep -lF 'editor'

  - （11）利用xargs执行mv命令
  - find . -name "*.log" | xargs -i mv {} test4

  - （12）用grep命令在当前目录下的所有普通文件中搜索hostnames这个词,并标出所在行
  - find . -name *(转义） -type f -print | xargs grep -n 'hostnames'
  
  - （13）查找当前目录中以一个小写字母开头，最后是4到9加上.log结束的文件
  - find . -name '[a-z]*[4-9].log' -print
  
  - （14）在test目录查找不在test4子目录查找
  - find test -path 'test/test4' -prune -o -print
  
  - （15）实例1：查找更改时间比文件log2012.log新但比文件log2017.log旧的文件
  -  find -newer log2012.log ! -newer log2017.log
  - 使用depth选项：
  - depth选项可以使find命令向磁带上备份文件系统时，希望首先备份所有的文件，其次再备份子目录中的文件。
  -  实例：find命令从文件系统的根目录开始，查找一个名为CON.FILE的文件。 它将首先匹配所有的文件然后再进入子目录中查找
  - find / -name "CON.FILE" -depth -print

 ## 17、grep　文本搜索命令
  - 强大的文本搜索命令，grep(Global Regular Expression Print)全局正则表达式搜索

  - grep的工作方式是这样的，它在一个或多个文件中搜索字符串模板。如果模板包括空格，则必须被引用，模板后的所有字符串被看作文件名。搜索的结果被送到标准输出，不影响原文件内容。

  - 命令格式：
  - grep [option] pattern file|dir
  
  - 常用参数：

  - -A n --after-context显示匹配字符后n行
  - -B n --before-context显示匹配字符前n行
  - -C n --context 显示匹配字符前后n行
  - -c --count 计算符合样式的列数
  - -i 忽略大小写
  - -l 只列出文件内容符合指定的样式的文件名称
  - -f 从文件中读取关键词
  - -n 显示匹配内容的所在文件中行数
  - -R 递归查找文件夹
  - grep的规则表达式:

  - ^ #锚定行的开始 如：'^grep'匹配所有以grep开头的行。
  - $ #锚定行的结束 如：'grep$'匹配所有以grep结尾的行。
  - . #匹配一个非换行符的字符 如：'gr.p'匹配gr后接一个任意字符，然后是p。
  - * #匹配零个或多个先前字符 如：'*grep'匹配所有一个或多个空格后紧跟grep的行。

  - .* #一起用代表任意字符。
  - [] #匹配一个指定范围内的字符，如'[Gg]rep'匹配Grep和grep。
  - [^] #匹配一个不在指定范围内的字符，如：'[^A-FH-Z]rep'匹配不包含A-R和T-Z的一个字母开头，紧跟rep的行。
  - (..) #标记匹配字符，如'(love)'，love被标记为1。
  - < #锚定单词的开始，如:'<grep'匹配包含以grep开头的单词的行。
  - > #锚定单词的结束，如'grep>'匹配包含以grep结尾的单词的行。
  - x{m} #重复字符x，m次，如：'0{5}'匹配包含5个o的行。
  - x{m,} #重复字符x,至少m次，如：'o{5,}'匹配至少有5个o的行。
  - x{m,n} #重复字符x，至少m次，不多于n次，如：'o{5,10}'匹配5--10个o的行。
  - \w #匹配文字和数字字符，也就是[A-Za-z0-9]，如：'G\w*p'匹配以G后跟零个或多个文字或数字字符，然后是p。
  - \W #\w的反置形式，匹配一个或多个非单词字符，如点号句号等。
  - \b #单词锁定符，如: '\bgrep\b'只匹配grep。

  - 实例：

  - （1）查找指定进程
  - ps -ef | grep svn

  - （2）查找指定进程个数
  - ps -ef | grep svn -c

  - （3）从文件中读取关键词
  - cat test1.txt | grep -f key.log

  - （4）从文件夹中递归查找以grep开头的行，并只列出文件
  - grep -lR '^grep' /tmp

  - （5）查找非x开关的行内容
  - grep '[x]' test.txt

  - （6）显示包含ed或者at字符的内容行
  - grep -E 'ed|at' test.txt

 ## 18、chmod　访问权限
  - 常用参数：
  - -c 当发生改变时，报告处理信息
  - -R 处理指定目录以及其子目录下所有文件
  
  - 权限范围：
  - u ：目录或者文件的当前的用户
  - g ：目录或者文件的当前的群组
  - o ：除了目录或者文件的当前用户或群组之外的用户或者群组
  - a ：所有的用户及群组

  - 权限代号：
  - r ：读权限，用数字4表示
  - w ：写权限，用数字2表示
  - x ：执行权限，用数字1表示  
  - \- ：删除权限，用数字0表示
  - s ：特殊权限

  - 实例：
  - （1）增加文件t.log所有用户可执行权限
  - chmod a+x t.log

  - （2）撤销原来所有的权限，然后使拥有者具有可读权限,并输出处理信息
  - chmod u=r t.log -c

  - （3）给file的属主分配读、写、执行(7)的权限，给file的所在组分配读、执行(5)的权限，给其他用户分配执行(1)的权限
  - chmod 751 t.log -c（或者：chmod u=rwx,g=rx,o=x t.log -c)

  - （4）将test目录及其子目录所有文件添加可读权限
  - chmod u+r,g+r,o+r -R text/ -c

 ## 19、chown　改为指定的用户或组
  - -c 显示更改的部分的信息
  - -R 处理指定目录及子目录
  
  - hown -c mail:mail log2012.log 改变拥有者和群组 并显示改变信息
  - chown -c :mail t.log 改变文件群组
  - chown -cR mail: test/ 改变文件夹及子文件目录属主及属组为mail

 ## 20、df　显示磁盘空间
  - 显示磁盘空间使用情况。获取硬盘被占用了多少空间，目前还剩下多少空间等信息，如果没有文件名被指定，则所有当前被挂载的文件系统的可用空间将被显示。默认情况下，磁盘空间将以 1KB 为单位进行显示，除非环境变量 POSIXLY_CORRECT 被指定，那样将以512字节为单位进行显示
  - -a 全部文件系统列表
  - -h 以方便阅读的方式显示信息
  - -i 显示inode信息
  - -k 区块为1024字节
  - -l 只显示本地磁盘
  - -T 列出文件系统类型

  - 实例：

  - （1）显示磁盘使用情况
  - df -l

  - （2）以易读方式列出所有文件系统及其类型
  - df -haT

 ## 21、date　显示时间
  - 显示或设定系统的日期与时间

  - 命令参数：
  - -d<字符串> 　显示字符串所指的日期与时间。字符串前后必须加上双引号。
  - -s<字符串> 　根据字符串来设置日期与时间。字符串前后必须加上双引号。
  - -u 　显示GMT。

  - %H 小时(00-23)
  - %I 小时(00-12)
  - %M 分钟(以00-59来表示)
  - %s 总秒数。起算时间为1970-01-01 00:00:00 UTC。
  - %S 秒(以本地的惯用法来表示)
  - %a 星期的缩写。
  - %A 星期的完整名称。
  - %d 日期(以01-31来表示)。
  - %D 日期(含年月日)。
  - %m 月份(以01-12来表示)。
  - %y 年份(以00-99来表示)。
  - %Y 年份(以四位数来表示)。

  - 实例：

  - （1）显示下一天

  - date +%Y%m%d --date="+1 day" //显示下一天的日期

  - （2）-d参数使用

  - date -d "nov 22" 今年的 11 月 22 日是星期三
  - date -d '2 weeks' 2周后的日期
  - date -d 'next monday' (下周一的日期)
  - date -d next-day +%Y%m%d（明天的日期）或者：date -d tomorrow +%Y%m%d
  - date -d last-day +%Y%m%d(昨天的日期) 或者：date -d yesterday +%Y%m%d
  - date -d last-month +%Y%m(上个月是几月)
  - date -d next-month +%Y%m(下个月是几月)

 ## 22、ps　查看进程
  - ps -ef 显示当前所有进程环境变量及进程间关系
  - ps -A 显示当前所有进程
  - ps -aux | grep apache 与grep联用查找某进程
  - s aux | grep '(cron|syslog)' 找出与 cron 与 syslog 这两个服务有关的 PID 号码


 ## 23、kill　杀死进程
  - kill -9 $(ps -ef | grep pro1) 先使用ps查找进程pro1，然后用kill杀掉

 ## 24、free　显示内存使用情况
  ### 1.显示内存使用情况
   - free
   - free -k
   - free -m

  ### 2.以总和的形式显示内存的使用信息
   - free -t

  ### 3.周期性查询内存使用情况
   - free -s 10

 ## 25、VI 和vim 编辑文本
  - vi filename :打开或新建文件,并将光标置于第一行首
  - vi n filename ：打开文件,并将光标置于第n行首
  - vi filename ：打开文件,并将光标置于一行首
  - vi /pattern filename：打开文件,并将光标置于第一个与pattern匹配的串处
  - vi -r filename ：在上次正用vi编辑时发生系统崩溃,恢复filename
  - vi filename....filename ：打开多个文件,依次进行编辑

  ### 1.屏幕翻滚类命令
  - Ctrl u：向文件首翻半屏
  - Ctrl d：向文件尾翻半屏
  - Ctrl f：向文件尾翻一屏
  - Ctrl＋b；向文件首翻一屏
  - nz：将第n行滚至屏幕顶部,不指定n时将当前行滚至屏幕顶部.

  ### 2.插入文本类命令
  - i ：在光标前
  - I ：在当前行首
  - a：光标后
  - A：在当前行尾
  - o：在当前行之下新开一行
  - O：在当前行之上新开一行
  - r：替换当前字符
  - R：替换当前字符及其后的字符,直至按ESC键
  - s：从前光标位置处开始,以输入的文本替代指定数目的字符

​
  ### 3.保存命令

  - 按ESC键 跳到命令模式，然后：
  - :w 保存文件但不退出vi
  - :w file 将修改另外保存到file中，不退出vi
  - :w! 强制保存，不推出vi
  - :wq 保存文件并退出vi
  - :wq! 强制保存文件，并退出vi
  - :q 不保存文件，退出vi
  - :q! 不保存文件，强制退出vi
  - :e! 放弃所有修改，从上次保存文件开始再编辑

 ## 26、echo指令向文件写入内容
  - 1.覆盖文件内容  
    echo "Raspberry" > test.txt  使用>指令覆盖文件原内容并重新输入内容，若文件不存在则创建文件。

  - 2.追加文件内容
    【示例脚本】test.sh  
    使用>>指令向文件追加内容，原内容将保存。  



# 六、自动化
  12、自动化测试selenium 显式等待和隐式等待

    显式等待就是有条件的等待
    隐式等待就是无条件的等待
    显式等待：

    # 设置等待时间
      WebDriverWait(driver, 3, 0.5) #传入三个参数，第一个是浏览器驱动，第二个是等待多少秒，第三个是每隔多少秒监控一次
      原理：指定一个等待条件，和一个最长等待时间，程序会判断在等待时间内条件是否满足，如果满足则返回，如果不满足会继续等待，超过时间就会抛出异常
     隐式等待：

      browser.implicitly_wait(10) #直接等待10秒钟
      当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
   13、pytest如何管理测试用例？

    1）掌握案例规则，如以test_开头，类以Test命名等

    2）案例文件执行单个py如何执行，多个文件夹的管理方式


                     


# 七、python

    1、装饰器介绍
    装饰器也是一个函数，它是让其他函数在不改变变动的前提下增加额外的功能。
    装饰器是一个闭包，把一个函数当作参数返回一个替代版的函数，本质是一个返回函数的函数（即返回值为函数对象）。
    python3支持用@符号直接将装饰器应用到函数。
    装饰器工作场景：插入日志、性能测试、事务处理等等。
    函数被装饰器装饰过后，此函数的属性均已发生变化，如名称变为装饰器的名称。

    2、生成器
    
    3、统计字符串中每个字符出现的次数
        a = "a;lskdh!`foiegn``as;ldnf,asd.121,2ljladsfkja`sdijfhaosjlfd,gjsdfg.as.dl"
       1) 使用方法库
     
          from collections import Counter
          b = Counter(a)
          print(b)
          # {'a': 7, ';': 2, 'l': 6, 's': 8, 'k': 2, 'd': 8, 'h': 2, '!': 1, '`': 4, 'f': 6, 'o': 2, 'i': 2, 'e': 1, 'g': 3, 'n': 2, ',': 3, '.': 3, '1': 2, '2': 2, 'j': 5}
       2) 使用字典处理
     
          dict_ = {}
          for i in a:
            if i in dict_:
              dict_[i] += 1
            else:
              dict_[i] = 1
          print(dict_)
          # {'a': 7, ';': 2, 'l': 6, 's': 8, 'k': 2, 'd': 8, 'h': 2, '!': 1, '`': 4, 'f': 6, 'o': 2, 'i': 2, 'e': 1, 'g': 3, 'n': 2, ',': 3, '.': 3, '1': 2, '2': 2, 'j': 5}
          
          
          
# 八、Jenkins
##


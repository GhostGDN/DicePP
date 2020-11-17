from .info_game import MENU_CUISINE_LIST, MENU_TYPE_LIST, MENU_STYLE_LIST, MENU_KEYWORD_LIST
from .info_game import PC_SKILL_DICT, PC_SHEET_TEMPLATE
from .utils import Str2CommandTypeDict
VERSION = '0.7.1'

HELP_STR = f'Dice++ by 梨子 Ver {VERSION}\n'
HELP_STR += '@骰娘 .bot on/off 开启或关闭骰娘\n'
HELP_STR += '.help指令 查看指令列表\n'
HELP_STR += '.help链接 查看源码地址\n'
HELP_STR += '.help协议 查看使用协议\n'
HELP_STR += '.help更新 查看最近更新内容\n'
HELP_STR += '伊丽莎白是D&D5E专用骰娘, 熟练掌握的技能包括:优劣势投骰, 查询和抽卡功能, 记录角色卡(生命值, 属性, 法术环位, 金钱), 实用先攻列表等\n'
HELP_STR += '欢迎加入交流群:861919492或联系开发者:821480843报告bug和提出意见~'

SHOW_STR = f'Dice++ by 梨子 Ver {VERSION} @骰娘 .bot on/off 开启或关闭骰娘\n'
SHOW_STR += '输入.help更新 查看最近更新内容\n'
SHOW_STR += '伊丽莎白是D&D5E专用骰娘, 熟练掌握的技能包括:优劣势投骰, 查询和抽卡功能, 记录角色卡(生命值, 属性, 法术环位, 金钱), 实用先攻列表等\n'
SHOW_STR += '欢迎加入交流群:861919492或联系开发者:821480843报告bug和提出意见~'

FIRST_TIME_STR = '伊丽莎白来咯~\n我是D&D5E专用骰娘, 请不要把我拉进无关的群哦~\n输入.help查看使用帮助\n请不要禁言和踢骰娘, 暂时不需要我的话就at我以后再加上.bot off或.dismiss吧~'
LEAVE_WARNING_STR = '不需要我的话, 我就去其他地方玩咯~\n#收拾东西准备离开'
LEAVE_NOTICE_STR = '一只人鱼趁着夜色离开了你的队伍。'

HELP_COMMAND_UPDATE_STR = '2020/11/17 v0.7.1:\n1.增加了群管理功能, 包括启用/禁用特定功能, 统计群成员信息, 请输入.help群管理查看\n'
HELP_COMMAND_UPDATE_STR += '2020/11/6 v0.7.0:\n1.改动代码结构并且增加搭建说明, 开放私骰的搭建 2.修复了更新时无法正确处理过期用户的问题\n'
HELP_COMMAND_UPDATE_STR += '2020/11/1 v0.6.4:\n1.更改了好感度设定 2.修复了若干文本问题\n'
HELP_COMMAND_UPDATE_STR += '2020/5/5 v0.6.3:\n1.加入了答题功能 2.增加了更多的随机姓名 3.增加了更多的今日笑话\n'
HELP_COMMAND_UPDATE_STR += '2020/4/26 v0.6.2:\n1.实验性地于查询指令中加入了交互命令, 具体使用方法请输入.help交互 或 .help查询 查看\n'
HELP_COMMAND_UPDATE_STR += '2020/4/26 v0.6.1:\n1.加入了随机姓名指令\n'
HELP_COMMAND_UPDATE_STR += '2020/4/25 v0.6.0:\n1.大幅改动了代码结构, 增强了可拓展性 2.记录笔记可以递增记录了 3.修复了一些指令的bug 4.加入了一些聊天彩蛋\n'
HELP_COMMAND_UPDATE_STR += '2020/4/15 v0.5.9.2:\n1.增强了.ri和.init指令 2.加入了队伍检定和队伍金钱功能 3.可以在一个属性检定指令中重复投多次骰子了 4.投骰表达式的识别不会忽略空格了, 如.rd2 0将被识别为原因是0的2面骰\n'
HELP_COMMAND_UPDATE_STR += '2020/4/10 v0.5.9.1:\n1.强化了draw指令\n'
HELP_COMMAND_UPDATE_STR += '画饼中的功能请在交流群:861919492查看~'

HELP_COMMAND_STR = '主要指令包括:\n'
HELP_COMMAND_STR += '.bot 开关 @骰娘 \n'
HELP_COMMAND_STR += '.dismiss 使骰娘退群 @骰娘\n'
HELP_COMMAND_STR += '.r 掷骰\n'
HELP_COMMAND_STR += '.nn 设置昵称\n'
HELP_COMMAND_STR += '.ri 先攻\n'
HELP_COMMAND_STR += '.init 先攻列表\n'
HELP_COMMAND_STR += '.hp 记录/调整生命值\n'
HELP_COMMAND_STR += '.笔记 笔记系列功能\n, 请输入.help笔记查看具体说明'
HELP_COMMAND_STR += '.法术位 记录/调整法术位, 请输入.help法术位查看具体说明\n'
HELP_COMMAND_STR += '.金钱 记录/调整金钱, 请输入.help金钱查看具体说明\n'
HELP_COMMAND_STR += '.角色卡 录入角色卡等功能, 请输入.help角色卡查看具体说明\n'
HELP_COMMAND_STR += '.检定 自动检定功能, 请输入.help检定查看具体说明\n'
HELP_COMMAND_STR += '.队伍 主要用来快速查看队员属性, 请输入.help队伍查看具体说明\n'
HELP_COMMAND_STR += '.长休 回复生命值与法术环位\n'
HELP_COMMAND_STR += '.查询 查询资料\n'
HELP_COMMAND_STR += '.draw 抽取牌库\n'
HELP_COMMAND_STR += '.答题 回答提问\n'
HELP_COMMAND_STR += '.烹饪 进行随机的烹饪检定\n'
HELP_COMMAND_STR += '.点菜 模拟点菜\n'
HELP_COMMAND_STR += '.今日菜单\n'
HELP_COMMAND_STR += '.今日笑话 获取一个随机TRPG冷笑话吧~\n'
HELP_COMMAND_STR += '.dnd 初始属性作成\n'
HELP_COMMAND_STR += '.name 生成随机姓名\n'
HELP_COMMAND_STR += '.jrrp 今日人品\n'
HELP_COMMAND_STR += '.send 单方面向Master发送消息\n'
HELP_COMMAND_STR += '.welcome 自定义入群欢迎词\n'
HELP_COMMAND_STR += '骰娘会自动去掉大多数空格以及转换小写, 多数指令需要后接参数, 详细用法请输入.help [指令名]查询, 如.help hp'

HELP_LINK_STR = 'Dice++是基于Python, NoneBot和go-cqhttp的骰子机器人项目\n'
HELP_LINK_STR += '项目地址: https://github.com/haowen-li/DicePP'

HELP_IA_STR = '目前交互指令还处于测试中, 实装的功能包括: [查询]\n'
HELP_IA_STR += '交互指令对于每个群聊和私聊来说都是独立的, 即用户在群聊A中不会触发私聊或群聊B中的交互指令\n'
HELP_IA_STR += '交互指令有60秒钟的有效时间, 过期则不会回应\n'
HELP_IA_STR += '若要提前结束当前交互指令, 请输入q或Q~'

HELP_AGREEMENT_STR =  '0.本协议是Dice++的服务协议。\n'
HELP_AGREEMENT_STR += '1.邀请骰娘, 使用掷骰服务和在群内阅读此协议视为同意并承诺遵守此协议，否则请移除骰娘。\n'
HELP_AGREEMENT_STR += '2.不允许禁言骰娘或刷屏掷骰等对骰娘的不友善行为，这些行为将会提高骰娘被制裁的风险。开关骰娘响应请使用.bot on/off。\n'
HELP_AGREEMENT_STR += '3.骰娘默认邀请行为已事先得到群内同意，因而会自动同意群邀请。因擅自邀请而使骰娘遭遇不友善行为时，邀请者因未履行预见义务而将承担连带责任。\n'
HELP_AGREEMENT_STR += '4.禁止将骰娘用于赌博及其他违法犯罪行为。\n'
HELP_AGREEMENT_STR += '5.对于设置敏感昵称等无法预见但有可能招致言论审查的行为，骰娘可能会出于自我保护而拒绝提供服务\n'
HELP_AGREEMENT_STR += '6.由于技术以及资金原因，无法保证骰娘100%的时间稳定运行，可能不定时停机维护或遭遇冻结，敬请谅解。\n'
HELP_AGREEMENT_STR += '7.对于违反协议的行为，骰娘将视情况终止对用户和所在群提供服务。\n'
HELP_AGREEMENT_STR += '8.本协议内容随时有可能改动。请注意帮助信息。\n'
HELP_AGREEMENT_STR += '9.Dice++参考了Dice! by 溯洄 Shiki的部分文字和指令设定, 但没有借鉴或复制任何代码, 如有疑问请联系qq:821480843。\n'
HELP_AGREEMENT_STR += '10.本服务最终解释权归服务提供方所有。'

HELP_COMMAND_R_STR =  '掷骰：.r[掷骰表达式]([掷骰原因]) [掷骰表达式]：([轮数]#)[个数]d面数(优/劣势)(k[取点数最大的骰子数])不带面数时视为掷一个默认的20面骰\n'
HELP_COMMAND_R_STR += 'r后加h即为暗骰\n'
HELP_COMMAND_R_STR += '示例:\n'
HELP_COMMAND_R_STR += '.rd20+1d4+4\n'
HELP_COMMAND_R_STR += '.r4#d    //投4次d20\n'
HELP_COMMAND_R_STR += '.rd20劣势+4 //带劣势攻击\n'
HELP_COMMAND_R_STR += '.r2#d优势+4 攻击被束缚的地精 //两次有加值的优势攻击\n'
HELP_COMMAND_R_STR += '.r1d12+2d8+5抗性 //得到减半向下取整的投骰总值'

HELP_COMMAND_NN_STR =  '设置昵称：.nn [昵称]\n'
HELP_COMMAND_NN_STR += '私聊.nn视为操作全局昵称\n'
HELP_COMMAND_NN_STR += '昵称优先级:群昵称>私聊昵称>群名片>QQ昵称\n'
HELP_COMMAND_NN_STR += '群聊中的nn指令会智能修改先攻列表中的名字\n'
HELP_COMMAND_NN_STR += '示例:\n'
HELP_COMMAND_NN_STR += '.nn	//视为删除昵称\n'
HELP_COMMAND_NN_STR += '.nn dm //将昵称设置为dm'

HELP_COMMAND_COOK_STR =  '烹饪菜肴：.烹饪([优劣势][加值]) (用/分隔的关键词列表)\n'
HELP_COMMAND_COOK_STR += '强烈建议加上关键词'
HELP_COMMAND_COOK_STR += f'可用关键词为: \n菜系:{MENU_CUISINE_LIST}\n风格:{MENU_STYLE_LIST}\n种类:{MENU_TYPE_LIST}\n'
HELP_COMMAND_COOK_STR += '示例:\n'
HELP_COMMAND_COOK_STR += '.烹饪 //随机烹饪食物, 可能遇到黑暗料理\n'
HELP_COMMAND_COOK_STR += '.烹饪优势 野炊/主食 //以优势烹饪含有野炊与主食关键字的食物'

HELP_COMMAND_ORDER_STR =  '点菜：.点菜(数量) (用/分隔的关键词列表)\n'
HELP_COMMAND_ORDER_STR += '强烈建议加上关键词'
HELP_COMMAND_ORDER_STR += f'可用关键词为: \n菜系:{MENU_CUISINE_LIST}\n风格:{MENU_STYLE_LIST}\n种类:{MENU_TYPE_LIST}\n'
HELP_COMMAND_ORDER_STR += '示例:\n'
HELP_COMMAND_ORDER_STR += '.点菜 //随机点一道菜, 可能遇到黑暗料理\n'
HELP_COMMAND_ORDER_STR += '.点菜4 野炊/主食 //点4道含有野炊与主食关键字的食物'

HELP_COMMAND_RI_STR =  '加入先攻(群聊限定)：.ri([优劣势][加值]) ([名称][/(投骰表达式#)名称/...])\n'
HELP_COMMAND_RI_STR += '示例:\n'
HELP_COMMAND_RI_STR += '.ri优势+1 //以昵称加入先攻列表\n'
HELP_COMMAND_RI_STR += '.ri20 地精 //将地精以固定先攻20加入先攻列表\n'
HELP_COMMAND_RI_STR += '.ri+2 地精/灵活地精+1/笨拙地精-1 //将3个地精分别加入先攻列表\n'
HELP_COMMAND_RI_STR += '.ri-2 2#食人魔僵尸/1d4#兽人僵尸 //将2个食人魔僵尸(a,b)以相同的先攻加入先攻列表, 将1d4个兽人僵尸(a~d)以相同的先攻加入先攻列表'

HELP_COMMAND_INIT_STR =  '显示先攻列表：.init ([可选指令]) [可选指令]:clr 清空先攻列表 del 删除指定先攻条目\n'
HELP_COMMAND_INIT_STR += 'del指令支持部分匹配\nhp信息也会在先攻列表上显示\n'
HELP_COMMAND_INIT_STR += '示例:\n'
HELP_COMMAND_INIT_STR += '.init //查看先攻列表\n'
HELP_COMMAND_INIT_STR += '.init clr //清空先攻列表\n'
HELP_COMMAND_INIT_STR += '.init del 地精 //在先攻列表中删除地精'
HELP_COMMAND_INIT_STR += '.init del 地精a/地精b/地精c //在先攻列表中删除地精abc'

HELP_COMMAND_NAME_STR =  '生成随机姓名：.name (次数#)类型\n'
HELP_COMMAND_NAME_STR += '次数必须在1~10之间\n类型支持部分匹配\n'
HELP_COMMAND_NAME_STR += '示例:\n.name 3#男性精灵\n.name 女性兽人'

HELP_COMMAND_QUERY_STR =  '查询资料: .查询 查询目标\n'
HELP_COMMAND_QUERY_STR += '查询指令支持部分匹配, 可用/区分多个关键字\n'
HELP_COMMAND_QUERY_STR += '可以用索引指令查询词条名\n'
HELP_COMMAND_QUERY_STR += '目前可查询的内容有: 玩家手册(by梨子,花作噫,邪恶,赵小安,睡帽), 全拓展法术与专长, 怪物图鉴(by花作噫, 梨子), '
HELP_COMMAND_QUERY_STR += '城主指南部分规则(by梨子), 拓展职业(by惠惠, 梨子), 拓展种族(by梨子), 核心与拓展魔法物品(by花作噫, 惠惠), 眼魔书城主工具(by梨子)\n'
HELP_COMMAND_QUERY_STR += '查询指令加入了交互功能, 可以通过查询或索引后直接输入序号查询, 更具体的信息请输入.help交互查看\n'
HELP_COMMAND_QUERY_STR += '示例:\n'
HELP_COMMAND_QUERY_STR += '.查询 借机攻击\n'
HELP_COMMAND_QUERY_STR += '.查询 长弓\n'
HELP_COMMAND_QUERY_STR += '.查询 法师/6环\n'
HELP_COMMAND_QUERY_STR += '.索引 长弓 // 返回所有含有长弓的词条(如物品, 怪物, 魔法物品, 能力)\n'
HELP_COMMAND_QUERY_STR += '.索引 昏迷/施法时间 //利用法术词条中必然含有施法时间的特性查询和昏迷相关的法术'

HELP_COMMAND_DRAW_STR =  '抽取牌库: .draw [抽取次数#]目标牌库\n'
HELP_COMMAND_DRAW_STR += '目标牌库支持部分匹配, 可用/区分多个关键字\n'
HELP_COMMAND_DRAW_STR += '查看支持的牌库请输入.draw\n'
HELP_COMMAND_DRAW_STR += '示例: .draw狂野 .draw3#魔法物品表a'

HELP_COMMAND_HP_STR =  '记录/调整生命值: .hp ([调整目标])([符号]) [骰子表达式/数值](/[最大生命值])\n'
HELP_COMMAND_HP_STR += 'hp关键字可出现在任意处\n'
HELP_COMMAND_HP_STR += '生命值信息将在.init的结果中显示\n'
HELP_COMMAND_HP_STR += '不输入符号与目标时默认为对自己的"="操作\n'
HELP_COMMAND_HP_STR += '不设置生命值则会显示已损失生命值\n'
HELP_COMMAND_HP_STR += 'pc生命值信息与先攻列表独立\n'
HELP_COMMAND_HP_STR += '查询目标支持部分匹配先攻列表中的条目, 可以用/区分多个目标\n'
HELP_COMMAND_HP_STR += '注意dm用.ri [pc名字]将pc加入先攻列表时, 该条目不会和pc的生命值自动关联, 需要pc自己用.ri加入先攻列表\n'
HELP_COMMAND_HP_STR += '示例:\n'
HELP_COMMAND_HP_STR += '.hp 地精- 1d12+2 // 对地精造成1d12+2点伤害\n'
HELP_COMMAND_HP_STR += '.hp 20/30 // 将自己的生命值设置为20, 最大生命值设置为30\n'
HELP_COMMAND_HP_STR += '.hp 杰+ 1d8+3 // 在先攻列表中匹配名字中有杰的对象, 然后给其增加1d8+3的生命值\n'
HELP_COMMAND_HP_STR += '.hp clr// 删除自己的生命值信息\n'
HELP_COMMAND_HP_STR += '.hp // 显示自己的生命值信息\n'
HELP_COMMAND_HP_STR += '.地精-10hp // 对地精造成10点伤害\n'
HELP_COMMAND_HP_STR += '.地精hp-10 // 对地精造成10点伤害\n'
HELP_COMMAND_HP_STR += '.地精1/地精2hp-1d8 // 对地精1和2都造成1d8点伤害'

HELP_COMMAND_SpellSlot_STR =  '记录/调整法术位:\n.记录法术位\n.(查看)法术位\n.[1~9]环(法术位)[+n/-n]\n.清除法术位\n'
HELP_COMMAND_SpellSlot_STR += '示例:\n'
HELP_COMMAND_SpellSlot_STR += '.记录法术位 4/3/2  //表示4个1环, 3个2环, 2个3环\n'
HELP_COMMAND_SpellSlot_STR += '.2环法术位-1  //消耗一个2环法术位\n'
HELP_COMMAND_SpellSlot_STR += '.1环法术位+2  //增加两个1环法术位\n'
HELP_COMMAND_SpellSlot_STR += '.3环+2  //增加两个3环法术位\n'
HELP_COMMAND_SpellSlot_STR += '.1环+2  //增加两个1环法术位'

HELP_COMMAND_Money_STR =  '记录/调整金钱:\n.记录金钱\n.(查看)金钱\n.金钱[+/-][xgp/ysp/zcp]\n.清除金钱\n'
HELP_COMMAND_Money_STR += '默认的单位是gp\n'
HELP_COMMAND_Money_STR += '每次输入时必须按照gp, sp, cp的顺序\n'
HELP_COMMAND_Money_STR += '示例:\n'
HELP_COMMAND_Money_STR += '.记录金钱 10gp 30sp\n'
HELP_COMMAND_Money_STR += '.金钱  //查看当前金钱\n'
HELP_COMMAND_Money_STR += '.金钱-2gp  //花费2gp\n'
HELP_COMMAND_Money_STR += '.金钱-10gp+50cp  //花费10gp并得到50cp'

HELP_COMMAND_NOTE_STR =  '笔记功能:\n.记录笔记 [索引:]内容\n.(查看)笔记[索引]\n.清除笔记[索引]\n'
HELP_COMMAND_NOTE_STR += '清除所有笔记请输入.清除笔记 所有笔记\n'
HELP_COMMAND_NOTE_STR += '新增笔记请在最前面写一个+\n'
HELP_COMMAND_NOTE_STR += '索引名支持部分匹配功能\n'
HELP_COMMAND_NOTE_STR += '默认索引为:临时记录\n'
HELP_COMMAND_NOTE_STR += '示例:\n'
HELP_COMMAND_NOTE_STR += '.记录笔记 下次开团时间是周六\n'
HELP_COMMAND_NOTE_STR += '.记录笔记 npc名字:+镇长约翰, 车夫强森\n'
HELP_COMMAND_NOTE_STR += '.记录笔记 背包:2瓶治疗药水, 火球术卷轴\n'
HELP_COMMAND_NOTE_STR += '.笔记  //查看所有笔记\n'
HELP_COMMAND_NOTE_STR += '.笔记 背包 //查看"背包"对应的笔记\n'
HELP_COMMAND_NOTE_STR += '.清除笔记 npc\n'
HELP_COMMAND_NOTE_STR += '.清除笔记 所有笔记'

HELP_COMMAND_QUESTION_STR =  '答题功能:\n.答题 [考题]\n'
HELP_COMMAND_QUESTION_STR += '直接输入.答题 可查看所有可用考题\n'
HELP_COMMAND_QUESTION_STR += '开始答题后用户的所有输入都被视为回答, 请不要输入其他无关内容\n提前结束考试请输入Q'

HELP_COMMAND_WELCOME_STR = '自定义入群欢迎词: .welcome [欢迎词]\n入群欢迎词为空则代表不发送欢迎词'

HELP_COMMAND_TEAM_STR =  '队伍系列指令:\n.加入队伍 [队伍名]\n.队伍信息\n.队伍点名\n.完整队伍信息\n.清除队伍\n.队伍[技能]检定\n.队伍金钱 [调整值]\n'
HELP_COMMAND_TEAM_STR += '只有第一个加入队伍的人可以命名队伍\n'
HELP_COMMAND_TEAM_STR += '完整队伍信息会通过私聊发送给查询者\n'
HELP_COMMAND_TEAM_STR += '示例:\n'
HELP_COMMAND_TEAM_STR += '.加入队伍 灰色小队\n'
HELP_COMMAND_TEAM_STR += '.队伍点名\n'
HELP_COMMAND_TEAM_STR += '.队伍信息\n'
HELP_COMMAND_TEAM_STR += '.队伍先攻检定\n'
HELP_COMMAND_TEAM_STR += '.队伍金钱+110gp // 队伍内每个人获得110gp'

HELP_COMMAND_LONGREST_STR =  '长休指令指令: .长休\n必须先设置最大生命值或最大法术位才有效哦'

HELP_COMMAND_JRRP_STR =  '这个指令也不清楚怎么用吗? #吃惊\n'
HELP_COMMAND_JRRP_STR += '.jrrp 查看今日人品'

HELP_COMMAND_DND_STR = '.dnd 生成的属性值来自于r6#4d6k3'

HELP_COMMAND_MENU_STR =  '.今日菜单 查看今日菜单, 找不到对应关键词的菜肴时会删减关键词甚至删掉这道菜'

HELP_COMMAND_PC_STR =  '角色卡相关功能:\n.记录角色卡 [角色卡模板]\n.查看角色卡\n.完整角色卡\n.清除角色卡\n'
HELP_COMMAND_PC_STR += '记录角色卡后(查看模板请输入.角色卡模板), 就可以使用相关的检定与豁免功能了, 查看详情请输入.help检定\n'
HELP_COMMAND_PC_STR += '提示:\n- 必填的内容是六个基本属性,熟练加值与熟练项,其他内容为选填\n- 不要去掉模板中的换行\n- 攻击检定已经自动加上了熟练加值, 不需要也不能写在熟练项里\n'
HELP_COMMAND_PC_STR += '- 在额外加值里写"检定+1"的话, 会把所有检定(不包括豁免)哦~ 同理, 写"豁免+1",会将所有豁免的结果都加1\n'
HELP_COMMAND_PC_STR += '  如果携带了幸运石, 就在额外加值处写上豁免+1/检定+1吧\n'
HELP_COMMAND_PC_STR += '- 记录角色卡时输入的名称等同于.nn [名称], 输入的生命值信息等同于.hp [生命值]/[最大生命值]\n'
HELP_COMMAND_PC_STR += '- 如果不确定自己的理解是否正确的话, 输入".完整角色卡"确认一下吧~\n'
HELP_COMMAND_PC_STR += '- 查看所有技能名请输入.help技能'

HELP_COMMAND_SKILL_STR = f'所有技能关键字:{list(PC_SKILL_DICT.keys())}'

HELP_COMMAND_SEND_STR = f'发送消息：.send 想对Master说的话\n如果用来调戏Master请做好心理准备'

HELP_COMMAND_CHECK_STR = '属性检定系列功能: .[次数#][属性检定或豁免检定][优/劣势][加值] [原因]\n'
HELP_COMMAND_CHECK_STR += '必须先设定角色卡才能使用哦~\n'
HELP_COMMAND_CHECK_STR += '属性检定其实没有大成功和大失败, 只是娱乐效果\n'
HELP_COMMAND_CHECK_STR += '攻击检定已经自动加上了熟练加值\n'
HELP_COMMAND_CHECK_STR += '示例:\n'
HELP_COMMAND_CHECK_STR += '.力量检定优势+1d4 掀开井盖\n'
HELP_COMMAND_CHECK_STR += '.说服检定\n'
HELP_COMMAND_CHECK_STR += '.敏捷豁免优势\n'
HELP_COMMAND_CHECK_STR += '.体质豁免+4 圣武士光环\n'
HELP_COMMAND_CHECK_STR += '.敏捷攻击优势\n'
HELP_COMMAND_CHECK_STR += '.3#敏捷攻击\n'
HELP_COMMAND_CHECK_STR += '.感知攻击 使用曳光弹'

HELP_COMMAND_GROUP_STR = '群管理系列功能:\n'
HELP_COMMAND_GROUP_STR += '.群管理 [启用/禁用]功能 [功能名称]\n'
HELP_COMMAND_GROUP_STR += f'可选功能: {list(Str2CommandTypeDict.keys())}\n'
HELP_COMMAND_GROUP_STR += '.群管理 信息\n'
HELP_COMMAND_GROUP_STR += '只有最近7天内在群内发言的成员会被统计'
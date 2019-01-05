def find(movie):
    all = { '白雪公主和七个小矮人':'白雪公主和七个小矮人,戴维·汉德,特德·西尔斯 / Otto Englander / 伊尔·赫德,阿德里亚娜·卡塞洛蒂 / 罗伊·阿特威尔 / Stuart Buchanan / Hall Johnson Choir,白雪公主原本是世界上最幸福的人，可惜当她母后逝去，父王娶了她继母后，这一切都改变了。恶毒的继母处处为难白雪公主，当她父王也死后，白雪公主过得更艰难了。这天，皇后从魔镜中得知世上最美的人不是自己而是白雪公主后，气急败坏的她下令武士将她带到森林处决了，好心的武士放走了白雪公主。夜晚，森林里的七个小矮人收留了无家可归的白雪公主。当皇后得知白雪公主还没死时，气急败坏的她决定亲自出马将白雪公主害死。第二天，她化妆成了一个老婆婆，带着毒苹果往森林深处走去。',
            '木偶奇遇记':'木偶奇遇记,汉密尔顿·卢斯科 / 宾·沙普斯坦,卡洛·科洛迪 / 特德·西尔斯 / Otto Englander / Webb Smith,梅尔·布兰科 / 弗兰基·达罗 / 克里夫·爱德华兹 / Dickie Jones,孤独的木匠爷爷这晚亲手制作了一个木偶男孩——皮诺曹。可能上天眷顾爷爷，午夜，蓝仙女显灵了，她让这个木偶男孩具有了意识，能像其他男孩那样跑跑跳跳了。获得了生命的皮诺曹兴奋不已，很快和屋子里的小动物交上了朋友。早上爷爷起来见到皮诺曹惊讶不已，他十分感激上天赐给他的礼物。 然而，皮诺曹很快就发现了自己和其他男孩子还是不一样，他没有肉体，不会疼痛，只有冰冷了木制躯体。他开始不满足于现状，梦想着找到蓝仙女让她将自己彻底变为一个真正的男孩子。于是，他踏上了旅程。',
            '幻想曲':'幻想曲,詹姆斯·阿尔格 / 福特·毕比 / Samuel Armstrong / Norman Ferguson / Jim Handley / T. Hee / Wilfred Jackson / Hamilton Luske / Bill Roberts / 保罗·萨特菲尔德 / 宾·沙普斯坦, Lee Blair / Elmer Plummer / Sylvia Moberly-Holland,华特·迪士尼 / 列奥波德·斯托科夫斯基 / Deems Taylor / 科里·伯顿 / Julietta Novis /,1940年，迪士尼公司制作了第三部长片动画《幻想曲》，为动画史贡献了一部迄今仍难以企及的经典名作。本片由8部音乐短片组成，最早诞生的《魔法师的学徒》讲述了在魔法师严西（Yensid，迪士尼Disney倒写）手下学徒的米老鼠偷戴师傅的帽子，利用魔法指挥扫帚挑水并惹下大祸的 有趣故事。该片原打算收入“糊涂交响曲（Silly Symphonies）”系列，但因严重超支，入不敷出，故迪士尼决定另外结合几支经典名曲拍成一部音乐短片合集，一并发行。只是因过于艺术化以及二战等方面的原因，《幻想曲》并未取得预期的收益。除杜卡的《魔法师的学徒》外，本片收录曲目还有巴赫《D小调托卡塔与赋格》、柴科夫斯基《胡桃夹子》、斯特拉文斯基《春之祭》、贝多芬《田园交响曲》、蓬基耶利《时间舞曲》、穆索尔斯基《荒山之夜》和舒伯特的《万福玛丽亚》。 ',
            '小飞象':'小飞象,宾·沙普斯坦 / 塞缪尔·阿姆斯特朗 / 诺曼·弗格森 / 威尔弗雷德·杰克逊 / 杰克·金尼 / 比尔·罗伯茨 / John Elliotte,狄克·灰默 / Harold Perl / Helen Aberson / 乔·格兰特,James Baskett / 赫尔曼·宾 / 比利·布莱彻 / 爱德华·布罗菲 / Jim Carmichael,丹波是马戏团的一只小象，因为样貌与众不同——它长着蓝色的眼睛和一双打得出奇的耳朵——而遭到大家都取笑。有一天，一个淘气的男孩子甚至作弄了丹波，象妈妈十分生气，就教训了他一顿，因此被马戏团老板关进了笼子。为了在马戏团立足，救出妈妈，丹波必须马上学会一门拿手绝活。四出学艺的它却又四处碰壁，心灰意冷之际全靠好朋友老鼠帝莫给了它鼓励和温暖。一次意外，丹波掉进了一个大酒桶内被灌得酩酊大醉，却因此意外发现了自己的拿手绝活。', 
            '小鹿斑比':'小鹿斑比,戴维·汉德 / 詹姆斯·阿尔格 / 塞缪尔·阿姆斯特朗 / 格雷厄姆·海德 / 比尔·罗伯茨 / 保罗·萨特菲尔德 / 诺曼·莱特,费利克斯·扎尔滕 / 佩斯·皮尔斯 / 拉里·莫里 / 弗农·斯托林斯 / Melvin Shaw,哈迪·奥尔布赖特 / Stan Alexander / Bobette Audrey/ Peter Behn / 特尔玛·博德曼,这是一个关于成长的故事。小鹿斑比来到了这个世界上，和其他好朋友一起无忧无虑生活在森林里。一天，他见到了鹿群的领袖，妈妈这时才告诉他，这就是他的父亲。鹿妈妈不久就牺牲在猎人的枪下，斑比只能和父亲相依为命了。转眼间，斑比长大了。到了恋爱的季节，他为了争夺一头母鹿的爱而和另一头公鹿进行了决斗，他大获全胜；秋天来临，森林燃起了大火，在父亲的鼓励下，斑比勇敢地跃入了瀑布；春天又得到了，斑比真的长大了，成了鹿群的新领袖。 ',
            '致候吾友':'致候吾友,Wilfred Jackson / Jack Kinney / 汉密尔顿·卢斯科 / Bill Roberts,特德·西尔斯 / William Cottrell / Webb Smith,Fred Shields / José Oliveira / Pinto Colvig / 华特·迪士尼 / 克拉伦斯·纳什 /,1940年代初期，欧亚各国正为二次大战打得如火如荼，当时美国原本希望孤立欧亚各国之外免受波及，所以非常重视与中南美的邻邦关系，华特迪士尼之前几部电影《白雪公主》、《木偶奇遇记》等尚无缘与欧亚地区观众见面，但在拉丁美洲已热烈上映，米老鼠、唐老鸭早已风靡当地观众。因此美国国务院就邀请华特迪士尼代表国家到中南美亲善访问。1941年，迪士尼花了约六週的时间走访中南美各国，顺便拍摄了许多当地风土民情，回国后迪士尼便推出了本片。 本片共包括四个段落∶1. 的的喀喀湖（Lake Titicaca）；2. 小飞机培卓（Pedro）；3. 高卓族的高飞（El Gaucho Goofy）；4. 巴西之旅（Aquarela do Brasil）。四个段落分别是由NormanFerguson、WilfredJackson、JackKinney、HamiltonLuske、BillRoberts共同执导，片中迪士尼运用了巴西知名作曲家AryBarroso创作的一首歌曲“AquareladoBrasil”，由于电影的宣传，让这首歌成为世界名曲！而本片的主题曲“SaludosAmigos”则是由EdmondoSantos作曲、CharlesWolcott作词，获得奥斯卡最佳歌曲提名。',
	    '三骑士':'三骑士,Norman Ferguson,James Bodrero / Homer Brightman / Del Connell / William Cottrell / 比尔·皮特 / Elmer Plummer / 特德·西尔斯 / Ernest Terrazzas / Roy Williams / Ralph Wright, Aurora Miranda / Carmen Molina / Dora Luz / 斯特灵·哈洛威 / 克拉伦斯·纳什 ,硕大的包裹，便签上写着“祝唐老鸭13号星期五快乐，他那美洲的朋友”。唐老鸭见此非常快乐，连忙拆开礼物。里面是一整套放映设备以及录影带。他安装完毕，静下心观看，哈维博士为他讲述了3个禽类亲戚的故事：《怕冷的企鹅》住在南极的企鹅巴比极度怕冷，暖炉是他最爱的伙伴。为了寻找温暖，他开始了一段伟大航程；《高卓小飞骡》乌拉圭宁静早晨，少年道奇多外出打猎，却在崇山峻岭间看到一只会飞的骡子。他要带着飞骡参加一场赛骡比赛，一战成名；《巴西与墨西哥之巡礼》跟随绿色鹦鹉的脚步，唐老鸭来到热情狂热的巴西和墨西哥，独有的风俗以及各种有趣的知识，此外还少不了充满激情的舞蹈。 ',
            '为我谱上乐章':'为我谱上乐章,罗伯特·科马克 / 克莱德·杰洛尼米 / 杰克·金尼 / 汉密尔顿·卢斯科 / Joshua Meador,Homer Brightman / Dick Huemer / Dick Kinney / John Walbridge,Nelson Eddy / Dinah Shore / Kelsey Heart / Benny Goodman / The Andrews Sisters /,本片由十个段落组成，每个段落分别以不同的音乐表达，有些段落有剧情，有些段落只是纯音乐，还有通俗的音乐，像爵士、民谣等，此片巧妙地将音乐、喜剧、马戏、歌剧熔为一炉，是较为经典的短篇音乐合辑动画片。 本片是迪士尼第八部经典动画。本片共包括十个段落︰ 1.马丁与可依﹙Th e Martins and t he Coys）乡村民谣 ;2.蓝色拜伦河﹙Blue Ba you）诗歌 ;3.大家来跳舞﹙All the Cats JoinIn）爵士间奏曲;4.没有你﹙Without You）蓝调 ;5.强棒凯西﹙Caseyat the Bat）戏剧吟诵 ;6.俪影双舞﹙Two Silhouettes）芭蕾三联韵 ;7.彼得与狼﹙Peter and the Wolf）音乐剧 ;8.自君别后﹙After You\'ve Gone）四种乐器演奏曲 ;9.软呢帽强尼与蓝绒帽艾莉丝﹙Johnny Fedora and Alice Bluebonnet）爱之颂 ;10.唱歌剧的鲸鱼﹙The Whale Who Wanted to Sing at the Met）歌剧挽歌',
            '米奇与魔豆':'米奇与魔豆,Jack Kinney / Hamilton Luske,Edgar Bergen,Edgar Bergen / Dinah Shore / Charlie McCarthy,邦果：本片根据Sinclair Lewis的原著改编。讲述了一只生活在马戏团名叫邦果的明星小熊，他会走钢丝、帽子戏法、骑独轮、打拳击，深受大人和小朋友的喜爱。但是它只能生活在笼子里，跟随马戏团周游全国各地，上演同样的戏码。有一天，邦果决定逃走，回到久违的大自然，在那里， 有新的考验和冒险在等着它；米奇和魔豆：在一个名叫欢乐谷的美丽所在，狂暴的巨人抢走了会唱歌的竖琴，从此欢乐谷变成了干枯荒芜之地，人们饱受饥馑之苦。某天，米奇用奶牛换来了三颗魔豆。夜晚，魔豆生根发芽，直冲云霄，带着米奇、古菲、唐老鸭来到了巨人的宫殿。本片为迪士尼公司在二战期间制作的package films，是沃尔特•迪士尼为最后一次为米奇这个角色担任配音。',
            '旋律时光':'旋律时光,克莱德·杰洛尼米 / 汉密尔顿·卢斯科 / 杰克·金尼 / 威尔弗雷德·杰克逊,温斯顿·希布勒 / Erdman Penner / Harry Reeves,罗伊·罗杰斯 / Trigger / 丹尼斯·戴 / The Andrews Sisters / Fred Waring /,本片是迪士尼于1948年推出的第十部动画长片，也是该公司制作的第五部短篇合集，它分别由冬日回忆（Once Upon a Wintertime）、狂乱的飞行（Bumble Boogie）、强尼苹果籽（Johnny Appleseed）、拖船小嘟嘟（Little Toot）、树木之颂（Trees）、忘情森巴舞（Blame it on the Samba）和佩柯斯`比尔（Pecos Bill）等七部音乐短片组成。音乐风格涵盖古典、流行、桑巴、爵士，应有尽有，剧情上既有无拘无束的奇思妙想，也有根据美国民间人物改编的故事。许多当时著名的歌手、演员、作曲家、动画人加盟制作团队，打造出丝毫不亚于幻想曲的经典动画作品。 不仅是迪士尼的粉丝，任何一个动画迷都不可错过的杰出之作！'
           } 
    a = str(all[movie])
    c = a.split(',')
    return c
from manim import *
import numpy as np

'''
A_coef=[(-2.6421516649584778+1.149892777491846j),
 (1.1232801565247013-1.0428251898431717j),
 (-0.9262338211696004+0.010025063317212429j),
 (-0.20582182088316486-0.06216296062693859j),
 (-0.03237294243479629+0.023853196991445096j),
 (0.12381331589579969+0.0898359296234999j),
 (-0.0393980787491381-0.04109401988609535j),
 (0.06228604211473088+0.14086373791575346j),
 (-0.002282016600699878-0.049685903815594526j),
 (-0.03094113687058565-0.04738693243749914j),
 (-0.04243410532670546+0.10628318023127652j),
 (0.13830658795941908-0.114420817935028j),
 (0.03965392971928919+0.0024539759394829022j),
 (0.05759799838647492-0.016239075476153757j),
 (-0.06438574841832209-0.04358434321065297j),
 (0.038270675890409625+0.003895047189746839j),
 (-0.04714232739148489-0.03527498565102764j),
 (-0.019156293626191718+0.046918455122039994j),
 (-0.007306370139722974-0.03543030223522173j),
 (0.04291530810341284+0.047278092360279786j),
 (0.006829045764838537+0.03759002706225075j),
 (-0.0057279519787654005-0.059346581724077675j),
 (-0.04508421189468573-0.034739484385231376j),
 (0.023204768977101428+0.014870705884494205j),
 (0.002008207194962899+0.008561004778684607j),
 (0.004451659854463803-0.0757452023840379j),
 (0.003242795834542381+0.026877308006082814j),
 (-0.03512062684102231-0.014190895480551j),
 (0.016922167781810382+0.028943913801520647j),
 (-0.0004539160161776452-0.013882215749418994j),
 (-0.00398356893611779-0.014288704025399373j),
 (0.007565173888734969+0.010071619260196427j),
 (-0.014634742834394282+0.022846844962759544j),
 (-0.02788220577455158+0.006042656784233286j),
 (0.017488790174175966-0.001989140445739966j),
 (0.02791738265235213-0.013790271673235223j),
 (-0.01657393756617511-0.008001692073680096j),
 (0.001501794143483295+0.00254408486904607j),
 (0.009554685581219462+0.0003103403234183126j),
 (-0.003529969226372044+0.009027705423879881j),
 (0.0019217579200048894+0.014320094348527665j),
 (-0.016746602388548228+0.005738086546490675j),
 (-0.008206761826019962-0.004306027935770382j),
 (0.0003057717879875285-0.00019726791070607261j),
 (-0.010393416378761157-0.0002895683408591845j),
 (0.00011535741126350558+0.0039318432493910755j),
 (-0.00016591602733014374+0.0020088383374294643j),
 (-0.004133698908906221-0.011301207056914704j),
 (-0.0013076588493417087-0.007280141991500145j),
 (0.007845887310161375+0.00889461804150305j),
 (0.012635110045022184-0.006464374220263602j),
 (-0.0018406513467722839+0.008849066433646234j),
 (-0.0022713396143119063-0.0022192125914539387j),
 (-0.005057767796772321-0.00435822105957151j),
 (0.0010228158975438724-0.004189188112124443j),
 (0.00258616552087331+0.002329023532980307j),
 (-0.0038837127285645968+0.005759648294925297j),
 (0.008353551204138282+0.0010248681308006942j),
 (0.004482883759795852-0.0016532452339119358j),
 (-0.0050097832135896515-0.002064310900333658j),
 (-0.0021101092778304954-0.007636555184862858j),
 (-0.0027536146681011366-0.00031100723869869793j),
 (-0.0025745264801083933+0.006607205053472652j),
 (0.0028394094092344057+0.0026187879362783648j),
 (3.79143610733727e-05-0.005861911157187437j),
 (-0.0011599847279282055-0.009994725664815263j),
 (0.00040341160711021595+0.0019572999059559865j),
 (0.005107268168851829-0.004621219883718934j),
 (-0.002863621299885615-0.00021563439029828157j),
 (-0.003992055404600523+0.00017794301531295038j),
 (-0.0016781694849155972-0.0014580036243147163j),
 (0.007108496125333154-0.002733799349931373j),
 (0.002133775451676505-0.0011238555859215775j),
 (-0.0011260702819796836-0.00738816316906898j),
 (-0.0029144539380965236-0.00015364793928878982j),
 (-0.002301924338900738-0.005509364866543972j),
 (0.006169744019135879-0.005646492548344758j),
 (-0.007080678661468526+0.0026830947532274652j),
 (0.0007519946478198695-0.004627263244592756j),
 (0.0017722497331522408+0.0004490395715652743j),
 (-0.0010181675266646211+0.003247581249654854j),
 (-0.0014657063892666825-0.002417845272805442j),
 (-0.0022673846614637808-0.0007960363325780984j),
 (0.00025515856892542723-0.0017535414850991123j),
 (0.00386886160085736-0.001970997833557943j),
 (-0.0007261141344706929-0.002297927063376785j),
 (-0.002549867675406739-0.006868332381403784j),
 (-0.004542661966652703-0.004256417763971757j),
 (0.0014561891303814987-0.0033991237496154725j),
 (0.002866134087635106+0.004003069452651335j),
 (-0.0013241356872987174+0.001110108788832102j),
 (-3.352038292655992e-05-0.007776105414994665j),
 (-0.006255983989744352-0.005157523824819538j),
 (-0.0028050165121686144-0.006600392358256614j),
 (-0.0010316932739607063-0.00046652697459152254j),
 (0.0008948738753615408+0.0018993210775166726j),
 (-0.001241645399923432-0.0029083867144204913j),
 (0.002630285563025039-0.0010604001925857052j),
 (0.0023913154852113106-0.003275401805660539j),
 (-0.002541407529043923-0.0030651314171899267j),
 (-0.0009047706738685673+0.001647277759368938j),
 (-0.0014019825444406752-0.00410132365942836j),
 (-0.005029465192376389-0.0024110444463315084j),
 (0.0013472290573091161-0.0031287961597570337j),
 (-0.00044909665956978937-0.0017560570307377042j),
 (-0.0015163052458659013-0.0018751889247265439j),
 (-0.003951100145559071-0.003715370200038592j),
 (0.0010451082295166551-0.003752360122198888j),
 (-0.001302363352887664-0.0005798941833544815j),
 (-0.00483862620059931-0.001605968592875822j),
 (-0.0002598385374117948-0.0028426980174226482j),
 (-0.00045656353232726923-0.001098998100768115j),
 (-0.001877456915946633-0.0012623543456575324j),
 (0.00044241703772808294-0.0015425982493985795j),
 (-0.00199999682664174-0.004304789632165676j),
 (-0.001504901574289002-0.0019170699324937647j),
 (-0.0019508371246780066-0.001104535095343814j),
 (-0.0028922054338787985-0.002792354983822085j),
 (-0.0028170137735449284-0.003435443445716404j),
 (-0.002547197792911227-0.0015676965236957074j),
 (0.0009469436202020924-0.002848866667476927j),
 (-0.078272339767788+0.14881586183749715j),
 (0.035908141059106266+0.018914963733976043j),
 (0.20443014878953467+0.011565716573472348j),
 (0.21298013538831084-0.013549667197591625j),
 (0.19244349756410123+0.07755845357756251j),
 (0.2561683477204238+0.03218073697804295j),
 (0.23189837420312748+0.0746785481928227j),
 (0.14283021975323376-0.05249257643009379j),
 (0.0489111026489356-0.019210767222790574j),
 (0.02335595245577587+0.1085736201038933j),
 (-0.001407143134527535+0.018820169913118755j),
 (0.03202159955667735-0.05092904204285675j),
 (-0.016701131325085276+0.0034769688386354753j),
 (0.032488999271525064-0.06519487618267394j),
 (-0.016764320613208195-0.023987630855006225j),
 (-0.022955053333501122-0.03206144350075149j),
 (-0.05053659101185548-0.004059142773037396j),
 (-0.004833714802833636-0.03115956294160637j),
 (-0.04411533398218195+0.015843159610752347j),
 (-0.011946959377108412-0.006310487202037328j),
 (-0.012311156571784812-0.04302057471107205j),
 (0.02114188718873499-0.00566788060517351j),
 (0.061375850318095296-0.01672682499289248j),
 (-0.007691352154968824-0.011347271584911464j),
 (0.06641706265851745-0.027608003834192905j),
 (-0.018945019038514897+0.009006378984804771j),
 (0.042763373255620955-0.01747691205331024j),
 (-0.006942429697223967-0.0186618417761933j),
 (-0.02887447429611941+0.001994062154002097j),
 (-0.03829315726446255+0.008189127916862155j),
 (0.0071297574883750214+0.006761343263486879j),
 (0.009132471826524425-0.01413868213692108j),
 (0.002231231051242691-0.01277541562044104j),
 (0.02305069005852132+0.026113734585191558j),
 (-0.00909717038791935-0.019762929454143294j),
 (0.017514865825037713-0.01892663465729143j),
 (0.01808217155848944+0.006742634980285121j),
 (-0.0001324502657847287-0.021560263880196467j),
 (-0.002119957266953144-0.006906834890921509j),
 (0.02813675232049739+0.0081267640523369j),
 (0.009514525360465664-0.0017163827270330312j),
 (0.017936104737951028-0.01894480425233353j),
 (0.006761233099831852+0.008653140076169834j),
 (0.010322215388205293-0.001994284564260439j),
 (0.009193217120749162+0.0020960586231326115j),
 (0.01504795087457223-0.001439154876873715j),
 (-0.001975670003039662-0.01660650921319653j),
 (0.006266254800135631-0.007258763870611794j),
 (0.007933617189038792-0.01466894579564872j),
 (0.011510116897323668-0.004295912320820056j),
 (0.008377596097004494-0.0011407541027254455j),
 (0.0012600412225247694+0.011535174816744232j),
 (0.009317815525312958-0.005391549734214537j),
 (-0.0010081696199891734-0.004455093388427471j),
 (0.006988759385680672-0.001519537833837153j),
 (0.0001043413801648243+0.005803856570789172j),
 (0.005522830694453798+0.0023699661452415894j),
 (0.010312348779315271-0.008429890293321387j),
 (0.0042777599102768495+0.015646034049378067j),
 (0.0011595459432125147+0.009342898594216179j),
 (0.009359374807378112-0.0043250131525812505j),
 (0.0033720115400316703+2.4751190785704367e-05j),
 (0.006397302130063222+0.006076402936167109j),
 (0.0005236925131083658-0.005122881644827316j),
 (0.009791901297181351-3.6755145056091335e-05j),
 (0.010848643485252133+0.006628620912774945j),
 (-0.002338026717331736+0.0033867664646905155j),
 (0.0004403669803771425+0.004497957113247287j),
 (0.008753513458305155-0.0014950953719166167j),
 (0.005752168901062187+0.001648712315699206j),
 (0.00217821549305744-0.002379049253954122j),
 (0.0015469700154186567+0.0028700728816287734j),
 (-0.00023734871031526078+0.0025012344181462097j),
 (0.002484873389619604-0.004837746639319129j),
 (-0.00036572038805587296+0.0030317799314626285j),
 (-0.001508962012911365+0.0014438926587764316j),
 (0.0005031511240856723+0.004327526427983084j),
 (0.008802248950027859+0.004208955071749325j),
 (0.001931804346333926-0.0009183111440782012j),
 (-0.0011844790654280933-0.002683108553025617j),
 (0.0006862719706008599+0.004616443662614211j),
 (0.0011883522522386349+0.0005325554724606263j),
 (0.0020778677599893186+0.0012917144819128052j),
 (0.0021469475030827345+0.002944496651839243j),
 (0.004405855381323503+0.002201590505961017j),
 (0.0030231321167039455+0.002447334898624802j),
 (0.007597684779459558+0.0006170123274732377j),
 (0.001590004029887804-0.0037478900811614875j),
 (0.0011117181534654956-0.004894180336702356j),
 (-0.0019662099786451775+5.680092457789226e-05j),
 (-0.0022605793324606354+0.003880963503124473j),
 (0.001617221978434248+0.0061543954245747694j),
 (0.0021156624507981834-0.0012823819615075491j),
 (0.005335096883350784-0.0029782889743979277j),
 (0.001874580324102737-0.00032332112577834694j),
 (0.00221104986913001+0.0025653550039966364j),
 (0.005047646237579937-0.0005770769669348285j),
 (0.00011175696504590307-0.0025635500780663736j),
 (0.004198330193500087-0.001060300454261592j),
 (-0.0010899605239495823-0.0010093097252323615j),
 (-0.0008485844899739441+0.002950541310249265j),
 (0.004187958567759123+0.004150657589242436j),
 (0.0062737533557583455+4.070413663472179e-05j),
 (0.0010585806047615374-0.0054360620832336545j),
 (0.002295819410990231+0.0008060531968800363j),
 (0.0025378090296001923+0.004261321584607171j),
 (0.0017464258444434588+0.003800479942953641j),
 (0.0027042464956417668+0.002626602223473655j),
 (0.0015543416284320806+0.001566736538932328j),
 (0.004620800134500498-0.0017638935418197495j),
 (0.002155270136905688-0.0015261767154458525j),
 (0.0012752189112943404-0.0010309113721271104j),
 (0.00019689116847101555+0.001957209001764033j),
 (0.0016235909552816397+0.0037529437095492496j),
 (0.004253613719102464+0.000833164397513404j),
 (0.003167608860724388-0.0002452188758483117j),
 (0.0002472750183752983+0.0016321505112099025j),
 (0.002499681433405865+0.000594996413670077j),
 (0.0011966491293484566-0.00023000988901401023j),
 (0.0016827005308220708+0.0038231639981906674j)]
NNN=120
'''
'''
A_coef=[(-0.9306107930149318+0.2374539943710767j),
 (1.4515495476697864-0.9176883174094925j),
 (-0.7767907471901958-0.41522692201670425j),
 (0.13423860381984257-0.055272185254890305j),
 (0.13617719428948677+0.1879415286143255j),
 (0.15347447883576107+0.25797146998347903j),
 (0.24998924234857725-0.022734522846977516j),
 (0.09456535302196067+0.1686049385640814j),
 (0.24954890862233867+0.14139802660163214j),
 (0.18298067272602664+0.15360846943191578j),
 (-0.016820765722122013+0.044825697486423816j),
 (0.12291906246175764+0.2460254554904613j),
 (0.1560133507482267+0.04244769990063508j),
 (0.11147971909908737+0.13385039680750685j),
 (0.08450228126442166+0.08319859082592344j),
 (-0.05566845099882632+0.03854485845676047j),
 (0.08398419848762911+0.07421907603369421j),
 (0.032305322505414666+0.009353540500509919j),
 (-0.02158153020358095+0.12915373785228224j),
 (-0.009331920252214953+0.07569046557851518j),
 (0.02773707293690688+0.10327924664228852j),
 (0.010416632806014302+0.029600026580660965j),
 (0.07936829455223311+0.05953951157122045j),
 (0.04103583330397461+0.04152842274227409j),
 (0.023881391278886617+0.04753245213255088j),
 (0.012765970454296505+0.057008258139130616j),
 (0.07890300369229233+0.1105016503207209j),
 (-0.02581508667583196+0.018941237641982096j),
 (0.04561216882894327+0.04481884966196091j),
 (-0.01944177594469176+0.09550453509238535j),
 (-0.01893469428803263+0.08518850967125537j),
 (0.0026844188877608016+0.08148176705294813j),
 (0.0032668907389888984+0.05197019552976141j),
 (-0.025128498382517146+0.028741018943180804j),
 (-0.03137885630550228+0.07618125013609893j),
 (-0.009873591473606363+0.05164464309816343j),
 (-0.0240452359004609+0.04063793233142185j),
 (-0.01729798357227553+0.06261666784417848j),
 (0.01180974779090091+0.039765669117455986j),
 (0.008994079672755185+0.03863517785894685j),
 (-0.030528608798110875+0.05018054400621955j),
 (-0.0320356287891319+0.03211131785740449j),
 (-0.01678471921260757+0.04854761950905796j),
 (-0.009669302264717258+0.04265214491271309j),
 (-0.015731878929611955+0.035261472200986056j),
 (-0.03730930287659183+0.04022304090361813j),
 (-0.02285387428406922+0.02603626294397394j),
 (-0.025422352713077842+0.04610906903011714j),
 (-0.01596921920101767+0.04501642980048267j),
 (-0.027602580427933527+0.023224604645079614j),
 (-0.037572481277342036+0.025871510994167426j),
 (-0.007419858675512685+0.03006864950001811j),
 (-0.028783066352214167+0.03218633905159114j),
 (-0.02437985852936815+0.029037780693044878j),
 (-0.0237953698022855+0.026367393418747456j),
 (-0.024710399389375328+0.023743063983576233j),
 (-0.028046971172567728+0.028180790171715084j),
 (-0.009653282165739548+0.018968061808817268j),
 (-0.0213064712620609+0.020481788131793868j),
 (-0.024799471871333977+0.025948888600513982j),
 (-0.02611833905959507+0.018454020177654493j),
 (-0.03141113279871844+0.02618010356192515j),
 (-0.017736887621094034+0.016188363066828484j),
 (-0.015057108611131161+0.02131891907261257j),
 (-0.006171967114445408+0.015687100943527654j),
 (-0.018710056441514487+0.016072623252896007j),
 (-0.0335427183428934+0.010153145928458021j),
 (-0.012201384786897598+0.01570814581274692j),
 (-0.013543701532428063+0.013254812185498788j),
 (-0.018199602895435638+0.017842222232071762j),
 (-0.024109284050584205+0.02099470908149573j),
 (-0.008567584592398399+0.012925435879940838j),
 (-0.011284286244940274+0.012195252230149339j),
 (-0.010581184204464845+0.017087576238187293j),
 (-0.014314229847025371+0.008031544240014456j),
 (-0.020465459667294156+0.014917790693968754j),
 (-0.01449596419294507+0.013214509835347362j),
 (-0.010733817372278536+0.014719501059874518j),
 (-0.017138082872422973+0.010324868514911182j),
 (-0.007523254381291009+0.008949522816590097j),
 (-0.010601175172471555+0.007789078764357328j),
 (-0.01110520525973689+0.010969660849617442j),
 (-0.018781559600871387+0.011093114170455214j),
 (-0.01077144375298653+0.004426255392927094j),
 (-0.0070274047578072225+0.013618427048968774j),
 (-0.016379905974554576+0.010230059351252378j),
 (-0.011434944076265966+0.004615272119677794j),
 (-0.00790749567082199+0.015749778666658307j),
 (-0.016579886932495666+0.00944041833676385j),
 (-0.010652465260598208+0.005758575792241314j),
 (-0.005861417058501205+0.006155774203673221j),
 (-0.00999744301690484+0.015801869547359987j),
 (-0.008860959490782406+0.012203260099312671j),
 (-0.0065132924992013525+0.007540152053196212j),
 (-0.01572452216817248+0.006005900029609832j),
 (-0.00990256262347961+0.0057392926484930015j),
 (-0.014245292836573876+0.007890799457617103j),
 (-0.018382391421865+0.009527178321333998j),
 (-0.006554604120301288+0.007745054309405988j),
 (-0.012502383419324123+0.006016076303963005j),
 (-0.006604385763924615+0.003835610741180335j),
 (-0.011171393681141905+0.004505286664886653j),
 (-0.012627659533788738+0.004228618320767699j),
 (-0.011739446706032509+0.009161184338642919j),
 (-0.013068602513985828+0.00676337944131767j),
 (-0.010545525951156848+0.0011260272129351477j),
 (-0.00911542561831658+0.004730431462090861j),
 (-0.006426623941179005+0.007774514060124417j),
 (-0.011264127983699454+0.00499890027531322j),
 (-0.007988086676386499+0.00590492802429176j),
 (-0.00709215602486966+0.002189587142849768j),
 (-0.009114049305514274+0.0033691354575242096j),
 (-0.006455616696828733+0.005524705463330741j),
 (-0.009490573446747738+0.003265503364168281j),
 (-0.009613778254584454+0.0037967093293227766j),
 (-0.011239608801740283+0.003136492584554163j),
 (-0.00983214714771096+0.005089878411955465j),
 (-0.002944736564421988+0.005994522972374378j),
 (-0.0030221853512410364+0.0014867313856048174j),
 (-0.009904225888577832+0.0022027585944858043j),
 (-0.006994174135452575+0.004197270788021689j),
 (0.1683468573501701+0.04530450151597021j),
 (0.1798319273994386-0.1800821976359605j),
 (0.16866638116983412-0.2173697182219945j),
 (0.1049838896979627-0.20240342455046764j),
 (0.09786504048316627-0.041643106549119735j),
 (0.02679862018484321+0.0619400730741671j),
 (0.19650922951998118+0.20275213372834355j),
 (0.24026518775227376+0.21010941191254778j),
 (0.27048252624785085+0.07826591831049329j),
 (0.24761278850166757-0.04428339750700204j),
 (0.09942400338319038+0.047000529920025035j),
 (0.03321107951887531+0.019499205647213785j),
 (0.08000082342185329-0.06096647905999638j),
 (-0.0017122378171217946+0.005042899894195122j),
 (0.08855149692292826+0.010093531116951267j),
 (0.06307824262079002+0.014853375244575976j),
 (0.10059139980113375-0.048540448109316285j),
 (0.0495231353864938-0.010945295673666635j),
 (0.05290145510196864-0.0622280301130184j),
 (0.03632666609872186-0.0015061748851191341j),
 (0.07166427881989028-0.032054335242643554j),
 (0.043095529486257486-0.037003137495536464j),
 (0.04677244137271059-0.05862628715557702j),
 (0.04689390098785993-0.12508830213593963j),
 (0.08260023348649768+0.00867428744110824j),
 (0.029655918255249776-0.03439745178839727j),
 (0.07609042186216156-0.030220136609517233j),
 (0.03894520193011128-0.07186656558314933j),
 (0.041815293610836836-0.0053285649278382655j),
 (0.021994118878628986-0.012951055777289654j),
 (0.04942929031669041+0.0019394877748381946j),
 (-0.002971967521724812+0.009099545231335151j),
 (0.013209138028131968-0.03345088694105248j),
 (0.0445990876800598-0.023608479509190084j),
 (0.01713163737931214-0.015219667808572044j),
 (0.031896712008732606-0.0316351992842833j),
 (0.010504492938390137-0.03854036400158123j),
 (0.011101368771884744-0.004355160143538607j),
 (0.02600206814741669-0.018245461945996112j),
 (0.00665951543774339-0.03205153106645347j),
 (0.03680402274357672-0.001201863166107259j),
 (0.015047233531110236-0.03292317736515102j),
 (0.00970069065175561-0.019597748417196487j),
 (0.017785110526729347+0.004667530419707443j),
 (0.030612686825959464+0.003327972964989068j),
 (0.010415743656118609-0.017745883858865122j),
 (0.02699656156908061-0.01305579033596652j),
 (0.01980428629861114-0.01073970986191705j),
 (0.02355161786574157-0.001048853817800498j),
 (0.009321859551509142+0.0028808179355914584j),
 (0.008443473064951726-0.007858578847240673j),
 (0.007316771328489022-0.01823649362739039j),
 (0.016257441056294498-0.004746528588688164j),
 (0.015979645968674402+9.01500838188516e-05j),
 (0.02866885254588603-0.003053695160346555j),
 (0.014235648606276045-0.007911676380413526j),
 (0.020025014515548206-0.006968197719878217j),
 (0.02230484691453147-0.010744186891735527j),
 (0.012424414694342398+9.460909551562053e-05j),
 (0.015050610255443563-0.005520121491502706j),
 (0.018380145757874545-0.006323148958943768j),
 (0.018695684599854604-0.017795002635888648j),
 (0.01155898184001006-0.01473918421625563j),
 (0.0067677295226219155-0.005399231996804227j),
 (0.021288601436357413-0.005735730552239324j),
 (0.014022636147712639-0.008902455800733339j),
 (0.01636822956163225-0.0010314482808056087j),
 (0.007855840937154471-0.008498789641599884j),
 (0.00726246352489188-0.010829492446046267j),
 (0.021183586333152763-0.01268530607578285j),
 (0.007360626498414839-0.008332105432237j),
 (0.01644161144283683-0.005093187088563156j),
 (0.012340008290083491-0.013908479137561875j),
 (0.009018785704450706-0.003268005262655415j),
 (0.01117588148237994-0.0034964234692341986j),
 (0.01366468013699712-0.017836068769500734j),
 (0.011545677795938996-0.01624842133496628j),
 (0.009691905514517183+0.0011719434587391918j),
 (0.01328103695519587-0.00939891352679781j),
 (0.005464200099754475-0.013140309367442725j),
 (0.013185587952255556-0.001778594792214215j),
 (0.016668976054186338-0.007475268731417079j),
 (0.015187681580616143-0.012910396361324957j),
 (0.006792928939407302-0.008314987233933233j),
 (0.011165577699651864-0.0044281510848636334j),
 (0.014659708228153608-0.0072941489396354565j),
 (0.006866530400818164-0.006814671037961979j),
 (0.013400332506698153-0.003294355253726864j),
 (0.012226973114193943-0.007071877958536948j),
 (0.011223595955545385-0.008926178021448582j),
 (0.011032478600716007-0.00654747485930263j),
 (0.01086572618969238-0.0021662160930165353j),
 (0.01107784109603421-0.007055144195105686j),
 (0.014585540106402416-0.007082777778615548j),
 (0.012511255629172243-0.004053131906780799j),
 (0.012681209421113747-0.005590872146857519j),
 (0.008541241333372364-0.010436831406018691j),
 (0.011585266292832028-0.003096802511650426j),
 (0.01596467285975684-0.00476577060256179j),
 (0.01330733573071188-0.006081876207337614j),
 (0.008083292375927087-0.007340714056861337j),
 (0.01278750575559418-0.005562029446444401j),
 (0.013955496241730161-0.010461917657368194j),
 (0.010402054798410611-0.006178405165971942j),
 (0.007753456048555139-0.00760704240809393j),
 (0.012792667985003284-0.00588363573410112j),
 (0.011193783230884172-0.0064429399845451546j),
 (0.012417913240208132-0.006604193799226456j),
 (0.009730767150035662-0.007152773436857626j),
 (0.012676620759137109-0.008544607935336134j),
 (0.012849555406134631-0.009985143079794487j),
 (0.007590480417904729-0.0093730350596188j),
 (0.009993344359205784-0.009495987812302402j),
 (0.008240804218056003-0.005261402427023665j),
 (0.010999573635723318-0.00954674948526561j),
 (0.010469802253161638-0.008862029815130968j),
 (0.007852012006454587-0.0073057905723018955j),
 (0.009144506380584729-0.00449469640305049j),
 (0.010919681537779655-0.0061400980190073375j),
 (0.0076159890319326615-0.007373206069349397j)]
'''
A_coef=[(0.1433160730054577+0.4418819510274488j),
 (-0.7056403403557935+0.5466220427290703j),
 (0.3449388199753438+0.020269780544855752j),
 (0.2364512620865351-0.42362994865179315j),
 (0.4454538897496159+0.023034810675411927j),
 (0.20099605479689825+0.04400779132430747j),
 (0.15518628708121604+0.07456426091439551j),
 (0.3233179846694193+0.1413674112089209j),
 (0.04434428706619294+0.12025830468337037j),
 (0.13556380978888471+0.025348302716956057j),
 (0.17135609043926098+0.1764956942454702j),
 (-0.0901404150169+0.019041344145021885j),
 (0.19452682343657973-0.011807330668372841j),
 (0.16769783419653958+0.11773490879725138j),
 (-0.06396156151149651+0.022486300140677477j),
 (0.11994486913833236+0.04333855816718805j),
 (-0.008821347824605596+0.07673824444428247j),
 (0.01721880971379288+0.059965942289599845j),
 (0.05842443969501097-0.026744413658681444j),
 (-0.07336177987227158+0.08508526445587064j),
 (0.06346839084255539+0.009960919397584313j),
 (0.060721946236630645-0.0453395513164289j),
 (-0.008261114304964219+0.1514016045353885j),
 (0.043630998082082526-0.0098774066612958j),
 (-0.051064961102316876+0.026539432316883355j),
 (0.021828102645151903+0.05069800659702926j),
 (-0.0006403031127972099+0.030134282792796892j),
 (0.022092296675532194+0.05402227310212922j),
 (0.07883546664198186+0.04272728027297598j),
 (-0.00817749581685414+0.05275708792187361j),
 (0.0890396104337445+0.07503273701940802j),
 (-0.033663757573314815+0.030127851491981272j),
 (0.037933511696021466+0.0668616375652105j),
 (-0.038569468084042685-0.014371523157793078j),
 (-0.05068132697866044+0.014572312161368228j),
 (-0.012350717190427237+0.08684284713780163j),
 (0.021224671084796688+0.07246961894455607j),
 (0.018074258709316008+0.013302244495366078j),
 (0.0003859279363353412+0.016762476205958048j),
 (-0.10278778315586053+0.046389311756839975j),
 (-0.0016703560509011895+0.06516941952787576j),
 (0.031692631717337404+0.01192479288727828j),
 (-0.05594806902341943+0.01103862596100677j),
 (-0.029032218532436368+0.03949172013358267j),
 (0.009945507682177139+0.08433836256779748j),
 (-0.07134219031285575+0.03166859649983164j),
 (-0.02257415260625452+0.017308066024086962j),
 (0.029664877217946008-0.0037079094559207817j),
 (-0.022017855663004477+0.0322867922726362j),
 (-0.038363323070281986+0.013559420122225647j),
 (-0.06124903841203836-0.0033628532504394485j),
 (-0.0252102296150606+0.011853594209531316j),
 (-0.0076368742442002365+0.048734111075059344j),
 (0.012632058235966389-0.0036291736374452817j),
 (-0.018899406322802154+0.018524434556956317j),
 (-0.04488454932175353+0.00900881432072744j),
 (-0.027333819223218734-0.009573843112256158j),
 (-0.025148164767523074+0.008908043488136681j),
 (-0.03427265176123827+0.013252391769463794j),
 (-0.011699292487866848+0.031190958612094293j),
 (-0.0063673376723502005-0.008612582651339544j),
 (-0.021489210906836722+0.011135742191762745j),
 (-0.028366487427786146+0.008722727508835692j),
 (-0.03535234425387586-0.016349242569214183j),
 (-0.03215443239097694-0.030304562574102877j),
 (-0.05392496694938562+0.0030976871935443602j),
 (-0.005099210570392911+0.007148831440554784j),
 (-0.03587073233484649-0.0024115724567542246j),
 (-0.016429368670986006-0.0018773963492558577j),
 (-0.0322312304400999+0.0017809566178267344j),
 (-0.01859996001914411+0.006263963283286093j),
 (0.0046443653213945205-0.008412728657839822j),
 (-0.018093081607206643-0.001248403485602326j),
 (0.0048204901967067015-0.002477972729794156j),
 (-0.008985605793434957-0.0023653929916879154j),
 (-0.009567894618501785-0.0008973444248954808j),
 (-0.022236085873274792-0.00379582363757411j),
 (-0.01820173001758473-0.008442032493103315j),
 (-0.004479740696424589-0.019154236293881792j),
 (-0.028900615851116366-0.0035034452607955163j),
 (0.0020119957811973333-0.0014612329240375175j),
 (-0.012464891029845127-0.005685163507650298j),
 (-0.010259183759933076-0.02228728493596673j),
 (-0.0188259858077732+0.010754181326826569j),
 (-0.018437333073759478-0.012366625991944026j),
 (0.0037287786070165727-0.011506429082852543j),
 (-0.0032036500436596125-0.0011275642814960265j),
 (-0.016804114610870443+0.005559969925367074j),
 (-0.010104105640581841+0.0003264350547173449j),
 (-0.0068108733682008035-0.009184708795421687j),
 (-0.011919375994038205+0.002528748364340796j),
 (-0.00886376072425299-0.005128442715692633j),
 (-0.006860720379432367-0.009530110954080349j),
 (-0.004457676232729338-0.0049259502647808874j),
 (-0.0056583763104127915+0.004552290894346716j),
 (-0.001579426546646942-0.003130094908832278j),
 (-0.011239090008670934-0.00021374087390926946j),
 (-0.007239965805789111+0.008101473824055771j),
 (-0.0043766361934680555-0.008685273647803657j),
 (0.0019927790995710667-0.004773308834731555j),
 (-0.007860702512319486+0.0038272124512427255j),
 (-0.00032160652865720265+0.007135364581448864j),
 (-0.016705676256814822-0.006828701594650052j),
 (-0.006001057294525209-0.0010393451749376292j),
 (-0.011601438079015166+0.0006215817717937753j),
 (-0.0016393809388836871-0.005498921213968165j),
 (-0.0033743022061581444-0.008605159290744558j),
 (0.0010221325337582804-0.0029695083593931195j),
 (-0.00471376943768337+0.006600799039938219j),
 (-0.006928203429386172+0.0010004850790106508j),
 (-0.010594346660732338-0.0062729045437064975j),
 (-0.011232921650586316+0.005378694558769071j),
 (-0.008074885045420033-0.0039712283050213045j),
 (0.0010782817508687265+0.0042555758985196365j),
 (-0.000810988494054231+0.002973260425604277j),
 (-0.0034950845748644974+0.00702313326906396j),
 (-0.004777278877783702+0.0007203608833157833j),
 (-0.006421203584644583+0.004442687054605809j),
 (-0.008246782767325388+0.0013397391154757114j),
 (-0.004455440919478132+0.0004936330572699662j),
 (-0.011980802791628224-0.005873211635706972j),
 (-1.6354462285179887-1.0080114347155646j),
 (1.4709878567368107-0.8162525878898261j),
 (0.32686970249576947+0.4635888324547828j),
 (0.5058612417969729+0.012249231532513918j),
 (0.5232685215780353-0.2319250472244146j),
 (0.25237893733890704+0.015328526160112408j),
 (0.5709733593900901-0.0939737997259608j),
 (0.27824814618589006-0.13111160990979653j),
 (0.13894544793492553+0.03373894921151012j),
 (0.21063018035707792-0.017801253781811355j),
 (0.03986396776683154+0.04102550528075424j),
 (0.12907338762253656+0.02716905462331607j),
 (0.2462296623188824+0.050880823614354816j),
 (0.01870513096162312-0.015516659980236443j),
 (0.0921197609323202-0.045002036629884376j),
 (0.08630848608645988+0.009426680314016367j),
 (-0.023011021256649965-0.016190548449650028j),
 (0.10329135617239557+0.10821722411695635j),
 (-0.06215895273227915-0.009772698185312715j),
 (0.04949624407077077+0.018234101234659898j),
 (0.043607935292456754+0.06856958571365686j),
 (-0.016481236732827812-0.043343744430594355j),
 (0.028606712446466627-0.015447239118139819j),
 (-0.0289661919047319+0.03958401873101926j),
 (0.044190213895275984-0.02720023033460924j),
 (0.03258244441507543+0.08347476964537161j),
 (0.09650862511403811-0.021755365501639572j),
 (0.09209967413774321+0.027517052407065243j),
 (0.10715556784135567+0.06731212327848693j),
 (0.12732461725070177-0.020207489523599863j),
 (0.08977791935710734+0.03876121460947687j),
 (0.04949765451759039-0.04740705346473128j),
 (0.057158109731605754+0.03861198310750102j),
 (-0.02392563830139861-0.016390979563678736j),
 (0.041469682042103266-0.03368458879808454j),
 (0.0027499536861528896-0.030414701880350684j),
 (0.07201976462545509+0.07645380242128268j),
 (0.030138233154565257+0.02488076944326674j),
 (0.03396887963290889-0.026488659658110435j),
 (0.08355242810804905-0.039782693682004946j),
 (0.06998876554337398+0.002979127011395918j),
 (0.040892683977582014+0.003052503106423847j),
 (0.02803374642625547+0.03469323466571685j),
 (0.04282660278728814-0.08738516026993969j),
 (0.061988333599876426-0.031890520850763056j),
 (-0.0026536578074216463+0.02577567402570015j),
 (0.034398896975052815+0.013147883275803567j),
 (0.057750255613484375+0.001767601723757519j),
 (0.05666699296673577+0.011160141896141817j),
 (0.004225850439293173-0.026090105828271943j),
 (0.05719014613079022-0.04488043130858664j),
 (0.015183566816331179+0.005367115774938679j),
 (0.038508021567700335-0.011721569129721594j),
 (0.010472680952856424+0.009586036536409341j),
 (0.012047035120614518-0.018483806014454134j),
 (0.023035019525553663-0.014605119258187459j),
 (0.021612781137507257-0.012038477545737697j),
 (0.04235189167591449-0.004408283037952435j),
 (0.022363611167278308-0.014291079994763653j),
 (0.04287157084236791+0.002800372540290997j),
 (0.013636741467829436-0.016046272127834084j),
 (-0.005682300106884018-0.009087690339753231j),
 (0.014893121275722156+0.0023439427196395106j),
 (0.029706304973737267+0.0005408985689709222j),
 (0.0143070504148595+0.014617572990435626j),
 (0.008358245056163583-0.024622971833853178j),
 (0.04528607989004885+0.00635150341599491j),
 (0.0216047871358383-0.008392923498548454j),
 (0.004610353529004362-0.008519075851959315j),
 (0.016009486034665836-0.019525662963764286j),
 (0.040987140255041285-0.00014275690070270444j),
 (0.021695901935080537+0.01240099602965393j),
 (0.030623886385896915-0.02294270408316917j),
 (0.013734221965205094-0.002379599115471646j),
 (0.017017960252770827-0.016486695285256304j),
 (0.0006314715818306162+0.0011646233019433176j),
 (0.026126170805197114-0.0029836140055067833j),
 (0.016401620885576788+0.0028397228759597425j),
 (0.004775429039121996+0.008304327248783617j),
 (0.02098305435372762-0.016021798357641313j),
 (0.019167066191562304+0.006952092908643812j),
 (0.00699985467926018-0.009009809508251457j),
 (0.0007078024583174772-0.013779289986655245j),
 (0.0025922798975281606-0.0024345293811077846j),
 (0.028495285565713045+0.0015040314005855004j),
 (0.012357625150420474-0.00020313840880848934j),
 (0.0081159668792549-6.362087947044332e-06j),
 (0.011844561587138792-0.005412705637988635j),
 (0.011934044463902699+0.0008787212759010681j),
 (0.0062675660018192015-0.00209191234317792j),
 (0.017905743935519924+0.00048743595695779874j),
 (0.010955259066351409+0.006263501994546135j),
 (0.018619442324408896+0.004803080416799835j),
 (0.01698341009405054-0.00011687642362042072j),
 (0.009648810763106553-0.007062497039071135j),
 (0.0028087447766122456+0.005884377776799169j),
 (0.0073432773426202495-0.0009501734220333592j),
 (0.019188217308460397+0.0011580625413090155j),
 (0.008965619064291865+0.0048682967804618265j),
 (0.010685534868632636+0.001729144979829247j),
 (0.012478384731704135-0.008159491704911554j),
 (0.0021378156834102836+0.0003381402567498461j),
 (0.006676900312471728+0.0005836932915033551j),
 (0.009294314388575973+0.0014228092557573306j),
 (0.01103609208274503+0.004157051843175317j),
 (0.017114613326551606+0.006635755708501432j),
 (0.011602338470324885+0.0010512283727574625j),
 (0.008198806454575347-0.0025724325179923434j),
 (0.006787523238661571+0.0034318387783275565j),
 (0.006220015938867225+0.003906476786314886j),
 (0.00827612911802599+0.0016577321333951136j),
 (0.008325419342859996-0.002595131800700365j),
 (0.01601469505695965+0.006026897718820727j),
 (0.01856953575589509-0.002870954355462599j),
 (0.014417329659718356-0.004471801924212628j),
 (0.011584246046215569-0.006130905363627317j),
 (0.00850858216246422+0.0003331929012992011j),
 (0.009736364295522168+0.0013654219629948817j),
 (0.0071376313200725875-0.002229540445734163j),
 (0.0017568109986649373+0.010099252693453877j)]
NNN=120





class FourierCirclesScene:
    def __init__(self, A_k, N):
        self.N = N
        self.c_pos_freq=A_k[1:N+1]
        self.c_neg_freq=A_k[N+1:]
        self.c_0=A_k[0]

    def comp_to_vec(self,x):
        r=abs(x)
        
        theta=np.log(x).imag
        return  np.array([r*np.cos(theta),r*np.sin(theta)])


    def step(self, delta_t):
        # updating
        for k in range(len(self.c_pos_freq)):
            self.c_pos_freq[k]*=np.exp(2*np.pi*(k+1)*delta_t*1j)
            self.c_neg_freq[k]*=np.exp(-2*np.pi*(k+1)*delta_t*1j)
    def vec(self,type="c",number=0):
        if type=="c":  
            return self.comp_to_vec(self.c_0)
        elif type=="p":
            return self.comp_to_vec(self.c_pos_freq[number])
        elif type=="n":
            return self.comp_to_vec(self.c_neg_freq[number])
    
           
class Epicycles(Scene):
    def construct(self):
        MF_coefs = FourierCirclesScene(A_coef,NNN)
        def get_epicycle(MF_coefs):
            V_0=MF_coefs.vec("c")
            points = [np.array([V_0[0],V_0[1],0])]
            for i in range(NNN):
                V1=MF_coefs.vec("p",i)
                V2=MF_coefs.vec("n",i)
                x_=V1[0]+points[-1][0]
                y_=V1[1]+points[-1][1]
                points+=[np.array([x_,y_,0]),np.array([x_+V2[0],y_+V2[1],0])]
            
            return [ Arrow(buff=np.linalg.norm(points[i]-points[i - 1]),start=points[i - 1],end=points[i]) for i in range(1, len(points)) ] 
        def get_points(MF_coefs):
            V_0=MF_coefs.vec("c")
            points = [np.array([V_0[0],V_0[1],0])]
            for i in range(NNN):
                V1=MF_coefs.vec("p",i)
                V2=MF_coefs.vec("n",i)
                x_=V1[0]+points[-1][0]
                y_=V1[1]+points[-1][1]
                points+=[np.array([x_,y_,0]),np.array([x_+V2[0],y_+V2[1],0])]
            
            return [ (points[i - 1],points[i]) for i in range(1, len(points))]
        

        
        def step(All_g, dt):
            '''
            f.remove(*f)      
            
            MF_coefs.step(dt/2)
            
            for obj in get_epicycle(MF_coefs):
                f.add(obj)
            a=Tex(str(len(self.mobjects)))    
            f.add(a)
            '''
            MF_coefs.step(dt/30)
            ii=0
            p=get_points(MF_coefs)
            end_p1=All_g.submobjects[0].submobjects[-1].get_end()
            for obj in All_g.submobjects[0]:
                obj.become( Arrow(buff=np.linalg.norm(p[ii][0]-p[ii][1]),start=p[ii][0],end=p[ii][1]))
                ii+=1
            end_p2=All_g.submobjects[0].submobjects[-1].get_end()
            All_g.submobjects[1].add(Line(end_p1,end_p2,color=YELLOW))    
        
            
 
            

                

        first = VGroup()
        second=VGroup()
        All_g=VGroup().add(first,second)
        for obj in get_epicycle(MF_coefs):
            first.add(obj)
          
            
        
        All_g.add_updater(step)
        self.add(All_g)    
        
        
        self.wait(30)
        All_g.remove_updater(step)
        
    
        
         
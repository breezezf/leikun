import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('(＾－＾)V', ['封页(*^▽^*)','兴趣推荐(ﾟДﾟノ)','音乐专题ᕦ(･ㅂ･)ᕤ','图片改色┓(;´_｀)┏','─=≡Σ(((つ•̀ω•́)つ词典','讨论区(︶.̮︶✽)'])

# ——-————————————————————————————————————————-————————————————————————————————————————————————
def page1():
    '''兴趣推荐'''
    tab1,tab2,tab3,tab4 = st.tabs(["电影推荐","游戏推荐","书籍推荐","习题集推荐"])
    with tab1:
        st.subheader(':blue[电影推荐]')
        st.caption(':red[(备注：排名仅为入站顺序)]')        
        st.caption('(-----如有推荐请留言)')
        st.caption('---')
        st.write('1. 《阿甘正传》',)
        st.image('屏幕截图 2024-02-20 170259.png')
        st.write('2. 《肖申克的救赎》',)
        st.image('屏幕截图 2024-02-20 171309.png')
        st.write('3. 《哈利波特与死亡圣器》')
        st.image('屏幕截图 2024-02-20 174938.png')
        st.write('4. 《异界》')
        st.image('异界.png')
        st.write('5. 《千星之城》')
        st.image('千星之城.png')
        st.write('6. 《星际穿越》')
        st.image('星际穿越.png')
    with tab2:
        st.subheader(':blue[游戏推荐]')
        st.caption(':red[提示：游戏属于个人喜好，不爱请别伤害]')
        st.caption('---')
        st.write('1. 原神')
        st.image('原神图片.png')
        st.write('2. 崩坏:星穹铁道')
        st.image('崩坏星穹铁道.png')
        st.write('3. 我的世界')
        st.image('我的世界.png')
        st.write(':grey[(如有推荐请留言)]')
    with tab3:
        st.subheader(':blue[书籍推荐]')
        st.write(':grey[站主认为以下每本都是经典，如有可能建议都读读]')
        st.caption(':grey[(如有推荐请留言)]')        
        st.caption('---')
        st.write('《天才在左，疯子在右》')
        st.image('天才在左疯子在右图片.png')
        st.write('《苏菲的世界》')
        st.image('苏菲的世界.png')
        st.write('《理想国》')
        st.image('理想国.png')
        st.write('《中国哲学简史》')
        st.image('中国哲学简史.png')
        st.write('《人生的智慧》')
        st.image('人生的智慧.png')
        st.write('《当尼采哭泣》')
        st.image('当尼采哭泣.png')
        st.write('《沉思录》')
        st.image('沉思录.png')
    with tab4:
        st.subheader(':blue[习题集推荐]')
        st.caption(':grey[(如有推荐请留言)]')  
        st.caption('---')
        st.write('《五年模拟，三年高考》')
        st.write(':grey[[示例图片为语文]]')
        st.image('五年模拟三年高考-语文.png')
# ——————————————————————————————————————————————————————————————————————————————————————
def page2():
    '''图片改色'''
    st.subheader(":blue[:sunglasses:图片改色:sunglasses:]")
    st.caption('---')
    uploaded_file = st.file_uploader("上传图片", type=['png','jpeg','jpg'])
    st.caption('---')
    if uploaded_file:
        # 获取图片文件的名称，类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 创建副栏
        tab1,tab2,tab3,tab4 = st.tabs(["原色","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 2, 0, 1))
    st.caption('---')        
# 处理图片
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
# ————————————————————————————————————————————————————————————————————————————
def page3():
    '''词典'''
    st.subheader(':blue[词典(英译汉)]')
    st.caption('---')
    # 从本地文件中将词典信息读取出来，并储存在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 本地文件中将单词的查询次数读取出来，并储存在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    st.caption('---')
# ——————————————————————————————————————————————————————————————————————————————————————————
def page4():
    '''讨论区'''
    st.write('讨论区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '狗头军师':
            with st.chat_message('🐶'):
                st.write(i[1],':',i[2])
        elif i[1]=='书熟鼠数':
            with st.chat_message('🐀'):
                st.write(i[1],':',i[2])
        elif i[1] == '智客':
            with st.chat_message('🎭'):
                st.write(i[1],':',i[2])
    name = st.selectbox('您是...', ['狗头军师','书熟鼠数','智客'])
    new_message = st.text_input('您对本网站的评价(建议)...')
    if st.button('发送'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
# ——————————————————————————————————————————————————————————————————————————————————
def page5():
    '''封页'''
    st.snow()
    with open('崔铭珈 - 2019无敌大串烧 [mqms2].ogg', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/ogg', start_time=0)
    st.caption('---')
    st.image('夕阳1.png')
    st.header(':blue[-]:red[-]—:blue[-]:red[-]—:blue[-]—:red[-]—:blue[-]—:blue[欢迎使用本网站]—:blue[-]—:red[-]—:blue[-]—:red[-]:blue[-]—:red[-]:blue[-]')
    st.caption('|ू･ω･` )')
    st.image('夕阳2.png')
    st.caption('---')
    col1,col3,col4,col2 = st.columns([1, 1,0.3,1])
    with col2:
        st.caption('[点击左侧侧边栏切换网站网页]')
    st.snow()
# ——————————————————————————————————————————————————————————————————————————————————
def page6():
    '''音乐专题'''
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.01)
        roading.progress(i, '叮,由于数据过多需要加载！'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    
    st.subheader(':blue[音乐]')
    st.caption('---')
    
    # st.write("  :blue[歌名：]未收录")
    # st.caption(":blue[歌手：]未收录")
    # st.caption(':blue[作曲：]未收录:blue[作词：]未收录')
    # with open('未收录.ogg/mp3/flac', 'rb') as f:
    #     mymp3 = f.read()
    # st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
    # with open('未收录.ogg|mp3|flac','rb')as f:
    #     a = f.read()
    # st.download_button(label='下载该歌曲', data = a ,file_name= '未收录')
    # st.caption('---')

    go = st.selectbox('点击下列切换歌曲', ['编程猫的梦想', '2019无敌大串烧', '不再过问','出山','说书人','爆丸天地','战国时代','But U','淋雨一直走','关于孤独','这份爱会不会会不会','So Far Away','虚拟'])
    st.caption('---')
    if go == '编程猫的梦想':
        # 打印字所用代码
        st.write("  :blue[歌名：]编程猫的梦想")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]海棠不言")
        with col2:
            st.caption(':blue[作曲：]阿丧')
        with col3:
            st.caption(':blue[作词：]阿丧')
        # 播放音乐所用代码
        with open('海棠不言 - 编程猫的梦想.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        # 下载音乐所用代码    
        with open('海棠不言 - 编程猫的梦想.mp3','rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '海棠不言 - 编程猫的梦想')
        st.caption('---')
    elif go == '2019无敌大串烧':
        st.write("  :blue[歌名：]2019无敌大串烧")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]沈虫虫、崔铭珈、蓝心羽、黄唯铭、Joysaaaa、可能是雨雨、热心市民谈阿姨")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('崔铭珈 - 2019无敌大串烧 [mqms2].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg', start_time=0)
        with open('崔铭珈 - 2019无敌大串烧 [mqms2].ogg','rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '沈虫虫、崔铭珈、蓝心羽、黄唯铭、Joysaaaa、可能是雨雨、热心市民谈阿姨 - 2019无敌大串烧')
        st.caption('---')
    elif go == '不再过问':
        st.write("  :blue[歌名：]不再过问")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('九宫格&郑雨泽 - 不再过问 (DJ版) [mqms2].flac', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/flac', start_time=0)
        with open('九宫格&郑雨泽 - 不再过问 (DJ版) [mqms2].flac','rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '九宫格&郑雨泽 - 不再过问')
        st.caption('---')
    elif go == '出山':
        st.write("  :blue[歌名：]出山")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('老陈酒 - 出山 [mqms2].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg', start_time=0)
        with open('老陈酒 - 出山 [mqms2].ogg', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '老陈酒 - 出山')
        st.caption('---')
    elif go == '说书人':
        st.write("  :blue[歌名：]说书人")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('洛少爷 - 说书人 [mqms2].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('洛少爷 - 说书人 [mqms2].ogg', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '洛少爷 - 说书人')
        st.caption('---')
    elif go == '爆丸天地': 
        st.write("  :blue[歌名：]爆丸天地")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('孙晔 - 爆丸天地 [mqms].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('孙晔 - 爆丸天地 [mqms].ogg', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '孙晔 - 爆丸天地')
        st.caption('---')
    elif go == '战国时代':
        st.write("  :blue[歌名：]战国时代")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('王强 - 战国时代 [mqms].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('王强 - 战国时代 [mqms].ogg', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '王强 - 战国时代')
        st.caption('---')
    elif go == 'But U':
        st.write("  :blue[歌名：]But U")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('勿念 - But U [mqms2].flac', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('勿念 - But U [mqms2].flac', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '勿念 - But U')
        st.caption('---')
    elif go == '淋雨一直走':
        st.write("  :blue[歌名：]淋雨一直走")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('张韶涵 - 淋雨一直走 [mqms2].flac', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('张韶涵 - 淋雨一直走 [mqms2].flac', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '张韶涵 - 淋雨一直走')
        st.caption('---')
    elif go == '关于孤独':
        st.write("  :blue[歌名：]关于孤独")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('赵俊飞 - 关于孤独 [mqms2].flac', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('赵俊飞 - 关于孤独 [mqms2].flac', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '赵俊飞 - 关于孤独')
        st.caption('---')
    elif go == '这份爱会不会会不会':
        st.write("  :blue[歌名：]这份爱会不会会不会")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('DJRE - 这份爱会不会会不会 (Remix) [mqms2].ogg', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/ogg|mp3|flac', start_time=0)
        with open('DJRE - 这份爱会不会会不会 (Remix) [mqms2].ogg', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= 'DJRE - 这份爱会不会会不会')
        st.caption('---')
    elif go == 'So Far Away':
        st.write("  :blue[歌名：]So Far Away.mp3")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('陆鳐LuLu - So Far Away.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        with open('陆鳐LuLu - So Far Away.mp3', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '陆鳐LuLu - So Far Away')
        st.caption('---')
    elif go == '虚拟':
        st.write("  :blue[歌名：]虚拟")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 2.5])
        with col1:
            st.caption(":blue[歌手：]未收录")
        with col2:
            st.caption(':blue[作曲：]未收录')
        with col3:
            st.caption(':blue[作词：]未收录')
        with open('云汐 - 虚拟.mp3', 'rb') as f:
            mymp3 = f.read()
        st.audio(mymp3, format='audio/mp3', start_time=0)
        with open('云汐 - 虚拟.mp3', 'rb')as f:
            a = f.read()
        st.download_button(label='下载该歌曲', data = a ,file_name= '云汐 - 虚拟')
        st.caption('---')

    st.link_button('推荐一个听歌软件(点击跳转网页)', 'https://www.kugou.com/')
    
# —————————————————————————————————————————————————————————————————————————————————
if page == '兴趣推荐(ﾟДﾟノ)':
    page1()
elif page=='图片改色┓(;´_｀)┏':
    page2()
elif page=='─=≡Σ(((つ•̀ω•́)つ词典':
    page3()
elif page=='讨论区(︶.̮︶✽)':
    page4()
elif page=='封页(*^▽^*)':
    page5()
elif page=='音乐专题ᕦ(･ㅂ･)ᕤ':
    page6()
